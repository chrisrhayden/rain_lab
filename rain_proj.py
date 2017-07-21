"""
this is a rain data annalists
fill this out more
"""

import os
import datetime
from typing import Tuple


Path = str


def show_list(dir_path) -> Path:
    """ show a list of files to chose from

    make a list of file with an assigned number
    then make a dictionary and menu to select
    then return a path as a string
    """

    the_files = [a_file for a_file in os.listdir(dir_path)
                 if a_file.endswith('.rain')]

    file_names = {str(i): file_n for i, file_n
                  in enumerate(the_files, start=1)}

    for num, data_file in file_names.items():
        print(num, data_file)

    user_input = input('witch data set: ')
    file_path = dir_path + file_names[user_input]
    return file_path


def open_file(file_name: str) -> str:
    """
    standard open file handler
    """

    with open(file_name, 'r') as f:
        content = f.read()
        return content


def clean_file(raw_data: str) -> Tuple[list, str]:  # needs Tuple from typing
    """ clean the file of noise """

    split_data = raw_data.split('\n')

    header = split_data[:11]

    just_data = split_data[11:]
    all_days = [day.split() for day in just_data]

    return all_days, header


def prosses_file(list_of_data: list) -> dict:
    """ change raw data in to useful things """

    # dictionary building thing
    daly_totals = dict()
    # row = whole line in raw data
    for row in list_of_data:
        # if exsits
        try:
            date = row[0]
        except IndexError:
            continue
        # make nums from the strs in the row
        try:
            day_ints = [int(hour) for hour in row[1:]]
        # unless its not a num
        except ValueError:
            continue
        # add to the dictionary day_totals
        daly_totals[date] = day_ints

    return daly_totals


def do_math(good_data: dict) -> Tuple[dict, dict]:
    """ calculate the data

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

    return daly_total, yearly_total


def show_results(days: dict, years: dict, file_path: Path):
    """ show highest year and day """
    # print(max(days, key=days.get))
    # print(days[max(days, key=days.get)])
    max_day = max(days, key=days.get) \
        + ' - ' \
        + str(days[max(days, key=days.get)])

    max_year = str(max(years, key=years.get)) \
        + ' - ' \
        + str(years[max(years, key=years.get)])
    list_path = file_path.split('/')

    print()
    print(list_path[-1][:-5])
    print(max_day)
    print(max_year)


def start_func():
    """ start the program

    set the dir path
    run the functions in order
    this program will only take .rain files
    """

    dir_name = '/home/chris/proj/rain_lab/data_sets/'

    closed_file = show_list(dir_name)
    raw_data = open_file(closed_file)
    clean_data, header = clean_file(raw_data)
    the_prossed_data = prosses_file(clean_data)
    total_days, total_years = do_math(the_prossed_data)
    show_results(total_days, total_years, closed_file)


start_func()
