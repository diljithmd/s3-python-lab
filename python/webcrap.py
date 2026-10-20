import requests
from bs4 import BeautifulSoup

def scrape_web_page(url):
    """
    Fetches a web page and parses it with BeautifulSoup.
    
    Args:
        url (str): The URL of the webpage to scrape.
        
    Returns:
        BeautifulSoup object or None: The parsed soup object on success, 
                                     or None on failure.
    """
    response = requests.get(url)
    
    if response.status_code == 200:
        # 'html.parser' is a built-in Python parser
        soup = BeautifulSoup(response.content, 'html.parser') 
        return soup
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

def extract_data(soup):
    """
    Extracts and prints the text content of all h1, h2, and h3 heading tags.
    
    Args:
        soup (BeautifulSoup): The parsed BeautifulSoup object of the webpage.
    """
    # Find all h1, h2, and h3 tags
    headings = soup.find_all(['h1', 'h2', 'h3']) 
    
    for heading in headings:
        # Get the text content, removing leading/trailing whitespace
        print(heading.get_text(strip=True)) 

# --- Main execution ---
# Note: The URL in the image appears to be a local or non-public one.
# I'm reproducing it as written, but it likely won't work without access 
# to that specific host.
url = 'https://llget.skp-ac.in' 

# Scrape the page
soup = scrape_web_page(url)

# If the scraping was successful, extract the data
if soup:
    extract_data(soup)