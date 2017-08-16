#!/usr/bin/python3
import utils
from constants import alphabet

lastname_files = [
    #"../wordlists/SecLists/Usernames/Names/top_1000_usa_familynames_english.txt",
]

firstname_files = [
    #"../wordlists/SecLists/Usernames/top_shortlist.txt",
    #"../wordlists/SecLists/Usernames/Names/top_1000_usa_malenames_english.txt",
    #"../wordlists/SecLists/Usernames/Names/top_1000_usa_femalenames_english.txt",
]

password_files = [
    #"./manual-guesses.txt",
    #"../wordlists/SecLists/Usernames/Names/top_1000_usa_femalenames_english.txt",
    #"../wordlists/SecLists/Usernames/Names/top_1000_usa_malenames_english.txt",
    #"./v1com.txt",
    #"./manifesto.txt",
    #"./twelveprinciples.txt",
    #"./localinst.txt",
    #"../wordlists/SecLists/Passwords/hak5.txt",
    #"../wordlists/SecLists/Passwords/top_shortlist.txt",
    #"../wordlists/SecLists/Passwords/10_million_password_list_top_10000.txt",
    #"../wordlists/SecLists/Passwords/rockyou-5.txt",
    #"../wordlists/SecLists/Passwords/cain.txt",
    "../wordlists/SecLists/Passwords/best1050.txt"
]

raw_last_names = set(utils.read_files_to_list(lastname_files))
raw_firstnames = set(utils.read_files_to_list(firstname_files))
passwords = set(utils.read_files_to_list(password_files))
v1_usernames = []

def construct_uname(prepended_char, raw_name, is_uppercase):
    raw_username = prepended_char + raw_name
    return raw_username.upper() if is_uppercase else raw_username.lower()

def construct_unames(member_api_url):
    global v1_usernames
    v1_usernames = utils.get_active_usernames(member_api_url)
    #passwords.update(v1_usernames) #check for unchanged default passwords
    val = v1_usernames
    if not len(raw_last_names) == 0: #build first letter of first name, whole last name set
        for char in alphabet:
            for name in raw_last_names:
               val.append(construct_uname(char, name, False))
    for name in raw_firstnames:
        val.append(name)
    return val

def construct_passwords():
    return passwords