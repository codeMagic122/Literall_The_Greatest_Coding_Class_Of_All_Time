## Introduction
Today, my goal is to blow your minds! The code we're going to write will be simple - it will be only 10-13 lines in length - but I hope that by the end of our lesson you realize just how powerful a language plus a packages can be! To start, head over to repl.it, create a free account, and open up a new Python REPL.

## Importing dependencies
Dependencies are packages with functionality that we are able to use. You can think about them as functions that people have created so that it's easier and faster for you to write your code. For web scraping, the two packages which we will use are Beautiful Soup and Requests

```python
import requests
from bs4 import BeauitfulSoup
```

## Requesting a website
In the world of coding, there are multiple different types of request that a computer can make, in order to achieve a certain goal. For example, when a computer wants to send data somewhere, then it uses a POST request. If a computer wants to update data, it uses a PUT request. For web scraping, when a computer wants to get data from a website, then it uses a GET request. Using the requests package, our work becomes very simple. 

All you have to do is create a link variable with the value of the url of the website you want to scrape, and then you use requests.get() to get the data from that site.

```python
link = 'https://www.economist.com/business/2020/08/18/america-closes-the-last-loophole-in-its-hounding-of-huawei'
page = requests.get(link)
print(page)
```

## Making our 'page' data readable
Now that we've requested a url using the requests package, we need to convert the data that we've gotten back into a a readable form. This is where BeauitfulSoup comes in. Simply put, BeauitfulSoup converts the raw data that requests gets us, and converts it into a form that's easier to then analyze and get specific pieces of data from. 

Once you've added the code below, comment out the previous print statement.

```python
soup = BeauitfulSoup(page.content,'html.parser')
print(soup)
```
