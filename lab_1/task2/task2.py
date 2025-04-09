from isb.lab_1.utils import read_from_file, read_json, save_to_file, save_dict_to_json
from constants import ENCRYPTED_TEXT, DECRYPTED_TEXT, KEY, RUSSIAN_FREQUENCIES
from frequency_analysis import calculate_frequencies, decrypt_text


def modify_key(key: dict) -> dict:
    """
    Позволяет изменять ключ через консоль.
    Запрашивает у пользователя символы, которые он хочет изменить, и на что.
    :param key: Текущий ключ (словарь с сопоставлением символов).
    :return: Обновленный ключ.
    """
    updated_key = key.copy()

    while True:
        print("\nТекущий ключ:")
        for char, ref_char in updated_key.items():
            print(f"{char} -> {ref_char}")

        old_char = input("\nВведите символ, который хотите изменить (или 'exit' для выхода): ").strip()

        if old_char == 'exit':
            break

        if old_char not in updated_key:
            print(f"Символ '{old_char}' не найден в ключе. Попробуйте снова.")
            continue

        new_char = input(f"Введите новый символ для '{old_char}': ").strip()

        updated_key[old_char] = new_char

        print(f"Символ '{old_char}' был заменен на '{new_char}'.\n")

    return updated_key


def main():
    """
    Главная функция программы. Выводит результаты.
    """

    rus_freq = read_json(RUSSIAN_FREQUENCIES)
    encrypted_text = read_from_file(ENCRYPTED_TEXT)
    encrypted_text = encrypted_text.replace("\n", " ")

    if not rus_freq or not encrypted_text:
        print("Ошибка: не удалось прочитать частоты или зашифрованный текст.")
        return

    frequencies = calculate_frequencies(encrypted_text)

    print("Полученные частоты:")
    for i, j in frequencies.items():
        print(f"{i} : {j}")

    key = read_json(KEY)

    print("Ключ:")
    for k, v in key.items():
        print(f"{k} -> {v}")

    modify_choice = input("Хотите изменить ключ? (yes/no): ").strip().lower()

    if modify_choice == 'yes':
        updated_key = modify_key(key)
        print("\nОбновленный ключ:")
        for char, ref_char in updated_key.items():
            print(f"{char} -> {ref_char}")
        save_dict_to_json(KEY, key)
    else:
        print("Ключ не был изменен.")

    decrypted_text = decrypt_text(encrypted_text, key)
    print("\nТекст, расшифрованный с помощью подобранного вручную ключа:")
    print(decrypted_text)
    save_to_file(DECRYPTED_TEXT, decrypted_text)


if __name__ == "__main__":
    main()
