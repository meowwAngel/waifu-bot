import requests
import json
import random

url = 'https://api.waifu.pics/many/sfw/waifu'
data = {
        "headers": {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.8",
        "content-type": "application/json;charset=UTF-8",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Brave\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1"
        },
        "referrer": "https://waifu.pics/",
        "body": "{\"exclude\":[]}",
        "method": "POST",
        "mode": "cors",
        "credentials": "omit"
        }
response = requests.post(url, json=data)
response_data = response.json()

data = json.loads(response)

urls = data["files"]
randomimage = random.choice(urls)
print(randomimage)