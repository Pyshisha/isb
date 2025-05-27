
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.rsa import (RSAPublicKey, RSAPrivateKey)
from isb.lab_3.asymmetric import AsymmetricCipher

class KeyWorker:
    @staticmethod
    def generate_rsa_keys() -> tuple[RSAPublicKey, RSAPrivateKey]:

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        return public_key, private_key

    @staticmethod
    def generate_seed_key() -> bytes:
        key_size=128

        seed_key = os.urandom(key_size // 8)
        return seed_key

    @staticmethod
    def generate_keys(settings):

        print("\nГенерация ключей началась")
        symmetric_key = KeyWorker.generate_seed_key()
        public_key, private_key = KeyWorker.generate_rsa_keys()
        encrypted_sym_key_path = settings['encrypted_symmetric_key_file']
        if not encrypted_sym_key_path:
            print("Не указан путь для сохранения зашифрованного симметричного ключа.")
            exit(1)
        encrypt_symmetric_key = AsymmetricCipher.encrypt(public_key, symmetric_key)
        print("Генерация ключей завершена")
        return public_key, private_key, encrypt_symmetric_key