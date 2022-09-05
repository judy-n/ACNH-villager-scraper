import requests
from bs4 import BeautifulSoup

url = 'https://www.animalcrossingportal.com' \
      '/tier-lists/new-horizons/all-villagers'

data = requests.get(url)

my_data = []


def scrape():
    soup = BeautifulSoup(data.content, 'html.parser')
    results = soup.select(
        "#__layout > div > div:nth-child(2) > div:nth-child(2) > "
        "div:nth-child(1) > section > div > div > div.c-spoiler-body.fadeIn > "
        "div > div > div")
    i = 0

    for res in results:
        name = res.select("div > p")[0].text
        personality = res.select("div > span.c-villager-personality")[0].text
        species = res.select("div > span.c-villager-species")[0].text
        my_data.append({"name": name, "rank": i, "personality": personality,
                        "species": species})
        i += 1
    return my_data

