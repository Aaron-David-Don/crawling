const fs = require('fs');
const csv = require('csv-parser');
const axios = require('axios');
const cheerio = require('cheerio');
const Replicate = require('replicate');

const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
});
// Function to extract URLs from a CSV file
function extractUrlsFromCsv(filename, callback) {
    const urls = [];
    fs.createReadStream(filename)
        .pipe(csv())
        .on('data', (row) => {
            // Assuming the URL is in the 4th column (index 3)
            urls.push(row[Object.keys(row)[3]]);
        })
        .on('end', () => {
            callback(urls);
        })
        .on('error', (error) => {
            console.error(`Error: ${error.message}`);
        });
}

// Function to scrape text from a URL
async function scrapeTextFromUrl(url) {
    try {
        const response = await axios.get(url);
        const html = response.data;
        const $ = cheerio.load(html);

        // Remove scripts and styles
        $('script, style').remove();

        // Get the entire text content without HTML tags
        let textContent = $.root().text();

        // Remove empty lines and trim each line
        const cleanedTextContent = textContent
            .split('\n')            // Split content into lines
            .map(line => line.trim()) // Trim each line to remove extra spaces
            .filter(line => line.length > 0) // Filter out empty lines
            .join('\n');            // Join the lines back together

        return cleanedTextContent;
    } catch (error) {
        console.log(`Error scraping ${url}:`, error.message);
        return null;
    }
}

// Function to append data to a JSON file
function appendToJsonFile(data, filename = 'output.json') {
    let existingData = [];
    if (fs.existsSync(filename)) {
        const fileContent = fs.readFileSync(filename);
        existingData = JSON.parse(fileContent);
    }

    existingData.push(data);

    fs.writeFileSync(filename, JSON.stringify(existingData, null, 4));
}

// Function to process each URL and get JSON response from Replicate
async function processUrls(urls) {
    for (const url of urls) {
        const scrapedContent = await scrapeTextFromUrl(url);
        if (!scrapedContent) continue;

        try {
            const result = await replicate.stream(
                "meta/meta-llama-3-8b-instruct",
                {
                    input: {
                        "top_k": 0,
                        "top_p": 0.95,
                        "prompt": scrapedContent,
                        "max_tokens": 512,
                        "temperature": 0.7,
                        "system_prompt": "user will paster a paper webpage content ,you need to extract TITLE and ABSTRACT and DOI from the text and output in json,output json directly do not add any formatting ,just direct json syntax output,also do not add \"Here is the extracted information in JSON\" sentence just output json title,abstract,doi",
                        "length_penalty": 1,
                        "max_new_tokens": 512,
                        "stop_sequences": ",",
                        "prompt_template": "system\n\n{system_prompt}user\n\n{prompt}assistant\n\n",
                        "presence_penalty": 0,
                        "log_performance_metrics": false
                    }
                }
            );

            // Validate if result is valid JSON
            const data = JSON.parse(result);
            console.log("Valid JSON:", data);
            appendToJsonFile(data);
        } catch (error) {
            console.error("Failed to get or decode JSON:", error);
            // Handle the error or debug further
        }
    }
}

// Specify the CSV file name
const csvFilename = 'googlescrape.csv';

// Extract URLs from the CSV file and process them
extractUrlsFromCsv(csvFilename, (urlsList) => {
    processUrls(urlsList);
});