import subprocess
import chardet
"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""

ARGS1 = ['ping', 'yandex.ru','-c', '2']
YA_PING = subprocess.Popen(ARGS1, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    resut = chardet.detect(line)
    line = line.decode(resut['encoding']).encode('utf-8')
    print(line.decode('utf-8'), end='')

print('#'*25)

ARGS2 = ['ping', 'youtube.com','-c', '2']
YA_PING = subprocess.Popen(ARGS2, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    resut = chardet.detect(line)
    line = line.decode(resut['encoding']).encode('utf-8')
    print(line.decode('utf-8'), end='')