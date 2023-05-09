#!/usr/bin/python

    """retrieve top ten hot topic on reddit """
import requests

def top_ten(subreddit):
     """get top ten hot topic"""

    url = "reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers ={"User-Agent": 'My agent'}
    response = request.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        post = response.json()

        for post in posts('data')['children']:
            print(post['data']['title'])
    else:
        return 0
