# Get Movie Poster from IMDB from the Movie Title
from bs4 import BeautifulSoup
import requests
import os
from PIL import Image
from io import BytesIO


class ImageScraper:

    def download_poster(self, title):
        print(title)
        url = f"http://www.imdb.com/find?s=tt&q={title}"
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")
        if result := soup.find("img", {"class": "ipc-image"}):
            href = result.get("srcset").split(" ")[-2]
            if href:
                print(href)
                src = href
                response = requests.get(src)
                img = Image.open(BytesIO(response.content))
                input = title
                rep = "%20"
                for i in range(len(input)):
                    if (input[i] == ' '):
                        input = input.replace(input[i], rep)
                print(input)
                img.save(f"posters/{input}.jpg", "JPEG")
            else:
                print(f"No poster found for {title}")
