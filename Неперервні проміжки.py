from dataclasses import dataclass


@dataclass()
class Date:
    year: int
    month: int
    date: int

    def __gt__(self, year):
        return self.year == year.year

    def __gt__(self, month):
        return self.month <= month.month

    def __gt__(self, date):
        return self.date >= date.date




@dataclass()
class DateRange:
    start_date: Date
    end_date: Date



def get_ranges_wo_insurance(insurance_periods: list[DateRange]) -> list[DateRange]:
    _insurances = []

    for date in range(len(_insurances)-1):
        return _insurances[DateRange.end_date, DateRange.start_date]


    return []


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