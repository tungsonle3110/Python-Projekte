import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get('https://api.covidtracking.com/v1/us/current.json')
    data = r.json()
    text = f'date: {data[0]["dateChecked"]} \nPositive: {data[0]["positive"]} \nNegative: {data[0]["negative"]} \nDeaths: {data[0]["death"]}}'

    while True:
        t=ToastNotifier()
        t.show_toast("Covid 19 Update", text, duration=20)
        time.sleep(10)

update()