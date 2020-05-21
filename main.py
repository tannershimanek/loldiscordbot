import requests
from bs4 import BeautifulSoup


class Scraper:
    """https://www.youtube.com/watch?v=1UMHhJEaVTQ"""
    """https://github.com/aj-4/newsbot/blob/master/main.py"""

    def __init__(self, champion):
        self.champion = champion
        self.markup = requests.get(f'https://www.lolskill.net/champion/{self.champion}').text

    def parse(self):
        soup = BeautifulSoup(self.markup, 'html.parser') # parse the markup html
        abilities = soup.findAll("div", {"class": "text"}) # look for div with class text

        return abilities






def main():
    # champion = input(str('Whose ablities do you want to learn? '))
    champion = 'riven'
    s = Scraper(champion)
    print(s.parse())


if __name__ == "__main__":
    main()