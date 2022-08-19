import requests, os
from bs4 import BeautifulSoup

class Getcomics:

    '''The init constructor tests the site if it is working or not.'''

    def __init__(self):

        self.temp= []
        self.links= []

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
                self.temp.append(title.find('a')["href"])
                print(f"{count}. {title.find('a').text}")
            self.link_substitute()

        except:
            print("site is not working")
            exit()
            os.system("exit")

    def link_substitute(self):

        "Sends multiple requests and makes it somewhat faster for now."

        try:
            with requests.Session() as session:
                for url in self.temp:
                    self.download_links(url,session)

        except:
            pass

    def download_links(self,url,session):

        "Scrapes download links for the comics and store it."

        with session.get(url) as response:
            result= response.content
            link= BeautifulSoup(result, "html.parser").find("a", class_= "aio-red")["href"]
            self.links.append(link)


