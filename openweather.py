import requests
import gzip
import json

# Открываем gz архив
with gzip.open('city.list.json.gz', 'rb') as f:
    file = f.read()
# Считываем ID города, имя и страну, записываем их в переменные
file_str = file.decode('utf-8')
city_i = 0
city_id = []
city_name = []
country_name = []
for i in json.loads(file_str):
    city_id.append(i['id'])
    city_name.append(i['name'])
    country_name.append(i['country'])

# Поочерёдно выводим города из списка и погоду в них.
for i in city_id:
    print('Страна: ', country_name[city_i], ' ', end='')
    print('Город: ', city_name[city_i], ' ', end='')
    city_temp_cels = requests.get(f'http://api.openweathermap.org/data/2.5/weather?id={i}&units=metric&appid=6f5cb7bcc49645254f60ba8ea1f9e5b5&lang=ru')
    r = city_temp_cels.json()
    for w in r['weather']:
        print('За окном ', w['description'], ' ',  end='')
    city_temp = r['main']
    print('Температура: ',city_temp['temp'])
    city_i += 1
