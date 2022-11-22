 # утилиты

import json

from lesson_4.general.variables import MAX_PACKAGE_LENGTH, ENCODING


def get_message(client):
    '''
    :param client:
    :return:
    Утилита приёма и декодирования сообщения
    принимает байты выдаёт словарь, если приняточто-то другое отдаёт ошибку значения
    :param client:
    :return:
    '''

    coded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(coded_response, bytes):
        json_response = coded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError

def send_message(sock, message):
    '''
    Утилита кодирования и отправки сообщения
    принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    '''


    js_message = json.dumps(message)
    coded_message = js_message.encode(ENCODING)
    sock.send(coded_message)
