from datetime import datetime, timedelta


def days_until_end_of_month() -> int:
    today = datetime.today()
    end_of_month = datetime(today.year, today.month + 1, 1) - timedelta(days=1)
    days_left = (end_of_month - today).days
    print(f"До кінця місяця залишилося {days_left} днів")
    return days_left


def days_until_end_of_week() -> int:
    today = datetime.now()
    end_of_week = today + timedelta(days=(6 - today.weekday()))
    days_left = (end_of_week - today).days
    print(f"До кінця тижня залишилося {days_left} днів")
    return days_left
