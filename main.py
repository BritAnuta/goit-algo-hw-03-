# ~ 1 Перше завдання ~

import datetime

def get_days_from_today(date):
    try:
        # Парсинг рядка в об'єкт datetime
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        # Отримання поточної дати
        current_date = datetime.datetime.today().date()
        # Рахування різниці в днях
        difference = (date_obj.date() - current_date).days
        return difference
    except Exception:
        return "Формат дати введено некоректно"
# Отримання дати від користувача
user_date = input("Введіть дату у форматі YYYY-MM-DD: ")
# Отримання і вивід резутьтату
result = get_days_from_today(user_date)
print("Кількість днів між заданою датою і поточною датою:", result)


# ~ Друге завдання ~
# Зробила трошки іншим способом

import random

def get_numbers_ticket(min, max, quantity):
 # Встановлюємоємо умови, що повернуть пустий рядок і помилку
    if (min < 1) or (max > 1000) or (min > max) or (quantity > (max - min + 1)) or (quantity < 1):
        print('Дані введені некоректно')
        return []
    
    numbers = random.sample(range(min, max+1), quantity) # Вибираємо рандомні числа
    return sorted(numbers)                               # Сортуємо їх
# Просимо користувача ввести межі, з яких будуть вибрана введена кількість чисел
min = int(input("Введіть мінімальне число для рендера від 1-1000: "))
max = int(input("Введіть максимальне число для рендера від 2-1000: "))
quantity = int(input("Введіть кількість чисел для рендера: "))
        
# Одержуємо і виводимо результат
lottery_numbers = get_numbers_ticket(min, max, quantity)
print('Ваші лотерейні числа:',lottery_numbers)


# ~ Третє завдання ~

# Створюємо функцію
def normalize_phone(phone_numbers):
    intab = "'()[]-/*_ "  # Вказуємо символи, включаючи пробіл, які хочемо видалити з ненормалізованих номерів
    normalized_numbers = []  # Створюємо пустий список, щоб у нього вводилися вже нормалізовані номери з циклу

    # Створюємо цикл, в якому видаляються всі непотрібні символи і перевіряються умови кількості символів у безсимвольному номері
    for phone_number in phone_numbers:
        trantab = phone_number.maketrans('', '', intab)
        num_no_sings = phone_number.translate(trantab)

        if len(num_no_sings) == 10:
            normalized_numbers.append('+38' + num_no_sings)
        elif len(num_no_sings) == 11:
            normalized_numbers.append('+3' + num_no_sings)
        elif len(num_no_sings) == 12:
            normalized_numbers.append('+' + num_no_sings)
        else:
            normalized_numbers.append(num_no_sings)
    
    # Повертаємо нормалізовані номера у вигляді списку
    return normalized_numbers

result = normalize_phone(["    +38(050)123-32-34", "     0503451234", "(050)8889900", "38050-111-22-22", "38050 111 22 11   "])
print("Нормалізовані номери телефонів для SMS-розсилки:", result)


# ~ Четвертє завдання ~

from datetime import datetime
from datetime import timedelta
from datetime import date

# Вводимо наш список колег з датами днів народжень
users = [ 
    {"name": "John Doe", "birthday": "1985.02.04"}, 
    {"name": "Jane Smith", "birthday": "1990.01.31"},
    {"name": "Lina Wulf", "birthday": "1989.01.28"}
]

# Створюємо функцію
def get_upcoming_birthdays(users = None):
    today_date = datetime.today().date() # Визначаємо сьогоднішню дату без часу
    birthdays = [] # Створюємо список, куди будуть повертатися результати

    # Починаємо перебирати дані зі списку колег
    for user in users:
        birthday_date = user["birthday"]
        birthday_date = datetime.strptime(birthday_date, "%Y.%m.%d").date() # Парсинг дати народження колег зі строки у формат дати
        birthday_date_today = birthday_date.replace(year = today_date.year) # Змінюємо рік дня народження на поточний
        
        day_of_week = birthday_date_today.isoweekday() # Знаходимо номер тижня дня народження колеги у цьому році
        
        # Розраховуємо різницю між цьогорічним днем народження і поточною датою
        days_between = (birthday_date_today - today_date).days
        
        # Перевіряємо умову, чи є на цьому тижні чийсь день народження
        if 0 <= days_between <= 7:
        
            # Перевіряємо умову, якщо дата випадає на суботу
            if day_of_week == 6:
                congratulation_date = birthday_date_today + timedelta(days=2)
                birthdays.append({'name':user['name'], 'birthday':(congratulation_date).strftime("%Y.%m.%d")})
            
            # Перевіряємо умову, якщо дата випадає на неділю
            elif day_of_week == 7:
               congratulation_date = birthday_date_today + timedelta(days=1)
               birthdays.append({'name':user['name'], 'birthday':(congratulation_date).strftime("%Y.%m.%d")})
            
            # Якщо дата просто на цьому тижні, і не припадає на суботу та неділю
            else:
                congratulation_date = birthday_date_today
                birthdays.append({'name':user['name'], 'birthday':(congratulation_date).strftime("%Y.%m.%d")})
  
        # Якщо дата народження вже пройшла, переносимо вітання на наступний рік
        elif date(today_date.year, 1, 1) <= birthday_date_today < today_date:
            congratulation_date = birthday_date_today.replace(year = birthday_date_today.year + 1)
            birthdays.append({'name':user['name'], 'birthday':(congratulation_date).strftime("%Y.%m.%d")})
        
        # Якщо дата народження більша за тиждень, повернеться пустий список
        
    return birthdays
        

print(get_upcoming_birthdays(users))