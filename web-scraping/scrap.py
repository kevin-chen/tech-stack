from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+cards&ignorear=0&N=-1&isNodeId=1"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
print(page_soup.h1)
print(page_soup.p)
page_soup.body.span
containers = page_soup.findAll("div", {"class":"item-container"})
print(len(containers))
print(containers[0])

# One Test
container = containers[0]
print(container.a) # Gets the item info heading
print(container.div) # Gets the heading of one item
print(container.div.div.a) # Gets the Brand name (image)
print(container.a.img["title"]) # gets the title name; index like dictionary; container.a.img["title"][:container.a.img["title"].find(" ")]

# Loop
for container in containers:
    brand = container.a.img["title"][:container.a.img["title"].find(" ")]
    title_container = container.findAll("a", {"class":"item-title"})
