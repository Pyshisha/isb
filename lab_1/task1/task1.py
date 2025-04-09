from isb.lab_1.utils import read_from_file, save_to_file
from constants import ORIGINAL_TEXT, KEY, ENCRYPT_TEXT
from trithemius import encrypt_trithemius, decrypt_trithemius


def main() -> None:
    """
    Главная функция программы. Выводит результаты.
    """

    original = read_from_file(ORIGINAL_TEXT)
    key = read_from_file(KEY)

    if not original or not key:
        print("Ошибка: не удалось прочитать текст или ключ.")
        return

    encrypted = encrypt_trithemius(original, key)
    save_to_file(ENCRYPT_TEXT, encrypted)
    print(" Зашифрованный текст:")
    print(encrypted)

    decrypted = decrypt_trithemius(encrypted, key)
    print("\n Расшифрованный текст:")
    print(decrypted)


if __name__ == "__main__":
    main()
