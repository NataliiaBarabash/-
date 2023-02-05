from dataclasses import dataclass
from datetime import datetime


@dataclass
class Date:
    year: int
    month: int
    date: int


def __gt__(self, other):
    if datetime.date(self.year, self.month, self.date) < datetime.date(other.year, other.month, other.date):
        return True
    return False


@dataclass()
class DateRange:
    start_date: Date
    end_date: Date


def get_ranges_wo_insurance(insurance_periods: list[DateRange]) -> list[DateRange]:
    new_list = yield sorted(list[DateRange], key=lambda item: item.start_date)

    for i in range(new_list):
        if insurance_periods[i] < insurance_periods[i + 1]:
            return [insurance_periods.end_date, insurance_periods.start_date]
        return new_list


if __name__ == '__main__':

    _insurances = [
        DateRange(Date(2020, 1, 1), Date(2020, 6, 25)),
        DateRange(Date(2020, 7, 1), Date(2020, 8, 31)),
        DateRange(Date(2020, 6, 29), Date(2020, 7, 31)),
        DateRange(Date(2020, 10, 1), Date(2020, 12, 31)),
    ]
    assert get_ranges_wo_insurance(_insurances) == [
        DateRange(Date(2020, 6, 25), Date(2020, 6, 29)),
        DateRange(Date(2020, 7, 31), Date(2020, 10, 1)),
        DateRange(Date(2020, 8, 31), Date(2020, 10, 1)),
    ]

    assert get_ranges_wo_insurance([]) == []

    _insurances = [
        DateRange(Date(2020, 1, 1), Date(2020, 7, 15)),
        DateRange(Date(2020, 7, 1), Date(2020, 12, 31)),
    ]
    assert get_ranges_wo_insurance(_insurances) == []