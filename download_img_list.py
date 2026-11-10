import requests

access_key = "T6EAsPVS3pX2ECTI5G4dd7aOJH3zwecCu4hMYUzHsyI"
query = "technology"

url = f"https://api.unsplash.com/search/photos?query={query}&per_page=5&language=en"

headers = {"Authorization": f"Client-ID {access_key}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for item in data["results"]:
        print(item["urls"]["raw"])
        with open(f"images/{item['id']}.jpg", "wb") as file:
            file.write(requests.get(item["urls"]["raw"]).content)


