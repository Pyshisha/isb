import os
from typing import Union, Tuple

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.rsa import (RSAPublicKey, RSAPrivateKey)

from isb.lab_3.asymmetric import AsymmetricCipher


class KeyWorker:
    """
    Класс для генерации различных криптографических ключей.
    """
    @staticmethod
    def generate_rsa_keys() -> tuple[RSAPublicKey, RSAPrivateKey]:
        """
        Генерирует пару RSA ключей (открытый и закрытый).
        :return: Кортеж (открытый ключ, закрытый ключ).
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        return public_key, private_key

    @staticmethod
    def generate_seed_key() -> bytes:
        """
        Генерирует случайный симметричный ключ (seed key) размером 128 бит.
        :return: Симметричный ключ.
        """
        key_size=128

        seed_key = os.urandom(key_size // 8)
        return seed_key

    @staticmethod
    def generate_keys(settings: dict) -> Union[Tuple[RSAPublicKey, RSAPrivateKey, bytes, bytes], None]:
        """
        Генерирует RSA ключи и симметричный ключ, затем зашифровывает симметричный ключ открытым RSA ключом.
        :param settings: Словарь настроек, должен содержать ключ 'encrypted_symmetric_key_file' с путём сохранения.
        :return: Кортеж (открытый ключ, закрытый ключ, симметричный ключ, зашифрованный симметричный ключ).
        """
        print("\nГенерация ключей началась")
        symmetric_key = KeyWorker.generate_seed_key()
        public_key, private_key = KeyWorker.generate_rsa_keys()
        encrypted_sym_key_path = settings['encrypted_symmetric_key_file']
        if not encrypted_sym_key_path:
            print("Не указан путь для сохранения зашифрованного симметричного ключа.")
        encrypt_symmetric_key = AsymmetricCipher.encrypt(public_key, symmetric_key)
        print("Генерация ключей завершена")
        return public_key, private_key, symmetric_key, encrypt_symmetric_key
