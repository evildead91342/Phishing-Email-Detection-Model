from bs4 import BeautifulSoup
from urllib import request
import requests

url = 'https://monkey.org/~jose/phishing/phishing-2020'


# Page content from Website URL
page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser").encode("UTF-8")
soup = BeautifulSoup(page.content, "html.parser").encode("UTF-8")
print(soup)
# print(soup)
# Function to remove tags
# Pull all text from the BodyText div
# artist_name_list = soup.find(class_='')

# Pull text from all instances of <a> tag within BodyText div
# artist_name_list_items = artist_name_list.find_all('a')
# Create for loop to print out all artists' names
# for artist_name in artist_name_list_items:
# print(artist_name.prettify())

# Print the extracted data
# print(page.content)
"""resp = requests.get('https://en.wikipedia.org/wiki/NIFTY_50')
print(resp)
soup = BeautifulSoup(request.urlopen(url).read(), "html.parser")
print(soup.encode("UTF-8"))
# w = soup.encode("UTF-8")
"""
"""
soup = BeautifulSoup(request.urlopen(url).read(), "lxml")
print(soup.encode("utf-8"))
"""
"""
with open("phishing-2020_2.mbox", "a") as f:
    print(soup.get_text(), file=f)
"""
