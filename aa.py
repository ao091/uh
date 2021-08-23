import requests
import sys
import urllib.request as urllib2
import lxml

from mechanize import Browser
 
br=Browser()

#UA
br.set_handle_robots( False )
br.addheaders = [('User-agent', 'GoogleChrome')]

url = "login.live.com"

rep = br.open(url)

username = input("Username")
password = input("Password")

#Get input from login.txt

with open("login.txt", "r") as login:
    lines = login.readlines()

while True:
 for line in lines:
 	 if line.split(":")[0] == username and line.split(":")[1] == password:
            print("A hit smh. %s" % (username))

while false:
		print("False login")


else:
	sys.exit
