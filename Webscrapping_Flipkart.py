#from the search options of the site- like product name, its description- which is available on the website, and then the image url.

from bs4 import  BeautifulSoup as soup
from urllib.request import urlopen as uReq

#Url who's information you want to scrape
url = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_3_na_na_na&as-pos=0&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=eaf0a368-4390-4227-b06e-92dee26d197b&as-searchtext=iph"

uClient = uReq(url)
data_info = uClient.read()

uClient.close()
page_soup=soup(data_info,"html.parser") #parsing of information

containers = page_soup.findAll("div",{"class":"_4rR01T"})

#The product name of that item
container=containers[0]
print("\n"+"*Product name of the 1st item is: "+containers[0].text+"\n")

#print("Number of products on a particular site is: ")
#print(len(contaiers))

#To get the product details of that specific product
contain= page_soup.findAll("div",{"class":"fMghEO"})
description= contain[1].findAll("ul",{"class":"_1xgFaf"})
print("*Product Details: "+description[0].text+"\n")

#To print out the Image Description of that product
co= page_soup.findAll("div",{"class":"CXW8mj"})	
print("*Image description: "+ co[0].img["src"])

#..................................................END............................................#
