
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Symmetrical:
    @staticmethod
    def symmetric_encrypt_seed(content, symmetric_key):
        print("Шифрование началось")


        padder = padding.ANSIX923(32).padder()
        padded_text = padder.update(content) + padder.finalize()

        # шифрование текста симметричным алгоритмом

        iv = os.urandom(16)  # случайное значение для инициализации блочного режима, должно быть размером с блок и каждый раз новым
        cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        print("Шифровка завершена!")
        return c_text

    @staticmethod
    def symmetric_decrypt_seed(encrypted_content, symmetric_key):
        print("Расшифровка началась")
        iv = encrypted_content[:16]
        ciphertext = encrypted_content[16:]

        cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.ANSIX923(32).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

        print("Данные расшифрованы!")
        return unpadded_dc_text