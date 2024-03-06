from collections import UserDict

# Створюємо базовий клас із загальними характеристиками полів
class Field:
    def __init__(self, value): # ініціалізуємо
        self.value = value # встановлюємо значення атрибута для об'єкта класу

    def __str__(self): # визначаємо метод для рядкового представлення об'єкта класу Field
        return str(self.value) # повертаємо рядкове значення value

# Визначаємо класи Name і Phone, які успадкуються від класу Field
class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    # реалізація класу
		pass

# Створюємо класс, що буде представляти запис в адресній книзі
class Record:
    def __init__(self, name): # ініціалізуємо об'єкт класу Record із заданим ім'ям
        self.name = Name(name) # створюємо об'єкт класу Name і зберігаємо його в атрибуті name
        self.phones = [] # порожній список для зберігання об'єктів класу Phone

    def add_phone(self, phone): # визначаємо метод, який буде додавати новий ноиер телефону
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone): # визначаємо метод, який буде редагувати існуючий номер теелфону
        for index, phone in enumerate(self.phones): # циклом пройдемося по всіх номерах у списку phones
               if phone.value == old_phone: # перевіримо співпадіння значення поточного і старого номера
                      self.phones[index] = Phone(new_phone) # і якщо є співпадіння, змінюємо на новий номер

    def find_phone(self, phone): # визначаємо метод, який буде шукати номер телефону в записі
        for ph in self.phones: # циклом пройдемося по всіх номерах у списку phones
               if ph.value == phone: # перевіримо співпадіння значення поточного номера із шуканим
                      return ph # і якщо є співпадіння, повертаємо

    # реалізація класу

    def __str__(self): # Визначаємо метод для рядкового представлення об'єкта класу Record
        # Повертаємо рядок, що містить ім'я запису та всі його номери через ";"
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

 # Створюємо клас, що успадковується від UserDict і представлятиме адресну книгу
class AddressBook(UserDict):
    def add_record(self, record): # визначаємо метод, який буде додавати новий запис до адресної книги
          self.data[record.name.value] = record # додаємо запис до словника адресної книги, де ім'я буде ключем

    def find(self, name): # визначаємо метод, який буде шукати запис за ім'ям у адресній книзі
          return self.data.get(name) # повертаємо запис із заданим ім'ям зі словника
    
    def delete(self, name): # визначаємо метод, який буде видаляти запис з адресної книги за ім'ям
          if name in self.data: # перевіримо існування запису у адресній книзі
            del self.data[name] # і якщо є, видаляємо його зі словника



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")