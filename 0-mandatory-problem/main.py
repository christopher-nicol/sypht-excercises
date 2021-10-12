start_date = str(input('Enter start date (in DD/MM/YYYY format): '))
end_date = str(input('Enter end date (in DD/MM/YYYY format): '))

# Destructures the start and end dates into separate variables for their day, month and year
start_day, start_month, start_year = map(int, start_date.split('/'))
end_day, end_month, end_year = map(int, end_date.split('/'))

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    """
    Returns whether a year is a leap year
        - Leap years are any year that can be exactly divided by 4
        - Except if it can be divided exactly by 100 then it isn't
        - But if it can be divided exactly by 400 then it is a leap year
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_from_reference(day, month, year):
    leap_years = 0
    days = 0

    for year in range(0, year):
        if is_leap_year(year):
            leap_years += 1
    
    days = ((365 * year) + leap_years) + sum(month_days[:month]) + day
    
    return days
    
start_date_days = days_from_reference(start_day, start_month, start_year)
end_date_days = days_from_reference(end_day, end_month, end_year)

days_between = abs(end_date_days - start_date_days) - 1 # Subtract 1 as we aren't counting partial days

print(f'There are {days_between} full days between {start_date} and {end_date}')
