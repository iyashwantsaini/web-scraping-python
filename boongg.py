
# boongg data pune 4jan 1pm to 4jan 2pm

import csv
import requests
from bs4 import BeautifulSoup


def scrape_data(url):

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')

    row_data=[]
    header=["Bike","Rent"]

    divs=soup.find_all(class_="bike-item")
    for i in divs:
        row_data.append([i.select(".searchBikeName")[0].get_text(),i.select(".actualPrice")[0].select("span")[0].get_text()])
    # print(row_data)

    with open('boongg.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in row_data:
            writer.writerow(row)

if __name__=="__main__":
    url = "https://www.boongg.com/rent/search/pune/any/any/any?start_date=1578123000000&end_date=1578126600000&timezone=Asia/Calcutta"
    scrape_data(url)










    

#  'https://www.urbandrive.co.in/Search/ChangeCity/46?starts=16/01/2020%2013:00?ends=16/01/2020%2014:00'