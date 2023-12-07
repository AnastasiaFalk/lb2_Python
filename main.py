from builtins import int, input, print, ValueError, abs, range, len, map


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

def input_date():
    while True:
        try:
            date_str = input("Введіть дату у форматі 'дд/мм/рррр': ")
            day, month, year = map(int, date_str.split('/'))

            if not (1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 2023):
                raise ValueError("Дата введена неправильно")

            return Date(day, month, year)
        except ValueError as e:
            print(f"{e}. Будь ласка, введіть знову.")

def format1_date(date):
    return f"{date.day:02d}/{date.month:02d}/{date.year}"

def format2_date(date):
    return f"{date.year:04d}-{date.month:02d}-{date.day:02d}"

def days_difference(date1, date2):
    days1 = date1.year * 365 + date1.month * 30 + date1.day
    days2 = date2.year * 365 + date2.month * 30 + date2.day
    return abs(days1 - days2)

def insertion_sort(dates):
    for i in range(1, len(dates)):
        current_date = dates[i]
        j = i - 1
        while j >= 0 and dates[j].year < current_date.year:
            dates[j + 1] = dates[j]
            j -= 1
        dates[j + 1] = current_date

# Запитайте користувача про першу дату
date1 = input_date()

# Запитайте користувача про другу дату
date2 = input_date()

# Виведіть форматовані дати
print("Перша дата (дд/мм/рррр): ", format1_date(date1))
print("Друга дата (дд/мм/рррр): ", format1_date(date2))

print("Перша дата (рррр-мм-дд): ", format2_date(date1))
print("Друга дата (рррр-мм-дд): ", format2_date(date2))

# Обчисліть та виведіть кількість днів між датами
difference = days_difference(date1, date2)
print(f"Кількість днів між датами: {difference} дн.")

# Створіть список дат і відсортуйте його за спаданням
dates = [date1, date2]
insertion_sort(dates)

print("Відсортовані дати за спаданням:")
for date in dates:
    print(format1_date(date))