import secrets
import string
import os
import tkinter as tk
from tkinter import messagebox, filedialog
from typing import List

# Генератор паролей заданной длины
def generate_pass(length: int, count: int) -> List[str]:
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/~'
    characters = string.ascii_letters + string.digits + special_chars
    # Генерация списка паролей
    passwords = [''.join(secrets.choice(characters) for _ in range(length)) for _ in range(count)]
    return passwords

# Записывает пароли в файл с обработкой ошибки записи
def to_file(passwords: List[str], filename: str) -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(passwords))
        messagebox.showinfo("Успех", f'{len(passwords)} сгенерированных паролей записано в файл {filename}.')
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при записи в файл: {e}")

# Функция для обработки нажатия кнопки "Сгенерировать"
def generate_passwords():
    try:
        password_length = int(length_entry.get())
        number_of_passwords = int(count_entry.get())
        filename = file_path.get()

        # Проверка на положительные значения
        if password_length <= 0 or number_of_passwords <= 0:
            messagebox.showwarning("Предупреждение", "Длина пароля и количество паролей должны быть положительными числами.")
            return

        # Проверка существования директории
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            messagebox.showwarning("Предупреждение", "Указанная директория не существует.")
            return

        # Генерация и запись паролей в файл
        passwords = generate_pass(password_length, number_of_passwords)
        to_file(passwords, filename)

        # Очистка полей ввода после успешной генерации
        length_entry.delete(0, tk.END)
        count_entry.delete(0, tk.END)
        file_path.set('')

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные целые числа.")

# Функция для выбора файла сохранения
def select_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        file_path.set(filename)

# Создание основного окна приложения
root = tk.Tk()
root.title("Passwd Generator")  # Заголовок окна

# Переменные для хранения данных ввода
file_path = tk.StringVar()

# Создание интерфейса
tk.Label(root, text="Длина пароля:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Количество паролей:").grid(row=1, column=0, padx=10, pady=10)
count_entry = tk.Entry(root)
count_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Путь к файлу:").grid(row=2, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, textvariable=file_path)
file_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Выбрать файл", command=select_file).grid(row=2, column=2, padx=10, pady=10)
tk.Button(root, text="Generate!", command=generate_passwords).grid(row=3, columnspan=3, padx=10, pady=20)

# Запуск основного цикла приложения
root.mainloop()
