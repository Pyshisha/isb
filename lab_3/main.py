import argparse

from isb.lab_3.key_creator import KeyWorker
from isb.lab_3.utils import WorkWithFiles
from isb.lab_3.asymmetric import AsymmetricCipher
from isb.lab_3.symmetrical import Symmetrical


def parse_args() -> argparse.Namespace:
    """
    Парсит аргументы командной строки.
    :return: Объект с аргументами.
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen','--generation',help='Запускает режим генерации ключей')
    group.add_argument('-enc','--encryption',help='Запускает режим шифрования')
    group.add_argument('-dec','--decryption',help='Запускает режим дешифрования')
    return parser.parse_args()

def main() -> None:
    """
    Главная функция программы.
    """
    args = parse_args()
    settings_path = None

    if args.generation is not None:
        settings_path = args.generation
    elif args.encryption is not None:
        settings_path = args.encryption
    elif args.decryption is not None:
        settings_path = args.decryption

    settings = WorkWithFiles.load_config(settings_path)

    if args.generation is not None:
        public_key, private_key, symmetric_key, encrypted_symmetric_key = KeyWorker.generate_keys(settings)
        WorkWithFiles.save_public_key(public_key, settings['public_key'])
        WorkWithFiles.save_symmetric_key(symmetric_key, settings['symmetric_key'])
        WorkWithFiles.save_private_key(private_key, settings['secret_key'])
        WorkWithFiles.save_encrypt_symmetric_key(encrypted_symmetric_key, settings['encrypted_symmetric_key_file'])
    elif args.encryption is not None:
        print("\nШифрование информации с помощью алгоритма SEED")
        path_to_initial = settings['initial_file']
        path_to_private_key = settings['secret_key']
        path_to_encrypted_sym_key = settings['encrypted_symmetric_key_file']
        encrypted_file_path = settings['encrypted_file']
        if not all([path_to_initial, path_to_private_key,
                    path_to_encrypted_sym_key, encrypted_file_path]):
            print(
                "Error: Не указаны все необходимые пути в настройках для шифрования.")
        private_key = WorkWithFiles.read_private_key(path_to_private_key)
        encrypted_sym_key_data = WorkWithFiles.read_file(path_to_encrypted_sym_key)
        symmetric_key = AsymmetricCipher.decrypt(private_key, encrypted_sym_key_data)
        print(f"Чтение файла {path_to_initial}...")
        content = WorkWithFiles.read_file(path_to_initial)

        ciphertext = Symmetrical.symmetric_encrypt_seed(content, symmetric_key)

        print(f"Сохранение зашифрованных данных в файл {encrypted_file_path}...")
        WorkWithFiles.write_file(encrypted_file_path, ciphertext)
        print("Шифрование и сохранение завершено")
    else:
        print("\nДешифрование информации с помощью алгоритма SEED")
        path_to_encrypt_file = settings['encrypted_file']
        path_to_private_key = settings['secret_key']
        path_to_encrypted_sym_key = settings['encrypted_symmetric_key_file']
        path_to_decrypted_file = settings['decrypted_file']

        if not all([path_to_encrypt_file, path_to_private_key,
                path_to_encrypted_sym_key, path_to_decrypted_file]):
            print(
                  "Error: Не указаны все необходимые пути в настройках для дешифрования.")
        private_key = WorkWithFiles.read_private_key(path_to_private_key)
        encrypted_sym_key_data = WorkWithFiles.read_file(path_to_encrypted_sym_key)
        symmetric_key = AsymmetricCipher.decrypt(private_key, encrypted_sym_key_data)
        print(f"Чтение зашифрованного файла {path_to_encrypt_file}...")
        encrypted_content = WorkWithFiles.read_file(path_to_encrypt_file)
        decrypted_text = Symmetrical.symmetric_decrypt_seed(encrypted_content, symmetric_key)

        print(f"Сохранение расшифрованных данных в {path_to_decrypted_file}...")
        WorkWithFiles.write_file(path_to_decrypted_file, decrypted_text)
        print("Дешифрование и сохранение завершено")

if __name__ == "__main__":
    main()
