from bs4 import BeautifulSoup
import requests

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# sets the html parsed through soup
soup = BeautifulSoup(html_doc)

# prints title tags, prints p tags.
print(soup.title)
print(soup.p)

# Send http get request
response = requests.get("https://www.wikipedia.org/")
print(response.text)
