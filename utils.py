from datetime import date, datetime

from constants import DATE_FORMAT_STRING, MONTH_DAY_FORMAT_STRING


def convert_date_to_str(d: date):
    return d.strftime(DATE_FORMAT_STRING)


def convert_date_to_month_day_str(d: date):
    return d.strftime(MONTH_DAY_FORMAT_STRING)


def convert_str_to_date(d_str: str):
    return datetime.strptime(d_str, DATE_FORMAT_STRING).date()
