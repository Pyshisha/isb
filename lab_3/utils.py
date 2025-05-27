

from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives import serialization



class WorkWithFiles:
    @staticmethod
    def write_file(path_to_file, content):
        print(f"Сохранение данных в файл {path_to_file}...")
        try:
            with open(path_to_file, 'wb') as f:
                f.write(content)
            print(f"||Данные успешно сохранены||")
        except Exception as e:
            print(f"Error: Произошла ошибка при сохранении в файл {e}")


    @staticmethod
    def read_file(path_to_file):

        print(f"Чтение данных из файла {path_to_file}...")
        try:
            with open(path_to_file, 'rb') as f:
                content = f.read()
            print(f"||Данные успешно прочитаны||")
            return content
        except FileNotFoundError:
            print(f"Error: Файл не найден")

        except Exception as e:
            print(f"Error Произошла ошибка при чтении в файла {e}")


    @staticmethod
    def read_private_key(path_to_key):
        print(f"Загрузка закрытого ключа из файла {path_to_key}...")
        try:
            with open(path_to_key, 'rb') as pem_in:
                private_bytes = pem_in.read()
            d_private_key = load_pem_private_key(private_bytes, password=None, )
            print("||Приватный ключ загружен!||")
            return d_private_key
        except FileNotFoundError:
            print(f"Error: Файл приватного ключа не найден по пути {path_to_key}")

        except Exception as e:
            print(f"Error: Произошла ошибка при загрузки закрытого ключа {e}")


    @staticmethod
    def read_public_key(path_to_key):
        """
        Reading the public key from a file
        :param path_to_key: Path to public RSA key
        :return: Public key
        """
        print(f"Загрузка открытого ключа из файла {path_to_key}...")
        try:
            with open(path_to_key, 'rb') as pem_in:
                public_bytes = pem_in.read()
            d_public_key = load_pem_public_key(public_bytes)
            print("||Открытый ключ загружен||")
            return d_public_key
        except FileNotFoundError:
            print(f"Error: Файл открытого ключа не найден по пути {path_to_key}")

        except Exception as e:
            print(f"Error: Произошла ошибка при загрузки открытого ключа {e}")


    @staticmethod
    def save_public_key(public_key, path_to_save):


        print(f"Сохранение открытого ключа в {path_to_save}...")
        with open(path_to_save, 'wb') as public_out:
            public_out.write(
                public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                        format=serialization.PublicFormat.SubjectPublicKeyInfo))
        print(f"Открытый ключ сохранен в {path_to_save}")

    @staticmethod
    def save_private_key(private_key, path_to_save):
        print(f"Сохранение закрытого ключа в {path_to_save}...")
        with open(path_to_save, 'wb') as private_out:
            private_out.write(
                private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                          format=serialization.PrivateFormat.TraditionalOpenSSL,
                                          encryption_algorithm=serialization.NoEncryption()))
        print(f"Закрытый ключ сохранен в {path_to_save}")


    @staticmethod
    def save_encrypt_symmetric_key(encrypted_symmetric_key, settings):

        encrypted_sym_key_path = settings['encrypted_symmetric_key_file']
        if not encrypted_sym_key_path:
            encrypted_sym_key_path = settings.get('symmetric_key')
            if not encrypted_sym_key_path:
                print(
                    "Error: Не указан путь для сохранения зашифрованного симметричного ключа в файле конфигурации.")
                exit(1)
        print(f"Сохранение зашиф. симметричного ключа в {settings['encrypted_symmetric_key_file']}...")
        WorkWithFiles.write_file(settings['encrypted_symmetric_key_file'], encrypted_symmetric_key)
        print(f"Зашифрованный симметричный ключ сохранен в {settings['encrypted_symmetric_key_file']}.")

    @staticmethod
    def save_symmetric_key(symmetric_key, path_to_save):
        print(f"Сохранение сим. ключа в {path_to_save}...")
        with open(path_to_save, 'wb') as key_file:
            key_file.write(symmetric_key)
        print(f"Сим. ключ сохранен в {path_to_save}")

    @staticmethod
    def read_symmetric_key(path_to_key):
        print(f"Загрузка сим. ключа из файла {path_to_key}...")
        try:
            with open(path_to_key, mode='rb') as key_file:
                symmetric_key = key_file.read()
            print("Сим. ключ загружен")
            return symmetric_key
        except FileNotFoundError:
            print(f"Error: Файл сим. ключа не найден по пути {path_to_key}")

        except Exception as e:
                print(f"Error: Произошла ошибка при загрузки сим. ключа {e}")
