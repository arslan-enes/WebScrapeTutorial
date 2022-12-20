from bs4 import BeautifulSoup
import requests

url = "https://www.haberturk.com/ekonomi"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
images = soup.find("div", {"class": "swiper-wrapper"}).find_all("img")

for image in images:
    print(image["src"])
    print(image["alt"])
    print("*" * 50)



