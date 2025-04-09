import json
import typing
from typing import Union


def read_from_file(filename: str) -> Union[str, None]:
    """
    Читает строку из файла.
    :param filename: Имя файла.
    :return: Строка, прочитанная из файла или None в случае ошибки.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return None


def save_to_file(filename: str, content: str) -> None:
    """
    Сохраняет строку в файл.
    :param filename: Имя файла.
    :param content: Строка для сохранения.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Содержимое успешно сохранено в файл {filename}.")
    except Exception as e:
        print(f"Произошла ошибка при сохранении в файл {filename}: {e}")


def read_json(filename: str) -> Union[dict[str, float], None]:
    """
    Читает JSON.
    :param filename: Имя файла.
    :return: Содержимое JSON, или None в случае ошибки.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except json.JSONDecodeError:
        print(f"Файл {filename} не является корректным JSON.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return None


def save_dict_to_json(filename: str, content: dict[str, float]) -> None:
    """
    Сохраняет словарь в файл JSON.
    :param filename: Имя файла.
    :param content: Словарь для сохранения.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Записываем словарь в файл в формате JSON
            json.dump(content, file, ensure_ascii=False, indent=4)
        print(f"Ключ успешно записан в файл {filename}.")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


def save_dict_to_file(filename: str, content: dict[str, float]) -> None:
    """
    Сохраняет словарь в файл.
    :param filename: Имя файла.
    :param content: Словарь для сохранения.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for symbol, letter in content.items():
                f.write(f"{symbol} -> {letter}\n")
        print(f"Ключ успешно записан в файл {filename}.")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")
