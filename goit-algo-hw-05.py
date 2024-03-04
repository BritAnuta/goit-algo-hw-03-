# ~ Перше завдання ~

def caching_fibonacci(): # Створюємо зовнішню функцію
    cache = {} # Також словничок, в якому будуть зберігатися наші дані

    def fibonacci(n): # Створюємо внутрішню функцію
        if n <= 0:  # Перевіряємо умови і 0 та 1 просто повертаємо
            return 0
        elif n == 1:
            return 1
        elif n in cache: # Перевіряємо, чи є наша n у кеші і повертаємо значення, якщо є
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)  # Ведемо розрахунок для кожного елемента і повертаємо результат
        return cache[n]
    
    return fibonacci # Повертаємо внутрішню функцію

fib = caching_fibonacci() # Викликаємо зовнішню функцію
print(fib(10)) # Виводимо результати чисел Фібоначчі для 10 та 15
print(fib(15))

# ~ Друге завдання ~

from typing import Callable
from functools import reduce
import re


def generator_numbers(text: str): # Створюємо функцію, що приймає рядок як аргумент
    pattern = r"\d+(\.\d+)?" # Створюємо шаблон регексу, щоб знайти в тексті всі числа і дійсні числа
    for numbers in map(float, filter(lambda x: re.findall(pattern,x), text.split(" "))): # Обробляємо в тексті усі числа за допомогою цикла
        yield numbers # Повертаємо генератор, що ітерує по всіх дійсних числах у тексті

def sum_profit(text: str, func: Callable): # Створюємо функцію, що використовує generator_numbers, в якій буде обчислюватись сума чисел
    sum = reduce(lambda x,y: x+y, func(text)) # Розраховуємо суму чисел, які повертає функція func
    return sum # Повертаємо результат

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers) # Викликаємо функцію
print(f"Загальний дохід: {total_income}") # Виводимо результат

# ~ Четвертє завдання ~

# Створюємо декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs): # Створюємо внутрішню функцію, яка буде замінювати функцію, яку декоруємо
        # Створюємо обробку помилок
        try:
            return func(*args, **kwargs) # Якщо виконання функції проходить без помилок, то повертаємо результат
        except (KeyError, ValueError, IndexError) as e: # При виникненні якогось з цих винятків, виконається наступний блок
            print(f"Input error: {e}") # Виведемо інформацію про виняток
            if isinstance(e, KeyError): # Якщо буде виняток KeyError, виведеться наступний текст
                print("Enter user name please")
            elif isinstance(e, ValueError): # Якщо буде виняток ValueError, виведеться наступний текст
                print("Give me name and phone please")
    return inner # Повертаємо внутрішню функцію

# Тепер огортаємо у наш декоратор кожну функцію обробки команд
@input_error
# Парсимо рядок, що вводить користувач
def parse_input(user_input):
    cmd, *args = user_input.split() # розбиваємо на команду і аргументи по пробілу
    cmd = cmd.strip().lower() # прибираємо зайві пробіли і текст команди приводимо до нижньго регістру
    return cmd, *args

@input_error
# Прописуємо фунцію, що буде додавати нові контакти
def add_contact(args, contacts):
    name, phone = args # аргументи розбиваємо на ім'я та номер
    contacts[name] = phone # додаємо у словник контакт, ім'я - ключ, номер - значення
    return "Contact added."

@input_error
# Перевіряємо фунцію, що буде змінювати номер контакта, який вже є
def change_contact(args, contacts):
    if args[0] in contacts.keys(): # перевіряємо наявність контакту за ім'ям
        add_contact(args, contacts) # якщо є, визиваємо функцію додавання номера
        return "Contact changed."
    else:
        return "Contact is not found" # якщо немає - поверне і виведе цю інформацію   

@input_error    
# Прописуємо фунцію, що буде показувати номер контакту за запросом користувача    
def show_contact(args, contacts):
    args[0] in contacts.keys() # перевіряємо наявність контакту
    return contacts[args[0]]
 
@input_error
# Прописуємо фунцію, що буде показувати всі контакти, які ми додали
def all_contacts(args, contacts):
    a_c='' # створюємо порожній рядок для збереження інформації
    for key in contacts:
        a_c+=(f"{key:15} : {contacts[key]}\n") # проходимося циклом по всіх ключах у словнику і додаємо їх у а_с в форматі "ім'я  : номер"
    return a_c

# CLI-бот
def main():
    contacts = {} # створюємо порожній словник для контактів
    print("Welcome to the assistant bot!")
    # Створюємо нескінчений цикл для очікування команд від користувача
    while True:
        user_input = input("Enter a command: ") # отримання вводу користувача
        command, *args = parse_input(user_input) # визиваємо функцію парсингу

        # Прописуємо умови введення команд користувачем і дії нашої програми
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(all_contacts(args, contacts))    
        else:
            print("Invalid command.")

if __name__ == "__main__": # перевіряємо, чи визивається запуск скрипта безпосередньо
    main()

