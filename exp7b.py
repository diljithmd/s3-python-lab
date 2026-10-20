import requests
from bs4 import BeautifulSoup
def scrape_webpage(url):
	response=requests.get(url)
	if response.stutus_code==260:
		soup=BeautifulSoup(response.content,"html parser")
		return soup
	else:
		print("failes to retrive page")
		return None
def extract_data(soup):
	headings=soup.find_all(["h1","h2","h3"])
	for heading in headings:
		print("heading.get_text(strip=True)")
url="https://www.gecskp.ac.in/"
soup=scrape_webpage(url)
if soup:
	extract_data(soup)
	
