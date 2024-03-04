# # ~ Перше завдання ~

# def total_salary(path):
    
#     # Створюємо обробку помилки відсутності файлу або помилки читання

#     try:
#         with open ("path.txt", "r", encoding='utf-8') as list: # Коректно відкриваємо наш текстовий файл
#             lines = list.readlines() # Читаємо по рядках
#             total_salary = 0 # Створюємо значення загальної зарплатні

#             for coleg in lines:
#                 name, salary_str = coleg.split(',') # Розбиваємо наші дані по комі
#                 salary = int(salary_str) # Переводимо строку у число
#                 total_salary += salary # Додаємо усі зарплатні зі списку і отримуємо загальну зарплатню
        
#             num_people = len(lines) # Розраховуємо кількість людей зі списка
#             average_salary = total_salary // num_people # Розраховуємо середню зарплатню
#             return total_salary, average_salary   # Повертаємо наші значення

#     except Exception:
#         print("Не вдалося знайти файл зі списком колег") # Виведеться при помилці

# total, average = total_salary("path.txt") # Визиваємо нашу функцію
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# # ~ Друге завдання ~

# def get_cats_info(path):

#     cats_list = [] # Створюємо порожній список, куди будуть повертатись наші словнички 

#     # Створюємо обробку можливості помилки
#     try:
#         with open (path, "r", encoding='utf-8') as file: # Корректно відкриваємо файл

#             # За допомогою циклу пробігаємось по нашому текстовому файлу
#             for line in file:
#                 cat_info = line.strip().split(',') # Розбиваємо наші дані по комі, виключаючи можливість непотрібних пробілів
#                 cat_dict = {"id": cat_info[0], "name": cat_info[1], "age": int(cat_info[2]) } # Створюємо словник з елементами інформації

#                 cats_list.append(cat_dict) # Додаємо у наш список усі словнички з інформацією

#     # Якщо буде помилка, то видасть яка саме і поверне порожній список    
#     except Exception as e:
#         print("Помилка:", e)
#         return cats_list
    
#     return cats_list # Повертаємо значення у наш список

# cats_list = get_cats_info("Cats.txt") # Викликаємо нашу функцію, яка зчитує значення з нашого текстового файлу

# # Виводимо результат так, щоб кожний словничок з інформацією кота був на новому рядку
# for cat in cats_list:
#     print(cat)

# ~ Четвертє завдання ~

# Парсимо рядок, що вводить користувач
def parse_input(user_input):
    cmd, *args = user_input.split() # розбиваємо на команду і аргументи по пробілу
    cmd = cmd.strip().lower() # прибираємо зайві пробіли і текст команди приводимо до нижньго регістру
    return cmd, *args

# Прописуємо фунцію, що буде додавати нові контакти
def add_contact(args, contacts):
    name, phone = args # аргументи розбиваємо на ім'я та номер
    contacts[name] = phone # додаємо у словник контакт, ім'я - ключ, номер - значення
    return "Contact added."

# Прописуємо фунцію, що буде змінювати номер контакта, який вже є
def change_contact(args, contacts):
     # Обробляємо помилку, якщо користувач запросив неіснуючий контакт
    if args[0] in contacts.keys(): # перевіряємо наявність контакту за ім'ям
        add_contact(args, contacts) # якщо є, визиваємо функцію додавання номера
        return "Contact changed."
    else:
        return "Contact is not found" # якщо немає - поверне і виведе цю інформацію   
    
# Прописуємо фунцію, що буде показувати номер контакту за запросом користувача    
def show_contact(args, contacts):
    # Обробляємо помилку, якщо користувач запросив неіснуючий контакт
    try:
        args[0] in contacts.keys() # перевіряємо наявність контакту
        return contacts[args[0]]
    except Exception:
        return "Contact is not found" # якщо немає - поверне і виведе цю інформацію

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


