from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    birthdays_by_day = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")

        if delta_days >= 7 and (birthday_weekday == "Saturday" or birthday_weekday == "Sunday"):
            delta_days -= (delta_days // 7) * 7

        birthdays_by_day[(today + timedelta(days=delta_days)).strftime("%A")].append(name)

    for day, names in birthdays_by_day.items():
        print(f"{day}: {', '.join(names)}")

test_users = [
    {"name": "Anton B", "birthday": datetime(1999, 11, 29)},
    {"name": "Igor D", "birthday": datetime(1988, 11, 26)},
]

get_birthdays_per_week(test_users)