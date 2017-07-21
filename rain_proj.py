"""
this is a rain data annalists
fill this out more
"""

import datetime
from typing import Tuple


def open_file(file_name: str) -> str:
    """
    standard open file handler
    """
    with open(file_name, 'r') as f:
        content = f.read()
        return content


def clean_file(raw_data: str) -> Tuple[list, list]:  # didnt like [list, dir]
    """ clean the file of noise """
    split_data = raw_data.split('\n')
    header = split_data[:11]
    # just_data = split_data[11:20]  # for testing
    # when i fix ti acounbt fo - and blank lines
    just_data = split_data[11:]
    all_days = [day.split() for day in just_data]
    return all_days, header


def prosses_file(list_of_data: list) -> dict:
    """ change raw data in to useful things """
    # dict_data = {day[0]: day[1:] for day in list_of_data}

    # dictionary building thing
    daly_totals = dict()
    # row = whole line in raw data
    for row in list_of_data:
        # if list is popu make key from date
        try:
            date = row[0]
        except IndexError:
            continue
        # make numbers from the strs in the row unless its not a num
        try:
            day_ints = [int(hour) for hour in row[1:]]
        except ValueError:
            continue
        # add to the dictionary day_totals
        daly_totals[date] = day_ints

    return daly_totals


def do_math(good_data: dict) -> Tuple[dict, dict]:
    """
    calculate the data

    find the highest rain day
    find the heist rain year
    """
    daly_total = {}
    yearly_total = {}
    for day, nums in good_data.items():
        datei = datetime.datetime.strptime(day, '%d-%b-%Y')
        daly_total[day] = sum(nums)                 # add all day nums

        if datei.year in yearly_total:              # if year is then add sum
            yearly_total[datei.year] += sum(nums)
        else:                                       # else add to dcit
            yearly_total[datei.year] = sum(nums)

    # print(daly_total)
    # print()
    # print(yearly_total)
    return daly_total, yearly_total


def show_results(days: dict, years: dict):
    """ show highest year and day """
    # print(max(days, key=days.get))
    # print(days[max(days, key=days.get)])
    max_day = max(days, key=days.get) + ' - ' + \
        str(days[max(days, key=days.get)])

    max_year = str(max(years, key=years.get)) + ' - ' + \
        str(years[max(years, key=years.get)])

    print(max_day)
    print(max_year)


def start_func():
    file_name = '/home/chris/proj/rain_data/data_sets/sample.rain'

    raw_data = open_file(file_name)

    clean_data, header = clean_file(raw_data)

    the_prossed = prosses_file(clean_data)

    total_days, total_years = do_math(the_prossed)

    show_results(total_days, total_years)


start_func()
