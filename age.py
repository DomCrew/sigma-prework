import datetime
today = datetime.date.today()

def ask_for_input():
    date = input("Enter your date: ")
    return date
def calculate_age(date):
    year, month, day = date.split("-")
    years = today.year - int(year) - 1
    if int(month) <= today.month and int(day) <= today.day:
        years += 1
    print(years)

date = ask_for_input()
calculate_age(date)