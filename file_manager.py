# Модуль работы с файлами

from crypt import apply_encoding, encode_text, decode_bytes

"""
Функция извлечения ключа шифрования из файла *.key

filename - строка, путь к файлу с ключом шифрования (.key)

"""


def extract_encoding_key(filename):
    key_file = open(filename, 'r')
    return key_file.read()


"""
Функция экспорта данных в формат .phone

contacts - массив контактов
encoding_key_path - строка, путь к файлу с ключом шифрования (по умолчанию - data/phone.key)
filename - строка, путь к файлу экспорта (по умолчанию - data/export.phone)

"""


def export_data(contacts, encoding_key_path="data/phone.key", filename="data/export.phone"):
    encoding_key = extract_encoding_key(encoding_key_path)
    export_string = ""
    """
	Доделать функцию, написать конвертацию контактов (data) в байты с сохранением их в файл
	- Конвертировать контакты в строку (при помощи serialize), не забыть в конце каждой строки контакта "\n"
	- Зашифровать полученный текст в байты (см. crypt.py)
	- Записать байты в файл по пути filename (для записи байтов использовать open() с модом 'wb')
	"""


"""
Функция импорта данных из формата .phone

filename - строка, путь к файлу .phone (по умолчанию - data/export.phone)
encoding_key_path - строка, путь к файлу с ключом шифрования (по умолчанию - data/phone.key)

Необходимо вернуть массив контактов
"""


def import_data(filename="data/export.phone", encoding_key_path="data/phone.key"):
    entities = []

    encoding_key = extract_encoding_key(encoding_key_path)
    text_bytes = open(filename, 'rb').read()

    """
	Доделать функцию, написать конвертацию байтов (text_bytes) в массив контактов
	- Декодировать байты в строку (см. crypt.py)
	- Написать конвертацию строки в массив контактов (при помощи deserialize)
	"""
    return entities


"""
Функция превращения контакта в строку (на умном - сериализация)

obj - контакт (массив с данными)

Контакт должен быть записан в формате <phone;first_name;last_name;patronymic;email;city;address>
Если каких-то данных нет, вместо них должна быть пустая строка
Например:
<+012345678901;Ivan;Ivanov;Ivanovich;;Kazan;Baumana str., 666 building, 42 flat>

"""


def serialize(obj):
    pass


"""
Функция превращения в строки в контакт (на умном - десериализация)

obj_str - строка, содержащая данные контакта в формате
<phone;first_name;last_name;patronymic;email;city;address>

"""


def deserialize(obj_str):
    pass
