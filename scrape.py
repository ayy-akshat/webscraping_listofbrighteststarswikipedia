from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import csv
import time

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("(insert chromedriver filepath)")
browser.get(url)
print("getting " + url + " please wait")
time.sleep(5)
print("done getting site")
header = ['magnitude', 'name', 'bayer', 'distance', 'spectral_class', 'mass', 'radius', 'luminosity']
planet_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    tbody = soup.find("tbody")
    for ul in tbody.find_all("tr"):
        li_tags = ul.find_all("td")
        template = []
        for index, e in enumerate(li_tags):
            try:
                template.append(e.find_all("a")[0].contents[-1].replace("\n", ""))
            except:
                try:
                    template.append(e.contents[-1].replace("\n", ""))
                except:
                    template.append("n/a")

        print(template)
        planet_data.append(template)
    
    print("done...")
    print("fully done")
    with open('stars.csv', "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)
        csv_writer.writerows(planet_data)
        print("written file!")
    
                


scrape()