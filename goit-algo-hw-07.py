from collections import UserDict
from datetime import datetime, timedelta
import re

# Створюємо базовий клас із загальними характеристиками полів
class Field:
    def __init__(self, value): # ініціалізуємо
        self.value = value # встановлюємо значення атрибута для об'єкта класу

    def __str__(self): # визначаємо метод для рядкового представлення об'єкта класу Field
        return str(self.value) # повертаємо рядкове значення value

# Визначаємо класи Name, Phone, Birthday
class Name(Field):
    pass

class Phone(Field):
    pass

class Birthday:
    def __init__(self, day, month, year): # ініціалізуємо класс Birthday з днем, місяцем і роком
        self.day = day
        self.month = month
        self.year = year

    def __str__(self): # визначаємо метод для рядкового представлення об'єкта класу Birthday
        return f"{self.day}.{self.month}.{self.year}"

# Створюємо класс, що буде представляти запис в адресній книзі
class Record:
    def __init__(self, name): # ініціалізуємо об'єкт класу Record із заданим ім'ям
        self.name = Name(name) # створюємо об'єкт класу Name і зберігаємо його в атрибуті name
        self.phones = [] # порожній список для зберігання об'єктів класу Phone
        self.birthday = None # створюємо поле для дня народження в класі Record

    def add_phone(self, phone): # визначаємо метод, який буде додавати новий номер телефону
        if re.match(r'^\d{10}$', phone): # прописуємо умову за допомогою регулярного вираза для валідації номеру до 10 цифр
            self.phones.append(Phone(phone))
        else:
            print("Enter 10-digit number, please")

    def edit_phone(self, old_phone, new_phone): # визначаємо метод, який буде редагувати існуючий номер телефону
        for index, phone in enumerate(self.phones): # циклом пройдемося по всіх номерах у списку phones
            if phone.value == old_phone: # перевіримо співпадіння значення поточного і старого номера
                if re.match(r'^\d{10}$', new_phone): # прописуємо умову за допомогою регулярного вираза для валідації номеру до 10 цифр
                    self.phones[index] = Phone(new_phone) # і якщо є співпадіння, змінюємо на новий номер
                else:
                    print("Enter 10-digit number, please")
                return
            
    def find_phone(self, phone): # визначаємо метод, який буде шукати номер телефону в записі
        for ph in self.phones:
               if ph.value == phone:
                      return ph

    def __str__(self): # Визначаємо метод для рядкового представлення об'єкта класу Record
        # Повертаємо рядок, що містить ім'я запису, номер телефону та день народження
        return f"Contact name: {self.name.value}, phone: {'; '.join(str(p) for p in self.phones)}, birthday: {self.birthday}"

# Створюємо клас, що успадковується від UserDict і представлятиме адресну книгу
class AddressBook(UserDict):
    def add_record(self, record): # визначаємо метод, який буде додавати новий запис до адресної книги
          self.data[record.name.value] = record

    def find(self, name): # визначаємо метод, який буде шукати запис за ім'ям у адресній книзі
          return self.data.get(name)

# Створюємо декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs): # Створюємо внутрішню функцію, яка буде замінювати функцію, яку декоруємо
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            print(f"Input error: {e}")
            if isinstance(e, KeyError):
                print("Enter user name, please")
            elif isinstance(e, ValueError):
                print("Give me name and phone, please")
    return inner

# Тепер огортаємо у наш декоратор кожну функцію обробки команд
@input_error
def parse_input(user_input): # парсимо рядок, що вводить користувач
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Прописуємо фунцію, що буде додавати нові контакти
@input_error
def add_contact(args, book):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."

# Прописуємо фунцію, що буде змінювати номер контакта, який вже є
@input_error
def change_contact(args, book):
    name, new_phone = args
    record = book.find(name)
    if record: # додаємо умови наявності контакту
        record.edit_phone(record.phones[0].value, new_phone)
        return "Contact changed."
    else:
        return "Contact is not found."

# Прописуємо фунцію, що буде показувати номер контакту за запросом користувача
@input_error
def show_contact(args, book):
    name = args[0]
    record = book.find(name)
    if record: # додаємо умови наявності контакту
        return str(record)
    else:
        return "Contact is not found."

# Прописуємо фунцію, що буде показувати всі контакти, які ми додали
@input_error
def all_contacts(book):
    all_info = ""
    for record in book.values():
        all_info += str(record) + "\n"
    return all_info

# Прописуємо фунцію, що буде додавати день народження контакта за іменем
@input_error
def add_birthday(args, book):
    name, *birthday = args
    day, month, year = birthday[0].split('.')
    record = book.find(name)
    if record: # додаємо умови наявності контакту
        record.birthday = Birthday(day, month, year)
        return "Birthday added."
    else:
        return "Contact is not found."

# Прописуємо фунцію, що буде відображати день народження контакта за іменем
@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record: # додаємо умови наявності контакту і дня народження
        if record.birthday:
            return f"{record.name.value}'s birthday is {record.birthday}"
        else:
            return f"{record.name.value} doesn't have a birthday set."
    else:
        return "Contact is not found."

# Прописуємо фунцію, що буде відображати наближені дні народження контактів за іменами
@input_error
def birthdays(args, book):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    upcoming_birthdays = []
    for record in book.values():
        if record.birthday: # додаємо умови наявності дня народження
            # створюємо об'єкт datetime зі значеннями поточного року та місяця і дня народження
            birthday_date = datetime(today.year, int(record.birthday.month), int(record.birthday.day)).date()
            if today <= birthday_date <= next_week: # додаємо умову попадання дня народження у діапазон тижня
                upcoming_birthdays.append((record.name.value, birthday_date))
    if upcoming_birthdays: # додаємо умови наявності наближених днів народження
        result = "Upcoming birthdays in the next week:\n"
        for name, birthday_date in upcoming_birthdays:
            result += f"{name}: {birthday_date.strftime('%d.%m')}\n" # додаємо ім'я та дату народження до рядка результату
        return result
    else:
        return "No upcoming birthdays in the next week."

# CLI-бот
def main():
    book = AddressBook() # створюємо екземпляр класу AddressBook і присвоюємо його змінній book
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        # Прописуємо умови введення команд користувачем і дії нашої програми
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_contact(args, book))
        elif command == "all":
            print(all_contacts(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__": # перевіряємо, чи визивається запуск скрипта безпосередньо
    main()