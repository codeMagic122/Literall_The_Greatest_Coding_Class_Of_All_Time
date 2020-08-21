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

## Parsing specific information
Now that we've successfully beautified our requested data with Beautiful Soup, the next step is to parse it! Parsing, is the process of getting specific pieces of data from a larger dataset. In our case, it's going to be getting the text of an economist article from all the data that on the page where that article exists. However, before we do so, we're going to need a quick introduction to HTML, the skeleton structure of every website you'll ever use (probably)!

The first thing you need to know about HTML is that it stores data in TAGS! The basic structure of a tag looks like:

```html
<[tag name]>[data]</[tag name]>
```

Here's an example showing real html on google.com that I accessed through the Developer Console:

```html
<div class="o3j99 c93Gbe">
  <style data-iml="1598035321037">.c93Gbe{background:#f2f2f2}.SSwjIe{padding:0 20px}.KxwPGc{display:flex;flex-wrap:wrap;justify-content:space-between}@media only screen and (max-width:1200px){.KxwPGc{justify-content:space-evenly}}.pHiOh{display:block;padding:15px;white-space:nowrap}a.pHiOh{color:#5f6368}</style>
  <div class="KxwPGc SSwjIe">
    <div class="KxwPGc"><a class="pHiOh" href="https://www.google.com/intl/en_us/ads/?subid=ww-ww-et-g-awa-a-g_hpafoot1_1!o2&amp;utm_source=google.com&amp;utm_medium=referral&amp;utm_campaign=google_hpafooter&amp;fg=1" ping="/url?sa=t&amp;rct=j&amp;source=webhp&amp;url=https://www.google.com/intl/en_us/ads/%3Fsubid%3Dww-ww-et-g-awa-a-g_hpafoot1_1!o2%26utm_source%3Dgoogle.com%26utm_medium%3Dreferral%26utm_campaign%3Dgoogle_hpafooter%26fg%3D1&amp;ved=0ahUKEwi2tf-8-azrAhXfHDQIHdPRAvoQkdQCCBA">Advertising</a><a class="pHiOh" href="https://www.google.com/services/?subid=ww-ww-et-g-awa-a-g_hpbfoot1_1!o2&amp;utm_source=google.com&amp;utm_medium=referral&amp;utm_campaign=google_hpbfooter&amp;fg=1" ping="/url?sa=t&amp;rct=j&amp;source=webhp&amp;url=https://www.google.com/services/%3Fsubid%3Dww-ww-et-g-awa-a-g_hpbfoot1_1!o2%26utm_source%3Dgoogle.com%26utm_medium%3Dreferral%26utm_campaign%3Dgoogle_hpbfooter%26fg%3D1&amp;ved=0ahUKEwi2tf-8-azrAhXfHDQIHdPRAvoQktQCCBE">Business</a><a class="pHiOh" href="https://google.com/search/howsearchworks/?fg=1">  How Search works </a></div>
    <div class="KxwPGc"><a class="pHiOh" href="https://policies.google.com/privacy?hl=en&amp;fg=1" ping="/url?sa=t&amp;rct=j&amp;source=webhp&amp;url=https://policies.google.com/privacy%3Fhl%3Den%26fg%3D1&amp;ved=0ahUKEwi2tf-8-azrAhXfHDQIHdPRAvoQ8awCCBI">Privacy</a><a class="pHiOh" href="https://policies.google.com/terms?hl=en&amp;fg=1" ping="/url?sa=t&amp;rct=j&amp;source=webhp&amp;url=https://policies.google.com/terms%3Fhl%3Den%26fg%3D1&amp;ved=0ahUKEwi2tf-8-azrAhXfHDQIHdPRAvoQ8qwCCBM">Terms</a>
      <div jscontroller="HFyn5c" class="ayzqOc"><style data-iml="1598035321038">.ayzqOc{position:relative}.EzVRq{display:block;padding:15px;white-space:nowrap}a.EzVRq,button.EzVRq{color:#5f6368}button.EzVRq{cursor:pointer;width:100%;text-align:left}button.EzVRq:hover,button.EzVRq:active{text-decoration:underline}.Qff0zd{display:none;position:absolute;list-style:none;background:#fff;border:1px solid #999}</style><button jsname="pzCKEc" class="EzVRq" aria-controls="dEjpnf" aria-haspopup="true" id="Mses6b" jsaction="mousedown:lgs1Pb;FwYIgd;keydown:QXPedb">Settings</button><ul jsname="xl07Ob" class="Qff0zd" aria-labelledby="Mses6b" id="dEjpnf" role="menu" jsaction="keydown:OEXC3c;focusout:Y48pVb"><li role="none"><a class="EzVRq" href="https://www.google.com/preferences?hl=en&amp;fg=1" role="menuitem" tabindex="-1">Search settings</a></li><li role="none"><a class="EzVRq" href="/advanced_search?hl=en&amp;fg=1" role="menuitem" tabindex="-1">Advanced search</a></li><li role="none"><a class="EzVRq" href="https://myactivity.google.com/privacyadvisor/search?utm_source=googlemenu&amp;fg=1" role="menuitem" tabindex="-1">Your data in Search</a></li><li role="none"><a class="EzVRq" href="https://myactivity.google.com/product/search?utm_source=google&amp;hl=en&amp;fg=1" role="menuitem" tabindex="-1">Search activity</a></li><li role="none"><a class="EzVRq" href="https://support.google.com/websearch/?p=ws_results_help&amp;hl=en&amp;fg=1" role="menuitem" tabindex="-1">Search help</a></li><li role="none"><button class="EzVRq" data-bucket="websearch" role="menuitem" tabindex="-1" jsaction="gf.sf">Send feedback</button></li></ul>
      </div>
    </div>
  </div>
</div>
```

Now, aside from the enormous amounts of data between each pair of HTML tags, did you notice anything weird about the 'Google HTML'? Maybe you're wondering what 'Classes' are, and what they do (*wink wink*)? Well, simply put, classes are used to group html elements that coders want to style in a similar manner. For example, all of the paragraphs on a website could share a class that makes their font-size be 20px, or they could also share a class that makes their color be green. 

For us, however, what the classes do doesn't actually matter. The only reason that they're important to us is that classes allow us to filter the data that we've scraped, in order to select only the data that's important to us.

Right now, visit the url of our economist article, and take a look at the class(es) assigned to the html element(s) that are storing our article!

Using Inspect Element, we are able to see that each paragraph of our article is stored in a 'p tag' with a class of 'article__body-text'

![Image of Economist Article](https://i.imgur.com/1J86Pff.png)

Zoomed In:

![Image of Economist Article](https://i.imgur.com/gTlkewf.png)

So how can we now use this information? Well, with Beautiful Soup we'll simply  select all *paragraph elements* with class of *'article__body-text'*. Then, to check if your code worked, print that selection out:

```python
paragraphs = soup.findAll('p',{'class':'article__body-text'})
print(paragraphs)
```

## Converting parsed HTML to plaintext form
At this point we are nearly finished! The last step is to convert our parsed HTML into straight text, so that it's easy to read, and comprehend. To do this we're going to create a variable called 'article', and then we're going to add the text content in every single paragraph to article.

```python
article = ''
for paragraph in paragraphs:
  article += paragraph.text
print(article)
```

## Last Thoughts
Hopefully by now you have a better understanding of web scraping, and will also have a greater appreciation for all of the crazy (stuff) you can do with it! Reach out if you have any questions, and stay tuned for future lessons!
