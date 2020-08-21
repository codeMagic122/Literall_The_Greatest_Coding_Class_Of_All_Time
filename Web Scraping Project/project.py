# Today we're going to learn about the basics of web scraping! Don't worry about the fact that none of the things you're doing make sense! 
# We'll go step by step, and take the time to answer any and all questions you might have :D

# Import the libraries that are needed for this project
import requests
from bs4 import BeautifulSoup

# Get the url of the website you want to scrape, and set it as the value of 'link'
link = "https://www.economist.com/business/2020/08/18/america-closes-the-last-loophole-in-its-hounding-of-huawei"

# Request the link
page = requests.get(link)

# Parse the data that our get request returns into a form that we can then use
soup = BeautifulSoup(page.content,'html.parser')

paragraphs = soup.findAll('p',{'class':'article__body-text'})
article = ''
for paragraph in paragraphs:
  article += paragraph.text
print(article)