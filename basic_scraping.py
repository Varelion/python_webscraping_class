from bs4 import BeautifulSoup

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
soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.prettify())

# print(soup.title, '\n', soup.title.string )

# print(soup.p.b)

# print(soup.find(href="http://example.com/lacie"))
# print(soup.find(class_="story"))

# all_a_tags = soup.find_all('a')
# print(all_a_tags[2])
# print(all_a_tags[2].string)

# Below finds all child tags of the p variable
# p = soup.find(class_='story')
# print(p.contents)

# for child in p.children:
#     print(child)

body = soup.find("body")
# print(body.contents)
# print(len(body.contents))

# print(list(body.descendants))
# # print(soup.a)
# for p in soup.a.parents:
#     print(p.name)

# print(soup.a.parent)
# print(soup.a.nextSibling.nextSibling)
# print(list(soup.a.next_siblings), soup.a.next_siblings)
# for sibling in soup.a.next_siblings:
#     print(sibling)

import requests

response = requests.get("https://en.wikipedia.org/wiki/Bristlecone_pine")
soup = BeautifulSoup(response.text, "html.parser")
# Challenge #1 : Find the text within the top-level H1.
# print(soup.find("h1").string)
# print(soup.h1.text)
# Challenge #2: Find how many H2 total there are on the page.
# print(list(soup.find_all("h2")))
# count = 0
# for tag in list(soup.find_all('h2')):
# 	count += 1
# 	print(count)
# print(len(soup.find_all("h2")))
# Challenge #3: Extract href metadata from the first href tag on the page.
# elements_with_href = soup.select("[href]")
# print(elements_with_href[0])
