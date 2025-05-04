import math
from typing import Union

from scipy.special import gammainc

from constants import PI


def bit_frequency_test(sequence: str) -> float:
    """
    Выполняет частотный побитовый тест.
    :param sequence: Бинарная последовательность.
    :return: Значение P.
    """
    if not sequence:
        return 0.0

    sum_sequence = 0.0

    for bit in sequence:
        if bit == "1":
            sum_sequence += 1
        else:
            sum_sequence -= 1

    sum_sequence /= math.sqrt(len(sequence))
    p_value = math.erfc(abs(sum_sequence) / math.sqrt(2))

    return p_value


def test_for_identical_consecutive_bits(sequence: str) -> float:
    """
    Выполняет тест на одинаковые подряд идущие биты.
    :param sequence: Бинарная последовательность.
    :return: Значение P.
    """
    if not sequence:
        return 0.0

    share_of_units = 0.0

    for bit in sequence:
        if bit == "1":
            share_of_units += 1

    share_of_units /= len(sequence)

    if abs(share_of_units-0.5) >= 2 / math.sqrt(len(sequence)):
        return 0.0

    number_of_sign_alternations = 0.0

    for i in range(len(sequence) - 1):
        if sequence[i] != sequence[i + 1]:
            number_of_sign_alternations += 1

    numerator = abs(
        number_of_sign_alternations - 2 * len(sequence) * share_of_units * (1 - share_of_units)
    )
    denominator = 2 * math.sqrt(2 * len(sequence)) * share_of_units * (1 - share_of_units)
    p_value = math.erfc(numerator / denominator)

    return p_value


def test_for_the_longest_sequence_of_ones(sequence: str) -> Union[float, None]:
    """
    Тест на самую длинную последовательность единиц в блоке.
    :param sequence: Бинарная последовательность.
    :return: Значение P.
    """
    if not sequence:
        return 0.0

    v = [0, 0, 0, 0]

    block_size = 8

    for i in range(0, len(sequence), block_size):
        block = sequence[i:i + block_size]
        max_len = 0
        current_len = 0

        for bit in block:
            if bit == '1':
                current_len += 1
                if current_len > max_len:
                    max_len = current_len
            else:
                current_len = 0

        if max_len <= 1:
            v[0] += 1
        if max_len == 2:
            v[1] += 1
        if max_len == 3:
            v[2] += 1
        if max_len >= 4:
            v[3] += 1

    hi_square = 0.0

    for i in range(4):
        hi_square += ((v[i] - 16 * PI[i]) ** 2) / (16 * PI[i])

    p_value = gammainc(1.5, hi_square / 2)

    return p_value


def tests(sequence: str, filename: str) -> None:
    """
    Запускает тесты для бинарной последовательности.
    :param sequence: Бинарная последовательность.
    :param filename: Имя файла для сохранения результатов.
    """
    test_names = [
        "Частотный побитовый тест",
        "Тест на одинаковые подряд идущие биты",
        "Тест на самую длинную последовательность единиц в блоке"
    ]
    p_values = [0, 0, 0]

    p_values[0] = bit_frequency_test(sequence)
    p_values[1] = test_for_identical_consecutive_bits(sequence)
    p_values[2] = test_for_the_longest_sequence_of_ones(sequence)

    write_result(sequence, filename, test_names, p_values)


def check_p_value(p_value: float) -> str:
    """
    Проверяет значение P для результатов.
    :param p_value: Значение P.
    :return: Итог.
    """
    conclusion = "Пройден" if p_value >= 0.01 else "Провален"
    return conclusion


def write_result(sequence: str, filename: str, test_names:list[str], p_values: list[float]) -> None:
    """
    Записывает результат в файл.
    :param sequence: Бинарная последовательность.
    :param filename: Имя файла для сохранения результатов.
    :param test_names: Названия тестов.
    :param p_values: Значения P каждого теста.
    """

    try:
        with open(filename, mode='w', encoding="utf-8") as f:
            f.write(f"Последовательность: {sequence}\n")
            for i in range(3):
                f.write(f"Тест: {test_names[i]}\n")
                f.write(f"P: {p_values[i]}\n")
                f.write(f"Итог: {check_p_value(p_values[i])}\n\n")
        print(f"Содержимое успешно сохранено в файл {filename}.")
    except Exception as e:
        print(f"Произошла ошибка при сохранении в файл {filename}: {e}")