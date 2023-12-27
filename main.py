#!/usr/bin/env python3

import re

def main():
    doesnt_follow_back = []

    followers_html = open("followers_1.html", "r")
    following_html = open("following.html", "r")

    followers = populate_usernames(followers_html)
    following = populate_usernames(following_html)
    doesnt_follow_back = list(set(following) - set(followers))
    doesnt_follow_back.sort()

    output("users_that_dont_follow_you_back.txt", doesnt_follow_back)

def populate_usernames(html_file):
    """
    function that takes in an html file and returns a list of usernames
    """
    try:
        usernames = []
        pattobj = re.compile(r'instagram.com/([^"]+)')
        
        lines = html_file.read().rstrip()
        usernames = pattobj.findall(lines)
        return usernames
        
    except FileNotFoundError:
        print("{} couldn't be found.".format(html_file))
        return []

def output(result_file, doesnt_follow_back):
    """
    function that takes in a list of usernames and outputs them to a file
    """
    try:
        file_handle = open(result_file, "w")
        file_handle.write("Users that don't follow you back:\n")
        for username in doesnt_follow_back:
            file_handle.write(username + "\n")
        file_handle.close()
    except FileNotFoundError:
        print("{} couldn't be found.".format(result_file))

if __name__ == "__main__":
    main()