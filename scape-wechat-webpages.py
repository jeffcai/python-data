import requests
from bs4 import BeautifulSoup
import pdfkit
import os

def scrape_links(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the page: {response.status_code}")
        return []

    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links in the page
    links = soup.find_all('a')
    hrefs = []

    # Extract href attributes
    for link in links:
        href = link.get('href')
        if href:
            # Resolve relative URLs
            full_url = requests.compat.urljoin(url, href)
            hrefs.append(full_url)

    return hrefs

def convert_links_to_pdf(links):
    for link in links:
        # Generate a valid filename for the PDF
        file_name = link.split('/')[-1].replace('.html', '').replace('.php', '') + '.pdf'

        # Convert the linked page to PDF
        try:
            print(f"Converting {link} to {file_name}...")
            pdfkit.from_url(link, file_name)
            print(f"Saved: {file_name}")
        except Exception as e:
            print(f"Failed to convert {link}: {e}")

if __name__ == "__main__":
    url = 'https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg4NzY3NzIwOA==&action=getalbum&album_id=2057539721295200257&scene=173'  # Replace with the target URL
    links = scrape_links(url)

    if links:
        print(f"Found {len(links)} links.")
        convert_links_to_pdf(links)
    else:
        print("No links found.")
