from bs4 import BeautifulSoup
soup=BeautifulSoup("<p>some<b>bad<i>HTML")
print(soup.prettify())

