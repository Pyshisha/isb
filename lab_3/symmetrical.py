import os
from typing import Union

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.decrepit.ciphers import algorithms  # <-- ВАЖНО!
from cryptography.hazmat.primitives.ciphers import Cipher, modes


class Symmetrical:
    @staticmethod
    def symmetric_encrypt_seed(content: Union[str, bytes], symmetric_key: bytes) -> bytes:
        """
        Шифрует данные с помощью алгоритма SEED.
        :param content: Исходные данные.
        :param symmetric_key: Симметричный ключ.
        :return: Зашифрованные данные с IV в начале.
        """
        print("Шифрование началось")

        if isinstance(content, str):
            content_bytes = content.encode('utf-8')
        else:
            content_bytes = content

        padder = padding.ANSIX923(128).padder()
        padded_text = padder.update(content_bytes) + padder.finalize()

        iv = os.urandom(16)  # случайное значение для инициализации блочного режима, должно быть размером с блок и каждый раз новым
        cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        print("Шифровка завершена!")
        return iv + c_text

    @staticmethod
    def symmetric_decrypt_seed(encrypted_content: bytes, symmetric_key: bytes) -> bytes:
        """
        Расшифровывает данные, зашифрованные алгоритмом SEED.
        :param encrypted_content: Зашифрованные данные с IV в начале.
        :param symmetric_key: Симметричный ключ.
        :return: Расшифрованные исходные данные.
        """
        if isinstance(encrypted_content, str):
            content_bytes = encrypted_content.encode('utf-8')
        else:
            content_bytes = encrypted_content
        print("Расшифровка началась")
        iv = content_bytes[:16]
        ciphertext = content_bytes[16:]

        cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.ANSIX923(128).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

        print("Данные расшифрованы")
        return unpadded_dc_text
