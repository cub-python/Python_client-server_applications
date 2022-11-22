import chardet
from nacl import encoding

"""
Задание 6.
Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.
При сдаче задания в папке должен лежать текстовый файл!

"""
T_F = open('../test_file.txt', 'w', encoding='windows-1251')
T_F.write('«сетевое программирование», «сокет», «декоратор»')
T_F.close()
print(type(T_F))

with open('../test_file.txt', 'rb') as t_f:
    context = t_f.read()
    result = chardet.detect(context)
    encoding = result['encoding']
    text_ = context.decode(encoding)
    with open('../test_file.txt', 'w', encoding='utf-8') as t_f:
        t_f.write(text_)

with open('../test_file.txt', 'r', encoding='utf-8') as t_f:
    text_ = t_f.read()

print(text_)


