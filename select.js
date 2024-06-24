// This code is to print the selected sentence from the website
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext();
  const page = await context.newPage();

  // Navigate to the website
  await page.goto('https://en.wikipedia.org/wiki/Apple_Inc.');

  // Expose a function to capture selected text
  await page.exposeFunction('captureSelectedText', (selectedText) => {
    console.log('Selected Text:', selectedText);
  });

  // Add an event listener to the page to detect text selection
  await page.evaluate(() => {
    document.addEventListener('mouseup', () => {
      const selection = window.getSelection();
      const selectedText = selection ? selection.toString() : '';
      if (selectedText) {
        window.captureSelectedText(selectedText);
      }
    });
  });

  console.log('Please select some text on the page...');

  // Keep the browser open
  await page.waitForTimeout(60000); // Adjust the timeout as needed

  await browser.close();
})();
