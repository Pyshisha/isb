from utils import read_from_file, read_json, save_to_file, save_dict_to_json
from constants import ENCRYPTED_TEXT, DECRYPTED_TEXT, KEY, RUSSIAN_FREQUENCIES, MANUALLY_KEY
from frequency_analysis import calculate_frequencies, generate_key_from_frequencies, decrypt_text


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

    key = generate_key_from_frequencies(encrypted_text, rus_freq)

    print("Сгенерированный ключ:")
    for k, v in key.items():
        print(f"{k} -> {v}")
    save_dict_to_json(KEY, key)

    decrypted_text = decrypt_text(encrypted_text, key)
    print("\nТекст, расшифрованный с помощью сгенерированного ключа:")
    print(decrypted_text)

    manually_key = read_json(MANUALLY_KEY)

    if not manually_key:
        print("Ошибка: не удалось прочитать подобранный вручную ключ.")
        return

    decrypted_text_manually = decrypt_text(encrypted_text, manually_key)
    print("\nТекст, расшифрованный с помощью подобранного вручную ключа:")
    print(decrypted_text_manually)
    save_to_file(DECRYPTED_TEXT, decrypted_text_manually)


if __name__ == "__main__":
    main()
