# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random

choice = random.sample(my_favorite_songs, k=3)
total_time_1 = 0
for song, time in choice:
    total_time_1 += time
print('Три случайных песни из списка:', choice)
print('Три песни звучат', round(total_time_1, 2), 'минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
from random import sample
import datetime

data = list(my_favorite_songs_dict.items())
choise_lst = sample(data, 3)
print('Три случайных песни из словаря:', choise_lst)

total_time = 0
for song, time in choise_lst:
    total_time += time
print('Три песни звучат', round(total_time, 2), 'минут.')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

a = total_time
tseconds = int(a*60)
time_delta = datetime.timedelta(seconds = tseconds)
start = datetime.datetime(1900,1,1)
result = start + time_delta
time_str = result.strftime('%H:%M:%S')
print('Время звучания:', str(time_str)) 
