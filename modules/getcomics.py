from distutils.log import info
import requests, os, re
from bs4 import BeautifulSoup

class Getcomics:

    '''The init constructor tests the site if it is working or not.'''

    def __init__(self):

        self.temp= []
        self.links= []
        self.info= {}
        self.currentpage= 0
        self.totalpages= 0
        self.size_pattern= "Size : \d*\.\d+ |Size : \d+ MB|GB"

        try:
            req= requests.get("https://getcomics.info")

        except:
            print("the site is not working")
            exit()
            os.system("exit")

    def search(self,query) -> None:

        '''Searches for a query/comic in the website and prints out the first page.'''

        try:

            if " " in query:
                query= query.replace(" ","+")
            else:
                pass
            
            soupobject= BeautifulSoup(self.changepage(query,1), "html.parser")
            titles= soupobject.find_all("h1", class_= "post-title")
            try:
                self.totalpages= int(BeautifulSoup(self.changepage(query,1), "html.parser").find_all("a", class_= "page-numbers")[-1].text)
            except:
                self.totalpages= self.currentpage
            
            sizes= self.get_size(soupobject)
            filtered_titles= self.filter_titles(titles)

            self.update_info(filtered_titles,sizes)
            self.temp= [title.find('a')["href"] for title in titles]

            for count,i in enumerate(self.info,1):
                print(f"\n{count}.  {i}     {self.info.get(i)}")
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
                        self.temp= []
                        self.links= []
                        sizes= []
                        filtered_titles= []
                        self.info= {}

                        soupobject= BeautifulSoup(self.changepage(query,int(pagenumber)), "html.parser")
                        titles= soupobject.find_all("h1", class_= "post-title")

                        sizes= self.get_size(soupobject)
                        filtered_titles= self.filter_titles(titles)

                        self.update_info(filtered_titles,sizes)
                        self.temp= [title.find('a')["href"] for title in titles]

                        for count,i in enumerate(self.info,1):
                            print(f"\n{count}.  {i}     {self.info.get(i)}")
                        self.link_substitute()
                except:
                    print(f"there is no page number '{pagenumber}' ")
                    continue
        except:
            print("site is not working a")
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
            print("site is not working b")

    def get_size(self,soupobject):

        sizes_list= []

        sizes= soupobject.find_all("p",class_= "post-excerpt")
        for size in sizes:
            x= re.findall(self.size_pattern,size.text)
            sizes_list.append(x)
        
        if len(sizes_list) == 13:
            sizes_list.pop()
            return sum(sizes_list,[])
        else:
            return sum(sizes_list,[])
        
    def filter_titles(self,titles_list):

        titles= []

        for title in titles_list:
            titles.append(title.find('a').text)

        return(titles)

    def update_info(self,titles,sizes):

        for i in range(12):
            self.info.update({titles[i]:sizes[i]})
        



