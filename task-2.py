"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""
w1 = 'class'
w2 = 'function'
w3 = 'method'
task2 = [w1, w2, w3]

for line in task2:
    print(line)
    print(type(line))
    print(len(line))
