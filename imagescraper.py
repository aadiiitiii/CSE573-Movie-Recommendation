# Get Movie Poster from IMDB from the Movie Title
from bs4 import BeautifulSoup
import requests
import os
from PIL import Image
from io import BytesIO


class ImageScraper:
    def get_poster_url(self, title):
        url = f"http://www.imdb.com/find?s=tt&q={title}"
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")
        if result := soup.find("img", {"class": "ipc-image"}):
            href = result.get("srcset").split(" ")[-2]
            print(href)
            return href

        return "Movie not found"

    def download_poster(self, src, title, dir_name):
        if src:
            if not os.path.isdir(dir_name):
                os.mkdir(dir_name)
            response = requests.get(src)
            img = Image.open(BytesIO(response.content))
            img.save(f"./{dir_name}/{title}.jpg", "JPEG")
        else:
            print(f"No poster found for {title}")

