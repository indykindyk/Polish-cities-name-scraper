import requests
from bs4 import BeautifulSoup

class PolishCities():
    
    def __init__(self):
        self.url = "https://pl.wikipedia.org/wiki/Miasta_w_Polsce"
        self.pageContent = ""
        self.cities = []

    def downloadPage(self):
        self.pageContent = requests.get(self.url).text

    def getCitites(self):
        self.downloadPage()
        soup = BeautifulSoup(self.pageContent, 'html.parser')

        text = soup.find(attrs={"id": "Indeks"})
        citiesLists = text.find_all_next('ul')
        for i in range(0, 26):
            for city in citiesLists[i].find_all('li'):
                cityTag = city.find('a')
                city = cityTag.get_text()
                self.cities.append(city)

    def save(self, path):
        # Open a file in write mode
        with open(path+'citites.txt', 'w') as file:
            # Iterate over the elements of the list
            for item in self.cities:
                # Write each element to a new line in the file
                file.write(item + '\n')

