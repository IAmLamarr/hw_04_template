# Модуль шифрования/дешифрования данных

ENCODING = 'utf-8'

"""
Функция применения алгоритма побитового XOR
https://blog.boot.dev/cryptography/why-xor-in-cryptography/


text - строка, исходный текст
encoding_key - строка, ключ шифрования
"""
def apply_encoding(source, key):
	key_repeats = (len(source) - 1) // len(key) + 1
	key_bytes = (key * key_repeats)[:len(source)].encode(ENCODING)
	return bytes([b1 ^ b2 for (b1, b2) in zip(source, key_bytes)])


"""
Функция кодирования текста по ключу шифрования

text - строка, исходный текст
encoding_key - строка, ключ шифрования
"""
def encode_text(text, encoding_key):
	text_bytes = text.encode(ENCODING)
	encoded_bytes = apply_encoding(text_bytes, encoding_key)
	return encoded_bytes

"""
Функция декодирования байтов по ключу шифрования

text - массив байтов, зашифрованные данные
encoding_key - строка, ключ шифрования
"""
def decode_bytes(text_bytes, encoding_key):
	decoded_bytes = apply_encoding(text_bytes, encoding_key)
	return decoded_bytes.decode(ENCODING)