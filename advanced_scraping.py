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

for heading in section_headings:
    print(heading.text)
