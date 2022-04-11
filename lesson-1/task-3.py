
"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

"""
var1 = b'attribute'
var2 = b'класс'
var3 = b'функция'
var4 = b'type'

gen_var = (var1, var2, var3, var4)

for el in gen_var:
    try:
        print(bytes(el, 'ascii'))
    except SyntaxError:
        print(f'Слово " el " неввозможно переводить в байтовие строки ')


