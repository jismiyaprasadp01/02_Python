#Sort List of Dates Given as Strings

from datetime import datetime

def sort_dates(date_list):
    return sorted(date_list, key=lambda date: datetime.strptime(date, "%Y-%m-%d"))

dates = ["2021-05-21", "2019-01-12", "2020-12-15"]
sorted_dates = sort_dates(dates)
print(sorted_dates)
