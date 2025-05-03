month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """

    :param year:
    :return: if year is leap year or not.
    """
    return year % 4 == 0  and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year,month):
    if month <= 0 or month > 12:
        print("Invalid Month")

    elif month == 2 and is_leap(year):
        print("Days in the month 29")

    else:
        days = month_days[month]
        print("Days in the month: {}".format(days))


days_in_month(2004,2)
