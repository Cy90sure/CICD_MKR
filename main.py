import os

def get_desktop_path() -> str:
    """
    Повертає шлях до робочого столу користувача.
    """
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')



if __name__ == "__main__":
    keyword = input("Введіть ключове слово: ")
    filepath = input("Введіть шлях до файлу: ")

    #filter_file(keyword, filepath)
