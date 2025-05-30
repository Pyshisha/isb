import json
from typing import Union

from cryptography.hazmat.primitives.asymmetric.dh import DHPrivateKey, DHPublicKey
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import (RSAPublicKey, RSAPrivateKey)


class WorkWithFiles:
    """
        Класс для работы с файлами.
    """
    @staticmethod
    def write_file(path_to_file: str, content:bytes) -> None:
        """
        Сохраняет строку в файл.
        :param path_to_file: Путь к файлу.
        :param content: Строка для сохранения.
        """
        print(f"Сохранение данных в файл {path_to_file}...")
        try:
            with open(path_to_file, 'wb') as f:
                f.write(content)
            print(f"Данные успешно сохранены")
        except FileNotFoundError:
            print(f"Error: путь {path_to_file} не найден.")
        except PermissionError:
            print(f"Error: нет прав для записи в {path_to_file}.")
        except OSError as e:
            print(f"Error: Ошибка записи в файл {path_to_file}: {e}")

    @staticmethod
    def read_file(path_to_file: str) -> Union[bytes, None]:
        """
        Читает строку из файла.
        :param path_to_file: Имя файла.
        :return: Строка, прочитанная из файла или None в случае ошибки.
        """

        print(f"Чтение данных из файла {path_to_file}...")
        try:
            with open(path_to_file, 'rb') as f:
                content = f.read()
            print(f"Данные успешно прочитаны")
            return content
        except FileNotFoundError:
            print(f"Error: Файл не найден")
        except Exception as e:
            print(f"Error: Произошла ошибка при чтении в файла {e}")

    @staticmethod
    def read_private_key(path_to_key: str) -> Union[RSAPrivateKey, None]:
        """
        Загружает приватный ключ из PEM-файла.
        :param path_to_key: Имя файла.
        :return: Приватный ключ или None в случае ошибки.
        """
        print(f"Загрузка закрытого ключа из файла {path_to_key}...")
        try:
            with open(path_to_key, 'rb') as pem_in:
                private_bytes = pem_in.read()
            private_key = load_pem_private_key(private_bytes, password=None, )
            print("Приватный ключ загружен")
            return private_key
        except FileNotFoundError:
            print(f"Error: Файл приватного ключа не найден по пути {path_to_key}")
        except Exception as e:
            print(f"Error: Произошла ошибка при загрузке закрытого ключа {e}")

    @staticmethod
    def read_public_key(path_to_key: str) -> Union[RSAPublicKey, None]:
        """
        Загружает открытый ключ из PEM-файла.
        :param path_to_key: Имя файла.
        :return: Открытый ключ или None в случае ошибки.
        """
        print(f"Загрузка открытого ключа из файла {path_to_key}...")
        try:
            with open(path_to_key, 'rb') as pem_in:
                public_bytes = pem_in.read()
            public_key = load_pem_public_key(public_bytes)
            print("Открытый ключ загружен")
            return public_key
        except FileNotFoundError:
            print(f"Error: Файл открытого ключа не найден по пути {path_to_key}")

        except Exception as e:
            print(f"Error: Произошла ошибка при загрузке открытого ключа {e}")

    @staticmethod
    def save_public_key(public_key: RSAPublicKey, path_to_save: str) -> None:
        """
        Сохраняет открытый ключ в файл в формате PEM.
        :param public_key: Объект открытого ключа.
        :param path_to_save: Путь к файлу, в который будет сохранён ключ.
        :return: None
        """
        print(f"Сохранение открытого ключа в {path_to_save}...")
        try:
            with open(path_to_save, 'wb') as public_out:
                public_out.write(
                    public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PublicFormat.SubjectPublicKeyInfo))
            print(f"Открытый ключ сохранен в {path_to_save}")
        except FileNotFoundError:
            print(f"Error: путь {path_to_save} не найден.")
        except PermissionError:
            print(f"Error: нет прав для записи в {path_to_save}.")
        except OSError as e:
            print(f"Error: Ошибка записи в файл {path_to_save}: {e}")

    @staticmethod
    def save_private_key(private_key: RSAPrivateKey, path_to_save: str) -> None:
        """
         Сохраняет закрытый ключ в файл в формате PEM.
         :param private_key: Объект закрытого ключа.
         :param path_to_save: Путь к файлу, в который будет сохранён ключ.
         :return: None
         """
        print(f"Сохранение закрытого ключа в {path_to_save}...")
        try:
            with open(path_to_save, 'wb') as private_out:
                private_out.write(
                    private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                              format=serialization.PrivateFormat.TraditionalOpenSSL,
                                              encryption_algorithm=serialization.NoEncryption()))
            print(f"Закрытый ключ сохранен в {path_to_save}")
        except FileNotFoundError:
            print(f"Error: путь {path_to_save} не найден.")
        except PermissionError:
            print(f"Error: нет прав для записи в {path_to_save}.")
        except OSError as e:
            print(f"Error: Ошибка записи в файл {path_to_save}: {e}")

    @staticmethod
    def save_encrypt_symmetric_key(encrypted_symmetric_key: bytes, path_to_save: str) -> None:
        """
         Сохраняет зашифрованный симметричный ключ в файл.
         :param encrypted_symmetric_key: Зашифрованные данные симметричного ключа (в виде байтов).
         :param path_to_save: Путь к файлу, в который будет сохранён ключ.
         :return: None
         """
        print(f"Сохранение зашифрованного симметричного ключа в {path_to_save}...")
        WorkWithFiles.write_file(path_to_save, encrypted_symmetric_key)
        print(f"Зашифрованный симметричный ключ успешно сохранён в {path_to_save}.")

    @staticmethod
    def save_symmetric_key(symmetric_key: bytes, path_to_save: str) -> None:
        """
         Сохраняет симметричный ключ в файл.
         :param symmetric_key: Симметричный ключ.
         :param path_to_save: Путь к файлу, в который будет сохранён ключ.
         :return: None
         """
        print(f"Сохранение сим. ключа в {path_to_save}...")
        try:
            with open(path_to_save, 'wb') as key_file:
                key_file.write(symmetric_key)
            print(f"Сим. ключ сохранен в {path_to_save}")
        except FileNotFoundError:
            print(f"Error: путь {path_to_save} не найден.")
        except PermissionError:
            print(f"Error: нет прав для записи в {path_to_save}.")
        except OSError as e:
            print(f"Error: Ошибка записи в файл {path_to_save}: {e}")


    @staticmethod
    def read_symmetric_key(path_to_key: str) -> Union[bytes, None]:
        """
        Загружает симметричный ключ из файла.
        :param path_to_key: Путь к файлу с симметричным ключом.
        :return: Симметричный ключ в виде байтов или None в случае ошибки.
        """
        print(f"Загрузка сим. ключа из файла {path_to_key}...")
        try:
            with open(path_to_key, mode='rb') as key_file:
                symmetric_key = key_file.read()
            print("Сим. ключ загружен")
            return symmetric_key
        except FileNotFoundError:
            print(f"Error: Файл сим. ключа не найден по пути {path_to_key}")
        except Exception as e:
            print(f"Error: Произошла ошибка при загрузке сим. ключа {e}")

    @staticmethod
    def load_config(path_to_settings: str) -> Union[dict, None]:
        """
        Загружает настройки из JSON-файла.
        :param path_to_settings: Путь к JSON-файлу с настройками.
        :return: Загруженный словарь настроек или None в случае ошибки.
        """
        print(f"Загрузка настроек из файла {path_to_settings}...")
        try:
            with open(path_to_settings, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print("Настройки загружены")
            return config
        except FileNotFoundError:
            print(f"Error: Настройки не найдены по пути: {path_to_settings}")
        except json.JSONDecodeError as e:
            print(f"Error: {e}")
