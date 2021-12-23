from datetime import datetime, timedelta
import calendar

def is_date(date: str) -> bool:
    try:
        true_date = datetime.strptime(date, "%Y%m%d")
    except ValueError:
        return False
    return True

def add_days(date: str, days: int) -> str:
    return (datetime.strptime(date, "%Y%m%d") + timedelta(days=days)).strftime("%Y%m%d")

def tomorrow(date: str) -> str:
    return (datetime.strptime(date, "%Y%m%d") + timedelta(days=1)).strftime("%Y%m%d")

def yesterday(date: str) -> str:
    return (datetime.strptime(date, "%Y%m%d") + timedelta(days=-1)).strftime("%Y%m%d")

def add_weeks(date: str, weeks: int) -> str:
    return (datetime.strptime(date, "%Y%m%d") + timedelta(weeks=weeks)).strftime("%Y%m%d")

def add_months(date: str, months: int) -> str:
    true_date = datetime.strptime(date, "%Y%m%d")
    month = true_date.month - 1 + months
    year = true_date.year + month // 12
    month = month % 12 + 1
    day = min(true_date.day, calendar.monthrange(year, month)[1])
    return datetime(year, month, day).strftime("%Y%m%d")

def add_years(date: str, years: int) -> str:
    return add_months(date, years * 12)
