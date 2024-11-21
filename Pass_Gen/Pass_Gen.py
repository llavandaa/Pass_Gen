import random
import string
import os
from typing import Generator
from tqdm import tqdm  # pip install tqdm (если не установлена)


# Генератор паролей заданной длины
def generate_pass(length: int = 6) -> Generator[str, None, None]:
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/~'
    characters = string.ascii_letters + string.digits + special_chars

    while True:
        # Генерация пароля заданной длины
        password = ''.join(random.choice(characters) for _ in range(length))
        yield password

# Записывает пароли в файл с отображением прогресса + обработка ошибки записи
def to_file(passwords: Generator[str, None, None], filename: str, count: int) -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for _ in tqdm(range(count), desc="Генерация паролей", unit="пароль"):
                file.write(next(passwords) + '\n')
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

# Проверка на корректное число
def get_positive_integer(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Число должно быть положительным.")
            else:
                return value
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")

def main():
    # Получение параметров генерации паролей от пользователя
    password_length = get_positive_integer('Введите необходимую длину пароля: ')
    number_of_passwords = get_positive_integer('Введите количество паролей для генерации: ')
    
    # Запрос пути к файлу для сохранения паролей
    filename = input('Введите путь к файлу для сохранения паролей (например, C:\\path\\to\\file\\pass.txt): ')

    # Проверка существования директории
    directory = os.path.dirname(filename)
    if not os.path.exists(directory) and directory != '':
        print("Указанная директория не существует.")
        return

    if password_length <= 0 or number_of_passwords <= 0:
        print("Длина пароля и количество паролей должны быть положительными числами.")
        return

    # Генерация и запись паролей в файл
    passwords = generate_pass(password_length)
    to_file(passwords, filename, number_of_passwords)

    print(f'{number_of_passwords} сгенерированных паролей записано в файл {filename}.')

if __name__ == "__main__":
    main()
