from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey


class AsymmetricCipher:
    @staticmethod
    def encrypt(public_key: RSAPublicKey, data: bytes) -> bytes:
        """
        Шифрует данные с помощью открытого RSA ключа.
        :param public_key: Открытый RSA ключ.
        :param data: Данные для шифрования.
        :return: Зашифрованные данные.
        """
        try:
            return public_key.encrypt(
                data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        except Exception as e:
            raise Exception(f"Error: Ошибка при шифровании данных: {e}")

    @staticmethod
    def decrypt(private_key: RSAPrivateKey, encrypted_data: bytes) -> bytes:
        """
        Расшифровывает данные с помощью закрытого RSA ключа.
        :param private_key: Закрытый RSA ключ.
        :param encrypted_data: Зашифрованные данные.
        :return: Расшифрованные данные.
        :raises Exception: В случае ошибки расшифровки.
        """
        try:
            return private_key.decrypt(
                encrypted_data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        except Exception as e:
            raise Exception(f"Ошибка при расшифровке данных: {e}")