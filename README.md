# Web Scraping with Captcha Handling

## Overview
This Python script demonstrates how to automate web scraping while handling CAPTCHA challenges. It uses popular libraries such as BeautifulSoup for HTML parsing, requests for making HTTP requests, Pillow for image processing, and pytesseract for OCR (Optical Character Recognition) to solve CAPTCHAs.

## Prerequisites
- Python 3.x
- Tesseract OCR installed (https://github.com/tesseract-ocr/tesseract)

## Installation
1. Install the required Python libraries:
   ```
   pip install requests beautifulsoup4 pillow pytesseract
   ```

2. Install Tesseract OCR and add it to your system's PATH.
   - Download Tesseract OCR: https://github.com/tesseract-ocr/tesseract
   - Follow the installation instructions for your operating system.

## Usage
1. Update the script with your specific URL where the CAPTCHA and form are located.
2. Set the user-agent in the headers to mimic a web browser.
3. Modify the custom_config variable in Step 3 according to your language and desired OCR settings.
4. Run the script using Python:
   ```
   python captcha_solver.py
   ```

## Explanation of the Approach
This script demonstrates a step-by-step approach to automate web scraping while dealing with CAPTCHA challenges.

### Step 1: Fetching CAPTCHA Image URL
- Use the `requests` library to fetch the web page content.
- Parse the HTML using BeautifulSoup (`beautifulsoup4`) to locate the CAPTCHA image tag.
- Extract the CAPTCHA image URL.

### Step 2: Downloading and Processing CAPTCHA Image
- Use `requests` to download the CAPTCHA image.
- Open the downloaded image using Pillow (`PIL`).
- Convert the image to grayscale and apply thresholding to binarize it.
- Prepare the image for OCR using `pytesseract`.

### Step 3: Extracting CAPTCHA Text
- Use Tesseract OCR (`pytesseract`) to extract text from the processed CAPTCHA image.
- Customize OCR settings as needed by modifying the `custom_config` variable.

### Step 4: Submitting CAPTCHA Text
- Prepare the data to be submitted to the form with the extracted CAPTCHA text.
- Use `requests` to submit the form data to the web page.

### Step 5: Checking Response and Extracting Next Page URL
- Check the HTTP response for success (status code 200).
- Parse the response HTML using BeautifulSoup to locate the next page link.
- Extract the URL of the next page if available.

### Step 6: Scrape and Print Full Page Content
- If the response was successful, scrape the full page content using `response.text`.
- Print the full HTML content of the page.

## Additional Notes
- This script uses Tesseract OCR to handle CAPTCHAs. Ensure that Tesseract is installed and configured correctly on your system.
- You can customize the user-agent string to mimic different web browsers or devices by modifying the `headers` dictionary.
- The script can be further extended to handle different CAPTCHA types and form submissions.

```
##Reason for Using Tesseract:**

-Tesseract OCR (Optical Character Recognition) was chosen because it provides a reliable, open-source, and platform-agnostic solution for converting CAPTCHA images into text. This choice aligns with the script's -requirement to avoid using external captcha-solving services and ensures the script can run independently on various systems while delivering accurate text extraction from images.
