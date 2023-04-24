# Задача 1
# Проверьте, содержит ли строка одинаковое количество "x" и "o".
# Строка должна быть нечувствительна к регистру. 
# Строка может содержать любые символы.
 
# Примеры ввода/вывода:
#   XO("ooxx") => true
#   XO("xooxx") => false
#   XO("ooxXm") => true
#   XO("zpzpzpp") => true # когда нет "x" и "o", должно быть возвращено значение true
#   XO("zzoo") => false
 
def check_xo(string):
    counter_x = 0
    counter_o = 0
    for i in string.lower():
        if i == 'o':
            counter_o += 1
        elif i == 'x':
            counter_x += 1
            
    return counter_x == counter_o
 
for i in ["ooxx", "xooxx", "ooxXm", "zpzpzpp", "zzoo"]:
    print(check_xo(i))

'''Скажи ка дядя, ведь не даром'''

    def trapezoid_s(a, b, h):
        ''''''
    return h * (a+b) / 2
 
S = trapezoid_s(8, 4, 10)
print(S)
print(help(trapezoid_s))

# Параметры
def trapezoid_s(a: int, *, b: int, h=1) -> float:
    '''Функция для расчета площади трапеции. 
    a - нижнее основание, 
    b - верхнее основание, 
    h - высота.'''
 
    return h * (a+b) / 2
 
# S = trapezoid_s(8, 4, 10)
S = trapezoid_s(8, h=10, b=4)
S = trapezoid_s(8, b=4)
print(S)
 
# Как работает функция print?
# print(1, 2, 3, 4,'vcdaf', '4215', [1, 2], sep='\n', end=' ')
 
def print_them_all(*args, **kwargs):
    print('print_them_all')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
 
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)
 
print_them_all(1, 2, 3, 4, ',dcw', 'a', a=124, b=4214)