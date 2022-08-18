import requests, os
from bs4 import BeautifulSoup

class Getcomics:

    '''The init constructor tests the site if it is working or not.'''

    def __init__(self):

        self.test= []

        try:
            req= requests.get("https://getcomics.info")

        except:
            print("the site is not working")
            exit()
            os.system("exit")

    def search(self,query) -> str:

        '''Searches for a query/comic in the website and prints out the first page.'''

        try:
            req= requests.get(f"https://getcomics.info/?s={query}").content
            titles= BeautifulSoup(req, "html.parser").find_all("h1", class_= "post-title")
            for count,title in enumerate(titles,1):
                print(f"{count}. {title.find('a').text}")
                self.linkcapture(title)

        except:
            print("site is not working")
            exit()
            os.system("exit")

    def linkcapture(self,title):

        "Scrapes download links for the comics and store it."

        try:
            req= requests.get(title.find('a')["href"]).content
            link= BeautifulSoup(req, "html.parser").find("a", class_= "aio-red")["href"]

            self.test.append(link)

        except:
            pass
