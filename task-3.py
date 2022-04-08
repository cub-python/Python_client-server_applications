
"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""
# w1 = b'attribute'
# w2 = b'класс'
# w3 = b'функция'
# w4 = b'type'
var_task3 = (b'attribute', b'класс', b'функция', b'type')

print(var_task3)


#   File "/home/kja/DRF/DRF_course/Django_REST_ramework/Python_Cl_Serv/task-3.py", line 14
#     w2 = b'класс'
#          ^
# SyntaxError: bytes can only contain ASCII literal characters.
