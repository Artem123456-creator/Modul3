from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        now = datetime.today()
        difference = now - date
        return difference.days
    except ValueError:
        print ("Try again, it must be date format")

d = get_days_from_today("2020-10-09")
d_2 = get_days_from_today("2024-10-09")
print(d,"\n", d_2)