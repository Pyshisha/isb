def calculate_frequencies(text: str) -> dict[str, float]:
    """
    Подсчитывает частоту каждого символа в тексте.
    Символы упорядочиваются по убыванию частоты.
    :param text: Текст, для которого нужно выполнить частотный анализ.
    :return: Словарь с частотами символов, отсортированный по убыванию частоты.
    """
    if not text:
        raise ValueError("Текст не может быть пустым.")

    frequencies = {}

    for char in text:
        frequencies[char] = frequencies.get(char, 0) + 1

    total_length = len(text)
    normalized_frequencies = {}
    for char, count in frequencies.items():
        normalized_frequencies[char] = count / total_length

    sorted_frequencies = dict(sorted(normalized_frequencies.items(), key=lambda item: item[1], reverse=True))

    return sorted_frequencies


def generate_key_from_frequencies(text: str, reference_frequencies: dict) -> dict:
    """
    Создает ключ, используя частоты символов и эталонные частоты русского алфавита.
    :param text: Текст, для которого нужно найти ключ.
    :param reference_frequencies: Эталонные частоты русского алфавита.
    :return: Ключ.
    """

    text_frequencies = calculate_frequencies(text)

    text_freq = list(text_frequencies.keys())
    ref_freq = list(reference_frequencies.keys())

    key = {}
    for i in range(min(len(text_freq), len(ref_freq))):
        key[text_freq[i]] = ref_freq[i]

    return key


def decrypt_text(text: str, key: dict) -> str:
    """
    Расшифровывает текст, используя ключ.
    :param text: Текст для расшифровки.
    :param key: Ключ.
    :return: Расшифрованный текст.
    """
    result = []
    for char in text:
        if char in key:
            result.append(key[char])
        else:
            result.append(char)
    return ''.join(result)


