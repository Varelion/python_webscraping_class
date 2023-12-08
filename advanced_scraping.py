# Regular Expressions
import re
import sys
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Bristlecone_pine"
path = "/home/z/python_webscraping_class/saved_page1.html"
saved_html = False

def get_html(url, path):
    if (saved_html == True):
        print("Already have something in there")
    else:
        response = requests.get(url)
        with open(path, "w", encoding="utf-8") as f:
            f.write(response.text)

try:
    with open(path, "r", encoding='utf-8') as f:
        saved_html = f.read()
except FileNotFoundError:
    print("File not found!!!")
    get_html(url, path)
    print("File now has been saved, program will not shut down.")
    # Next line stops the program from executing.
    sys.exit()
except Exception as e:
    print("Error!:", e)



# this saves the file on the path read as utf-8 as f
# then it saves html variable as the contents being read from object f


# Here we are passing the saved html page to BeautifulSoup with the 'html.parser' parameter.
soup = BeautifulSoup(saved_html, 'html.parser')

section_headings = soup.find_all('span', attrs={'class': 'mw-headline'})

# for heading in section_headings:
#     print(heading.text)

# Here we are overwriting 'section_headings' with the 'span.string' value of every 'span' in 'section_headings'
section_headings = [span.string for span in section_headings]
# print(section_headings)

# Take note that the type of one of those strings is 'bs4.element.NavigableString'.
# This means that each of the strings in section_heading remembers its place in the original document.
# In other words, we can print its parent.
# print(type(section_headings[2]))
# print(section_headings[2].parent)
# If we had done '.ktext' instead of '.string' we would have severed this connection.

taxonomy = {}

info_box = soup.find('table', attrs={'class': 'infobox biota'})

def taxonomy_filter(tag):
    return ':' in tag.text and tag.name == 'td'

filtered = info_box.find_all(taxonomy_filter)
key = filtered
# print(filtered)
# print(filtered[2].next_sibling) # this gives us a blank, because next-sibling gives us junk data often.
# print(filtered[2].next_sibling.next_sibling) # it is for the reason above that we call .next_sibling on top of itself, to skip the junk that often comes with it.


for tag in filtered:
    sibling = tag.next_sibling.next_sibling
    # the .strip() till remove the junk spaces and the like from a .text.
    taxonomy[tag.text.strip().replace(':', "")] = sibling.text.strip()

# print(taxonomy)

# SECOND SOLUTION FOR TAXONOM ################################################################

# def taxonomy_filter_2(tag):
#     # Here we are going to be parsing for any single table row that has two children. HOWEVER, the reason that we aren't going to be finding it with tag.children ==2, is because, in the soup, there are artifacts between the two tables, and it turns out that, this causes the correct number that we are looking for to be tag.children == 4
#     return 'tr' and len(list(tag.children)) == 4

# keys_2 = info_box.find_all(taxonomy_filter_2)

# taxonomy_2 = {}
# # print('second method:', info_box.find_all(taxonomy_filter_2))
# for tr in keys_2:
#     target = tr.find_all('td')
#     if len(target) > 0:
#         taxonomy_2[(target[0].text.strip())] = target[1].text.strip()

# print(taxonomy_2)

################################################################################################

# Link Scraping  ################################################################

p_content = soup.find_all('p')
body_links = []
for p in p_content:
    body_links += p.find_all('a')

body_links = list(filter(lambda a: '#cite' not in a['href'], body_links))
# print(body_links)

links = {}

for a in body_links:
    links[a['title']] =  'https://wikipedia.org/' + a['href']

print(links)
##############################################################################################

# IMG Scraping ###############################################################################


##############################################################################################
