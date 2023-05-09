#!/usr/bin/python3

""" retrieve the top ten hot topic on reddit """

import requests


def top_ten(subreddit):
    """ get the top ten hot topics"""

    url = "reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": 'My agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            print(post['data']['title'])
    else:
        return None
