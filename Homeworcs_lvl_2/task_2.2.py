# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

#def quarter_of(month):
    #pass

#1:
#def quarter_of(month):
    #def quarter_of(month):
    #q = {1:(1,3), 2:(4,6), 3:(7,9), 4:(10,12)}
    #return [k for k,v in q.items() if v[0] <= month <= v[1]][0]
#2:
number = int(input('Введите номер месяца:'))
if number == 1 or number == 2 or number == 12:
    print('является частью первого квартала')
elif number == 3 or number == 4 or number == 5:
    print('является частью второго квартала')
elif number == 6 or number == 7 or number == 8:
    print('является частью третьего квартала')
elif number == 9 or number == 10 or number == 11:
    print('является частью четвертого квартала')
else:
    print('такого месяца не существует')

   