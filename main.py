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

if __name__ == "__main__":
    keyword = input("Введіть ключове слово: ")
    filepath = input("Введіть шлях до файлу: ")

    #filter_file(keyword, filepath)
