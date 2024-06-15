  //this code is to fetch only the text content of the given webiste
const axios = require('axios');
  const cheerio = require('cheerio');
  
  axios.get('https://replicate.com/')
    .then(response => {
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
  
      console.log(cleanedTextContent);
    })
    .catch(error => {
      console.log("Error:", error.message);
    });
