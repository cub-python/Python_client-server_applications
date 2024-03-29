'''
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
'''
import yaml
dict = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
           'items_quantity': 4,
           'items_ptice': {'computer': '200€-1000€',
                           'printer': '100€-300€',
                           'keyboard': '5€-50€',
                           'mouse': '4€-7€'}}

def write_dict_to_yaml(dict, file_1):
    with open(file_1, 'w') as f_n:
        yaml.dump(dict, f_n, default_flow_style=False, allow_unicode = True)

    with open(file_1) as f_n:
        f_n_content = yaml.load(f_n)

    print(f_n_content == dict)

if __name__ == "__main__":
    my_dict = {
        '100€': [1, 2, 3, 4],
        '200€': 8000,
        '300€': {
            'first': [1,2,3,4],
            'second': 800,
        }
    }

    write_dict_to_yaml(my_dict, 'file_1.yaml')