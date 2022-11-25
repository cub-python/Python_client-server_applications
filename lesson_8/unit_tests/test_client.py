"""Unit-тесты клиента"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from general.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presence, response_reply


class TestClass(unittest.TestCase):
    # Класс с тестами
    def test_def_presense(self):
        """Тест коректного запроса"""
        test = create_presence()
        test[TIME] = 1.1  # время необходимо приравнять принудительно
        # иначе тест никогда не будет пройден
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_reply(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(response_reply({RESPONSE: 200}), '200 : OK')

    def test_400_reply(self):
        """Тест корректного разбора 400"""
        self.assertEqual(response_reply({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, response_reply, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
