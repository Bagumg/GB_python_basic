import requests
import gzip
import json
import datetime

with gzip.open('city.list.json.gz', 'rb') as f:
    file = f.read()

class Get_weather():
    def __init__(self):
        self.city_id = []
        self.city_name = []
        self.country_name = []
        self.city_data = dict()
        self.now = datetime.datetime.now()
        self.file_str = file.decode('utf-8')

    def get_weather(self, user_city):
        if user_city in self.city_data.keys():
            city_temp_cels = requests.get(f'http://api.openweathermap.org/data/2.5/weather?id={self.city_data[user_city]}&units=metric&appid=6f5cb7bcc49645254f60ba8ea1f9e5b5&lang=ru')
            r = city_temp_cels.json()
            print(f'Город {user_city.capitalize()}')
            print(f'{self.now.hour}:{self.now.minute}')
            print(r['weather'][0]['description'])
            print('Температура', r['main']['temp'], ' C', "\u00b0")
        else:
            print('Извините, такого города нет в списке')

    def city_data_gen(self):
        for i in json.loads(self.file_str):
            self.city_id.append(i['id'])
            self.city_name.append(i['name'])
            self.country_name.append(i['country'])
            self.city_data.update({i['name'].lower(): i['id']})



cls = Get_weather()
cls.city_data_gen()
user_city = ''
while user_city != 'q' or user_city != 'Q':
    user_city = input('Укажите город для получения прогноза: ').lower()
    cls.get_weather(user_city)