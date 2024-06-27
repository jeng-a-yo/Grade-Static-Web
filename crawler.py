import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
from timer import timing_decorator

# Base URL of the exam papers page
base_url = "https://www.ceec.edu.tw/xmfile?xsmsid=0J052424829869345634"
download_dir = "all_files"

# Create download directory
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

@timing_decorator
def download_pdfs(url):
    # Send HTTP GET request
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    # Parse the webpage content
    soup = BeautifulSoup(response.text, 'html.parser')



    # Find all links to exam papers (excluding answer sheets and Word files)
    links = soup.find_all('a', href=True)
    pdf_links = [link['href'] for link in links if link['href'].endswith('.pdf') and '解答' not in link.text and '答案' not in link.text]

    # Download exam papers
    for pdf_link in pdf_links:
        pdf_url = pdf_link if pdf_link.startswith('http') else f"https://www.ceec.edu.tw{pdf_link}"
        pdf_name_encoded = pdf_url.split('/')[-1]
        pdf_name = urllib.parse.unquote(pdf_name_encoded)  # Decode URL-encoded filename
        pdf_response = requests.get(pdf_url)

            # Check if the page contains content for the year 95
        if "94" in pdf_name:
            print("Reached the year 95, stopping download.")
            return
        
        # Save PDF file
        with open(os.path.join(download_dir, pdf_name), 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        print(f"Downloaded {pdf_name}")

    # Find the next page link and recursively download PDFs
    next_page = soup.find('a', string='下一頁')
    if next_page and 'href' in next_page.attrs:
        next_page_url = next_page['href']
        if not next_page_url.startswith('http'):
            next_page_url = f"https://www.ceec.edu.tw{next_page_url}"
        download_pdfs(next_page_url)

# Start downloading from the base URL
download_pdfs(base_url)

print("All files downloaded successfully.")
