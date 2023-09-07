import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
from io import BytesIO
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your Tesseract path

# Rest of your code...


# Set the URL of the web page where the captcha and form are located
url = 'https://www.amazon.com/errors/validateCaptcha'

# Set user-agent to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Step 1: Fetch the captcha image URL from the web page
webpage = requests.get(url, headers=headers).text
soup = BeautifulSoup(webpage, 'lxml')
img_tags = soup.find_all('img')
if img_tags:
    captcha_image_url = img_tags[0]['src']
    print("Captcha Image URL:", captcha_image_url)
else:
    print("No img tags found in the HTML")

# Step 2: Download and process the captcha image
response = requests.get(captcha_image_url)
captcha_image = Image.open(BytesIO(response.content))
img_gray = captcha_image.convert('L')
img_thresholded = img_gray.point(lambda x: 0 if x < 200 else 255, '1')

# Step 3: Use Tesseract OCR to extract text from the captcha image
custom_config = r'--oem 3 --psm 6 -l eng'
captcha_text = pytesseract.image_to_string(img_thresholded, config=custom_config)
print("Extracted Captcha Text:", captcha_text)

# Step 4: Submit the captcha text to the form
data = {'input_field_name': captcha_text}
response = requests.post(url, data=data, headers=headers)

# Step 5: Check the response for success and extract the next page URL
if response.status_code == 200:
    print("Data successfully submitted.")
    soup = BeautifulSoup(response.text, 'html.parser')
    next_page_link = soup.find('a', {'class': 'next-page-link'})
    if next_page_link:
        next_page_url = next_page_link.get('href')
        print("Next Page URL:", next_page_url)
    else:
        print("Next page link not found.")
else:
    print(f"Failed to submit data. Status code: {response.status_code}")
