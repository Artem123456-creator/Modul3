from datetime import datetime, timedelta  # Імпорт класів datetime та timedelta для роботи з датами і часом

users = [  # Список користувачів з їхніми датами народження
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith1", "birthday": "1990.03.05"},
    {"name": "Sara Konor", "birthday": "1990.03.05"},
    {"name": "David Redlklif", "birthday": "1990.03.12"},
    {"name": "Rupert Green", "birthday": "1990.03.13"},
    {"name": "Emma Yotson", "birthday": "1990.03.10"},
    {"name": "Bilbo Beggins", "birthday": "1990.03.9"},
]

def find_next_weekday(d, weekday: int):  # Функція для знаходження наступного заданого дня тижня після заданої дати
    days_ahead = weekday - d.weekday()  # Різниця між заданим днем тижня та днем тижня заданої дати
    if days_ahead <= 0:  # Якщо день народження вже минув
        days_ahead += 7  # Додаємо 7 днів, щоб отримати наступний тиждень
    return d + timedelta(days=days_ahead)  # Повертаємо нову дату


def prepared(users):
    prepared_users = []  # Список підготовлених користувачів
    for user in users:  # Ітерація по кожному користувачеві зі списку
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  # Парсимо дату народження
            prepared_users.append({"name": user['name'], 'birthday': birthday})  # Додаємо користувача з підготовленою датою народження
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')  # Виводимо повідомлення про помилку
    return prepared_users


def get_upcoming_birthdays(users):
    days = 7  # Кількість днів для перевірки на наближені дні народження
    today = datetime.today().date()  # Поточна дата
    upcoming_birthdays = []  # Список майбутніх днів народження
    for user in prepared(users):  # Ітерація по підготовленим користувачам
        birthday_this_year = user["birthday"].replace(year=today.year)  # Заміна року на поточний для дня народження цього року

        if birthday_this_year < today:  # Якщо дата народження вже пройшла цього року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  # Переносимо наступний рік

        if 0 <= (birthday_this_year - today).days <= days:  # Якщо день народження в межах вказаного періоду
            if birthday_this_year.weekday() >= 5:  # Якщо день народження випадає на суботу або неділю
                birthday_this_year = find_next_weekday(birthday_this_year, 0)  # Знаходимо наступний понеділок

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')  # Форматуємо дату у рядок
            upcoming_birthdays.append({  # Додаємо дані про майбутній день народження
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
    return(upcoming_birthdays)  # Виводимо список майбутніх днів народження

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)