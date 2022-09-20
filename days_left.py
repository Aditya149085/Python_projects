import datetime
def days_in_month():
    """
    This module initiates the days in th current month and tells ho many days is left to end of month
    """
    now = datetime.datetime.now()
    td = 0
    if now.year / 400 ==0 or now.year/4 == 0 and now.year/100 != 0:
        if now.month == 2:
            td = 29
        td =28
    if now.month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        td = 31
    elif now.month == 4 or 6 or 9 or 11:
        td = 30
    days_left = abs(now.day-td)
    return days_left
answer = days_in_month()
print(answer)