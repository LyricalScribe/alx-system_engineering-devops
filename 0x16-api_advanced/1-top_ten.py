#!/usr/bin/python3

""" retrieves the top ten hot topic on reddit"""

import requests


def top_ten(subreddit):
    """ gets the top ten hot topics"""

    url = "reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": 'My agent'}

    posts = requests.get(url, headers=headers, allow_redirects=False)

    if post.status_code == 200:
        for post in posts.json()['data']['children']:
            print(post['data']['title'])
    else:
        return (None)
