# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

##def minimum(arr):
    #pass

#def maximum(arr):
    #pass

from datetime import datetime
arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]

def insertion(data):
  for i in range(len(data)):
    j = i - 1
    key = data[i]
    while data[j] > key and j >= 0:
      data[j + 1] = data[j]
      j -= 1
    data[j + 1] = key
  return data

def bubble (data):
  n = len(data)
  for i in range (n-1):
    for j in range (n-i-1):
      if data[j] > data[j+1]:
        data[j], data[j+1] = data[j+1], data[j]
  return data

def vibor(data):
  n = len(data)
  i = 0
  while i < n-1:
    m = i
    j = i + 1
    while j < n:
      if data[j]<data[m]:
        m = j
      j += 1
    data[i], data[m] = data[m], data[i]
    i += 1
  return data

def default(data):
  for data in arr:
    data = sorted(data)
    return data

def minimum(arr):
  print ("МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ")
  print ("Метод сортировки встроенный")
  start_time = datetime.now()
  for data in arr:
   data = sorted(data)
   print ("Минимальное значение из массива:", data, min(data))
  end_time = datetime.now()
  print ('Продолжительность: {}'.format(end_time - start_time))
  print ("Метод сортировки вставкой")
  start_time = datetime.now()
  for data in arr:
    print ("Минимальное значение из массива:", data, insertion(data)[0])
  end_time = datetime.now()
  print ('Продолжительность: {}'.format(end_time - start_time))
  print ("Метод сортировки пузырьком")
  start_time = datetime.now()
  for data in arr:
    print ("Минимальное значение из массива:", data, bubble(data)[0])
  end_time = datetime.now()
  print ('Продолжительность: {}'.format(end_time - start_time))
  print ("Метод сортировки выбором")
  start_time = datetime.now()
  for data in arr:
    print ("Минимальное значение из массива:", data, vibor(data)[0])
  end_time = datetime.now()
  print ('Продолжительность: {}'.format(end_time - start_time))

def maximum(arr):
  print ("МАКСИМАЛЬНЫЕ ЗНАЧЕНИЯ")
  print ("Метод сортировки встроенный")
  start_time = datetime.now()
  for data in arr:
   data = sorted(data)
   print ("Максимальное значение из массива:", data, max(data))
  end_time = datetime.now()
  print ('Продолжительность: {}'.format(end_time - start_time))
  print ("Метод сортировки вставкой")
  start_time = datetime.now()
  for data in arr:
    print ("Максимальное значение из массива:", data, insertion(data)[len(data)-1])
  end_time = datetime.now()
  print ('Продолжительность: {}'.format(end_time - start_time))
  print ("Метод сортировки пузырьком")
  start_time = datetime.now()
  for data in arr:
    print ("Максимальное значение из массива:", data, bubble(data)[len(data)-1])
  end_time = datetime.now()
  print ('Продолжительность: {}'.format(end_time - start_time))
  print ("Метод сортировки выбором")
  start_time = datetime.now()
  for data in arr:
    print ("Максимальное значение из массива:", data, vibor(data)[len(data)-1])
  end_time = datetime.now()
  print ('Продолжительность: {}'.format(end_time - start_time))

def main():
 print (minimum(arr))
 print (maximum(arr))

print (main())