import requests, os
from bs4 import BeautifulSoup

class Getcomics:

    '''The init constructor tests the site if it is working or not.'''

    def __init__(self):

        self.temp= []
        self.links= []
        self.currentpage= 0
        self.totalpages= 0

        try:
            req= requests.get("https://getcomics.info")

        except:
            print("the site is not working")
            exit()
            os.system("exit")

    def search(self,query) -> None:

        '''Searches for a query/comic in the website and prints out the first page.'''

        try:
            titles= BeautifulSoup(self.changepage(query,1), "html.parser").find_all("h1", class_= "post-title")
            self.totalpages= int(BeautifulSoup(self.changepage(query,1), "html.parser").find_all("a", class_= "page-numbers")[-1].text)
            for count,title in enumerate(titles,1):
                self.temp.append(title.find('a')["href"])
                print(f"\n{count}. {title.find('a').text}")
            self.link_substitute()

            loop= True

            while loop:
                pagenumber= input(f"\nWhich page you wanna browse? page {self.currentpage}/{self.totalpages} (type 'back' to return to searching)\n")
                try:
                    if pagenumber == "back":
                        loop= False
                    elif int(pagenumber) > self.totalpages:
                        print(f"there is no page number {pagenumber}")
                        continue
                    else:
                        self.links= []
                        titles= BeautifulSoup(self.changepage(query,int(pagenumber)), "html.parser").find_all("h1", class_= "post-title")
                        for count,title in enumerate(titles,1):
                            self.temp.append(title.find('a')["href"])
                            print(f"\n{count}. {title.find('a').text}")
                        self.link_substitute()
                except:
                    print(f"there is no page number '{pagenumber}' ")
                    continue
        except:
            print("site is not working")
            exit()
            os.system("exit")

    def link_substitute(self) -> None:

        "Sends multiple requests and makes it somewhat faster for now."
        try:
            with requests.Session() as session:
                for url in self.temp:
                    self.download_links(url,session)
        except:
            pass

    def download_links(self,url,session) -> None:

        "Scrapes download links for the comics and store it."
        
        with session.get(url) as response:
            result= response.content
            link= BeautifulSoup(result, "html.parser").find("a", class_= "aio-red")["href"]
            self.links.append(link)
        
    def changepage(self,query,pagenumber) -> bytes:

        "Changes the page number and updates the current page."

        try:
            req= requests.get(f"https://getcomics.info/page/{pagenumber}/?s={query}").content
            self.currentpage= pagenumber
            return req
        except:
            print("site is not working")
