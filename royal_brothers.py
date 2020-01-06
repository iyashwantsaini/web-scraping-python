# royal_brothers data pune 15jan 1pm to 15jan 2pm

import csv
import requests
from bs4 import BeautifulSoup


def scrape_data(url):

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)
    row_data=[]
    header=["Bike","Rent"]

    card=soup.find_all(class_="tarif-desc-body col m5 l3 s10 offset-s1 z-depth-1")
    for i in card:
        row_data.append([i.select(".bike_name")[0].get_text(),i.select("#rental_amount")[0].get_text()])

    # print(row_data)

    with open('royal_brothers.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in row_data:
            writer.writerow(row)


if __name__=="__main__":
    url = "https://www.royalbrothers.com/search?utf8=%E2%9C%93&city_id=39&city_name=Agra&city=agra&current_service_type=bike-rentals&pickup=15+Jan%2C+2020&pickup_submit=15-01-2020&pickup_time=1%3A00+PM&dropoff=15+Jan%2C+2020&dropoff_submit=15-01-2020&dropoff_time=2%3A00+PM"
    scrape_data(url)