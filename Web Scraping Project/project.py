# Import packages
import requests
from bs4 import BeautifulSoup

# Url of article you want to request
link = "https://www.economist.com/business/2020/08/18/america-closes-the-last-loophole-in-its-hounding-of-huawei"

# Request the link
page = requests.get(link)

# Make data readable with Beautiful Soup
soup = BeautifulSoup(page.content,'html.parser')

# Parse article paragraphs from soup
paragraphs = soup.findAll('p',{'class':'article__body-text'})

# Convert paragraphs into plaintext article
article = ''
for paragraph in paragraphs:
  article += paragraph.text
  
#  Print article
print(article)
