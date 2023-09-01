from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv
import pandas as pd


url = 'https://www.amazon.com/Feelin-Good-Tees-Sarcasm-Sarcastic/dp/B00VJ8O3SM/ref=sr_1_1_sspa?crid=2PEJS335HRMZT&keywords=funny+data+analyst+tshirt&qid=1692611988&sprefix=data%2Banalyst%2Btshir%2Caps%2C452&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text().strip()

price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text().strip()[1:6]

today = datetime.date.today()

header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f: 
    writer = csv.writer(f)
    writer.writerow(data)


def check_price():
    url = 'https://www.amazon.com/Feelin-Good-Tees-Sarcasm-Sarcastic/dp/B00VJ8O3SM/ref=sr_1_1_sspa?crid=2PEJS335HRMZT&keywords=funny+data+analyst+tshirt&qid=1692611988&sprefix=data%2Banalyst%2Btshir%2Caps%2C452&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id='productTitle').get_text().strip()
    price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text().strip()[1:6]
    today = datetime.date.today()
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f: 
        writer = csv.writer(f)
        writer.writerow(data)
    if(float(price) < 14):
        send_email()

def send_email():
    server = server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login('emabrijacak@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Ema, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Feelin-Good-Tees-Sarcasm-Sarcastic/dp/B00VJ8O3SM/ref=sr_1_1_sspa?crid=2PEJS335HRMZT&keywords=funny+data+analyst+tshirt&qid=1692611988&sprefix=data%2Banalyst%2Btshir%2Caps%2C452&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'emabrijacak@gmail.com',
        msg 
    )

while True:
    check_price()
    time.sleep(2) 



