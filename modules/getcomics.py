import requests
from bs4 import BeautifulSoup

class Getcomics:

    def __init__(self):

        try:
            req= requests.get("https://getcomics.info")

        except:
            print("site is not working")

    def search(self,query) -> str:

        try:
            req= requests.get(f"https://getcomics.info/?s={query}").content
            titles= BeautifulSoup(req, "html.parser").find_all("h1", class_= "post-title")
            
            for count,title in enumerate(titles,1):
                print(f"{count}. {title.find('a').text}")

        except:
            print("site is not working")


