# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = "https://www.nasdaq.com/aspx/infoquotes.aspx?symbol=SPX&selected=SPX"

# query the website and return the HTML to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, "html.parser")

# Take out the <div> of name and get its value
name_box = soup.find("strong")
name = name_box.text
print name

# get the index price
price_box = soup.find("label", id="SPX_LastSale1")
price = price_box.text.strip()
print price
