import requests

url = "https://plus.unsplash.com/premium_photo-1661963063875-7f131e02bf75?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D"

response = requests.get(url)

if response.status_code == 200:
    with open("example.jpg", "wb") as file:
        file.write(response.content)
    print(f"Image downloads successfully")
else:
    print(f"Error downloading image, status code: {response.status_code}")


