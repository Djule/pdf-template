import requests
import send_email

topic = "tesla"
url = ("https://newsapi.org/v2/"
       f"everything?q={topic}&from=2026-10-10&sortBy=publishedAt&apiKey=d1522b8e0272473a996bf8634db44445&language=en")

request = requests.get(url)
content = request.json()

body = "Subject: Today News\n\n"
for article in content["articles"][:5]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" * 2


body =  body.encode("utf-8")
send_email.send_email(body)
print(body)

