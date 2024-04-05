import os

def get_desktop_path() -> str:
    """
    Повертає шлях до робочого столу користувача.
    """
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def read_file(filepath: str) -> list:
    """
    Зчитує вміст файлу та повертає список рядків.
    :param filepath: Шлях до файлу.
    :return: Список рядків у файлі.
    """
    try:
        with open(filepath, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Сталася помилка під час читання файлу:", str(e))
        return []

def filter_lines(lines: list, keyword: str) -> list:
    """
    Фільтрує список рядків за ключовим словом та повертає відфільтровані рядки.
    :param lines: Список рядків для фільтрації.
    :param keyword: Ключове слово, за яким фільтруються рядки.
    :return: Список відфільтрованих рядків.
    """
    return [line.strip() for line in lines if keyword in line]

def write_filtered_lines(filtered_lines: list):
    """
    Записує відфільтровані рядки у файл "filtered.txt" на робочому столі.
    :param filtered_lines: Список відфільтрованих рядків.
    """
    try:
        if filtered_lines:
            desktop_path = get_desktop_path()
            filtered_file_path = os.path.join(desktop_path, "filtered.txt")
            with open(filtered_file_path, 'w') as filtered_file:
                filtered_file.write('\n'.join(filtered_lines))
            print("Файл успішно створено з відфільтрованими рядками.")
        else:
            print("Не знайдено жодного рядка, що містить ключове слово.")
    except Exception as e:
        print("Сталася помилка під час запису у файл:", str(e))

def filter_file(keyword: str, filepath: str):
    """
    Фільтрує вміст файлу за ключовим словом та записує результат у файл "filtered.txt" на робочому столі.
    :param keyword: Ключове слово для фільтрації рядків.
    :param filepath: Шлях до файлу, що підлягає фільтрації.
    """
    lines = read_file(filepath)
    if lines:
        filtered_lines = filter_lines(lines, keyword)
        write_filtered_lines(filtered_lines)



if __name__ == "__main__":
    keyword = input("Введіть ключове слово: ")
    filepath = input("Введіть шлях до файлу: ")

    filter_file(keyword, filepath)
