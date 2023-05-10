#!/usr/bin/python3

""" retrieves the top ten hot post topics on reddit"""

import requests


def top_ten(subreddit):
    """ function that gets the top ten hot topics"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": 'My agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        articles = response.json()['data']['children']
        for article in articles:
            print(article['data']['title'])
    else:
        print(None)
