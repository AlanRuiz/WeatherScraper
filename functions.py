import requests
import selectorlib
import os.path
import datetime
import time

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

now = datetime.datetime.now()
currentime = now.strftime(("%Y-%m-%d %H:%M:%S"))

def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['weather']
    return value


def store(extracted):
    if os.path.isfile("data.txt"):
        with open("data.txt","a") as file:
            file.write(f"{currentime},{extracted}\n")
    else:
        with open("data.txt","w") as file:
            file.write(f"date,temp\n{currentime},{extracted}\n")

def read():
    with open("data.txt","r") as file:
        return file.read()


if __name__ =="__main__":
    while True:
        now = datetime.datetime.now()
        currentime = now.strftime(("%Y-%m-%d %H:%M:%S"))
        scrapped = scrape(URL)
        extracted = extract(scrapped)
        store(extracted)
        print(read())
        time.sleep(5)

