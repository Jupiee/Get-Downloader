import os
from modules import Getcomics
from colorama import *

def main():
  
  test= Getcomics()

  print("""
   ___     _       ___                  _              _         
  / __|___| |_ ___|   \ _____ __ ___ _ | |___  __ _ __| |___ _ _ 
 | (_ / -_)  _|___| |) / _ \ V  V / ' \| / _ \/ _` / _` / -_) '_|
  \___\___|\__|   |___/\___/\_/\_/|_||_|_\___/\__,_\__,_\___|_|                                                             
  """)
  while True:
    query= str(input("\nWhat comics do you want to search for?  (type 'exit' to close program)\n"))
    if query == "exit":
      
      exit()
      os.system("exit")

    else:

      test.search(query)

if __name__ == "__main__":
    main()