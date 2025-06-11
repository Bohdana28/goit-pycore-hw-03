from datetime import datetime

def get_days_from_today(date_string) :
    try:
        datetime_object = datetime.strptime(date_string, "%Y-%m-%d") 
        now_date = datetime.today()
        difference = datetime_object.date() - now_date.date()
        return difference
    except ValueError:
        print("This isn't a right form of data, try YYYY-MM-DD!")

print(get_days_from_today("2025-06-22"))
print(get_days_from_today("2025-06-10"))
print(get_days_from_today("10 June 2025"))