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

# Print the value of soup in the console to check that your code worked
print(soup)

# PART 2 - Make sure that the link you've selected goes to an article from the economist!
# At this point, we've now learned how to get all the data we can possibly get from the website of our choice. But how do we get specific pieces of data? Like how do we get the text of an article, and nothing else?
# This is where Beautiful Soup comes in handy. Beautiful Soup allows us to parse the data we get back from a website, to only get information that we care about
