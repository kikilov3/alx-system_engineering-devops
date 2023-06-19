import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return 0
