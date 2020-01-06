# wheelstreet data pune 15jan 1pm to 15jan 2pm

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import  QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage as QWebPage

import csv
import requests
from bs4 import BeautifulSoup

class Client(QWebPage):
    
    def __init__(self , url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.load(QUrl(url))
        self.app.exec_()
    
    # def on_page_load(self):
    #     self.app.quit()

    def on_page_load(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

url="https://www.wheelstreet.com/search/1578075850139662"

def scrape_data(url):

    client_response = Client(url)
    source = client_response

    soup = BeautifulSoup(source.html, 'html.parser')
    row_data = []
    header = ["Bike","Rent"]

    data = soup.find_all(class_="searchPage__bikeCardInfoPricing")
    
    # selecting_required_data
    # card=soup.find_all(class_="tarif-desc-body col m5 l3 s10 offset-s1 z-depth-1")
    # for i in card:
    #     row_data.append([i.select(".bike_name")[0].get_text(),i.select("#rental_amount")[0].get_text()])

    # writing data to CSV file

    # with open('wheel_street.csv', 'w') as csv_file:
    #     writer = csv.writer(csv_file)
    #     writer.writerow(header)
    #     for row in row_data:
    #         writer.writerow(row)

if __name__=="__main__":
    url = 'https://www.wheelstreet.com/search/1578076174680676'
    scrape_data(url)