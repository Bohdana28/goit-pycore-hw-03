from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users) :
    today = datetime.today().date()
    congratulations = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
           birthday_this_year = birthday_this_year.replace(year=today.year+1)

        difference_of_days = (birthday_this_year - today).days
        if 0<= difference_of_days <=7 :
            if birthday_this_year.weekday() in (5,6):
                days_to_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year +timedelta(days=days_to_monday)
            else:
                congratulation_date = birthday_this_year
            
            congratulations.append({"name": user['name'],"congratulation_date":congratulation_date.strftime("%Y.%m.%d")})
        
    return congratulations
    
users = [
    {"name": "Олег", "birthday": "1990.06.14"},
    {"name": "Ірина", "birthday": "1992.06.15"},
    {"name": "Аня", "birthday": "1995.06.16"},
    {"name": "Петро", "birthday": "1987.06.23"},  
]


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

