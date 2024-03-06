#!/usr/bin/python3
""" Accessing the Reddit API to get number of subscribers """
import requests
import sys

def top_ten(subreddit):
    """
    Function that accesses the REDDIT API
    If not valid return 0

    Args:
        subreddit (str) : The name of subreddit

    Return:
        str: The title of first 10 posts, or 0
    """
    url =  "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    req = requests.get(url, headers=headers, params={"limit": 10})

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            info = get_data.get("data").get('title')
            print(info)
    else:
        return(None)
