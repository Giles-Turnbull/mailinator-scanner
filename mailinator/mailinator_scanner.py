import random
import requests
from bs4 import BeautifulSoup
import time
#from selenium import webdriver
from requests_html import HTMLSession

adds = ["", "1", "12", "123", "12345", "123456", "1234567", "123345678", "123456789", "1234567890", "0987654321", "987654321", "87654321", "7654321", "654321", "54321", "4321", "321", "21", "69", "21", "420"]
search = ["Tesco", "Amazon", "Google", "Steam", "login", "signup", "restore", "reset", "password", "account", "bank", "money", "transaction", "trade"]
words, emails, found, count, trigger, comp = [], [], False, -1, False, ""

file = open("example.txt", "r")
for line in file:
#-----------------------------------------------------------------
    word = line[:-1]
    words.append(word)
    #for ex in adds: words.append(word + ex)                                     # creates the search list and adds the extra numbers onto the web addresses
    #for num in range(100): words.append(word + num)
    #for num in range(40): words.append(word + str(num + 1970))
file.close()
#==========================================================================================================================


for address in words:
    start_time = time.time()
    request_name = "https://www.mailinator.com/v3/index.jsp?zone=public&query=" + str(address) + "#/#inboxpane"    # shows inbox name and finds url
    print("The inbox being tested is " + str(address) + "@mailinator.com")
    globals()[address] = []
    emails.append(address)
#-----------------------------------------------------------------
    session = HTMLSession()
    resp = session.get(request_name)
    resp.html.render()                                                       # renders js for source code of the page for table of recieved emails, then puts it into string
    ret = str(BeautifulSoup(resp.html.html, "lxml"))      
#-----------------------------------------------------------------
    for letter in ret:
        count += 1
        if letter == "n" and found == False:
            try:
                if ret[count + 1] == "g" and ret[count + 2] == "-" and ret[count + 3] == "b" and ret[count + 4] == "i" and ret[count + 5] == "n" and ret[count + 6] == "d" and ret[count + 7] == "i" and ret[count + 8] == "n" and ret[count + 9] == "g":
                    found = True                            
            except IndexError: expen = ""
        if found == True:
            if letter == ">": trigger = True                                 # looks for "ng-binding" which is the class name for the table of the recieved emails
            if trigger == True:
                if letter == '<':
                    eval(address).append(comp)
                    found, comp, trigger = False, "", False
                else: comp = comp + letter
#-----------------------------------------------------------------
    for x in eval(address):
        for keyword in search:
            if keyword in x: print("there was", keyword)                        # on the spot search timer
    print("--- %s seconds ---" % (time.time()-start_time))
        

#==========================================================================================================================
print("\n\n\n\n\n\n\n\n\n\n\n=============================================\nfinal search conclusions\n")
for i in emails:
    for x in eval(i):                                                       #final search
        for keyword in search:
            if keyword in x: print("there was", keyword, "found in", i)
print("=============================================")
#-----------------------------------------------------------------


## maybe find a way to render quicker
## maybe make it remover word if inbox is empty
## maybe add a noise aleart next to timer
