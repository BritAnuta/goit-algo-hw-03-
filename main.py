# # 1 Перше завдання

# import datetime

# def get_days_from_today(date):
#     try:
#         # Парсинг рядка в об'єкт datetime
#         date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
#         # Отримання поточної дати
#         current_date = datetime.datetime.today().date()
#         # Рахування різниці в днях
#         difference = (date_obj.date() - current_date).days
#         return difference
#     except Exception:
#         return "Формат дати введено некоректно"
# # Отримання дати від користувача
# user_date = input("Введіть дату у форматі YYYY-MM-DD: ")
# # Отримання і вивід резутьтату
# result = get_days_from_today(user_date)
# print("Кількість днів між заданою датою і поточною датою:", result)


# # Друге завдання

# import random

# def get_numbers_ticket(min, max, quantity):
#  # Встановлюємоємо умови, що повернуть пустий рядок і помилку
#     if (min < 1) or (max > 1000) or (min > max) or (quantity > (max - min + 1)) or (quantity < 1):
#         print('Дані введені некоректно')
#         return []
    
#     numbers = random.sample(range(min, max+1), quantity) # Вибираємо рандомні числа
#     return sorted(numbers)                               # Сортуємо їх
# # Просимо користувача ввести межі, з яких будуть вибрана введена кількість чисел
# min = int(input("Введіть мінімальне число для рендера від 1-1000: "))
# max = int(input("Введіть максимальне число для рендера від 2-1000: "))
# quantity = int(input("Введіть кількість чисел для рендера: "))
        
# # Одержуємо і виводимо результат
# lottery_numbers = get_numbers_ticket(min, max, quantity)
# print('Ваші лотерейні числа:',lottery_numbers)


# Третє завдання



