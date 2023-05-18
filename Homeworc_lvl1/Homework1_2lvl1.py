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
time_songs = 0
time_songs += my_favorite_songs[3][1]
time_songs += my_favorite_songs[5][1]
time_songs += my_favorite_songs[8][1]

print('Три песни звучат', round(time_songs, 2), 'минут')

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
time_songs = 0
time_songs += my_favorite_songs_dict['Waste a Moment']
time_songs += my_favorite_songs_dict['A Sorta Fairytale']
time_songs += my_favorite_songs_dict['Beautiful Day']

print('Вывод: Три песни звучат', round(time_songs, 2), 'минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

import random
print ('Случайные песни:', random.choice(my_favorite_songs) 
       + random.choice(my_favorite_songs) 
       + random.choice(my_favorite_songs))

# Дополнительно 
# Пункт D. 
# Переведите минуты и секунды в формат времени. Используйте модуль datetime
