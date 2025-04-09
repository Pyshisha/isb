from constants import ALPHABET, ALPHABET_SIZE


def letter_to_number(letter: str) -> int:
    """
    Возвращает номер буквы (начиная с 1).
    :param letter: Буква.
    :return: Номер буквы.
    """
    return ALPHABET.index(letter) + 1


def number_to_letter(number: int) -> str:
    """
     Возвращает букву по номеру (от 1 до 33).
     :param number: Номер буквы.
    :return: Буква.
    """
    return ALPHABET[number - 1]


def prepare_text(text: str) -> str:
    """
    Приводит текст к верхнему регистру и заменяет Ё на Е.
    :param text: Строка с текстом.
    :return: Подготовленная строка.
    """
    return text.upper().replace('Ё', 'Е')


def repeat_key(key: str, length: int) -> str:
    """
    Повторяет ключ до нужной длины.
    :param key: Ключ.
    :param length: Длинна строки с текстом.
    :return: Подготовленный ключ.
    """
    return (key * (length // len(key) + 1))[:length]


def encrypt_trithemius(text: str, key: str) -> str:
    """
    Шифрует текст с помощью шифра Тритемиуса.
    :param text: Текст для шифрования.
    :param key: Ключ.
    :return: Зашифрованный текст.
    """
    text = prepare_text(text)
    key = prepare_text(key)
    long_key = repeat_key(key, len(text))

    encrypted_text = ''
    key_index = 0

    for char in text:
        if char in ALPHABET:
            k_char = long_key[key_index]
            t_num = letter_to_number(char)
            k_num = letter_to_number(k_char)
            total = t_num + k_num
            if total > ALPHABET_SIZE:
                total -= ALPHABET_SIZE
            encrypted_text += number_to_letter(total)
            key_index += 1
        else:
            encrypted_text += char
            key_index += 1

    grouped = ''
    count = 0
    for c in encrypted_text:

        if count and count % 5 == 0:
            grouped += ' '
        grouped += c
        count += 1

    return grouped


def decrypt_trithemius(ciphertext: str, key: str) -> str:
    """
    Расшифровывает текст, зашифрованный шифром Тритемиуса.
    :param ciphertext: Текст для расшифровки.
    :param key: Ключ.
    :return: Расшифрованный текст.
    """
    ciphertext = prepare_text(ciphertext)
    key = prepare_text(key)
    long_key = repeat_key(key, len(ciphertext))

    no_grouped = ''
    count = 0

    for c in ciphertext:
        if count != 5:
            no_grouped += c
            count += 1
        else:
            count = 0

    decrypted_text = ''
    key_index = 0

    for char in no_grouped:
        if char in ALPHABET:
            k_char = long_key[key_index]
            c_num = letter_to_number(char)
            k_num = letter_to_number(k_char)
            total = c_num - k_num
            if total <= 0:
                total += ALPHABET_SIZE
            decrypted_text += number_to_letter(total)
            key_index += 1
        else:
            decrypted_text += char
            key_index += 1

    return decrypted_text
