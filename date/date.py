from typing import Optional, overload


class TimeDelta:
    def __init__(self, days: Optional[int] = None, months: Optional[int] = None, years: Optional[int] = None):
        self.days = days or 0
        self.months = months or 0
        self.years = years or 0

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, value):
        if isinstance(value, int) and value >= 0:
            self._days = value
        else:
            raise ValueError('Incorrect days')

    @property
    def months(self):
        return self._months

    @months.setter
    def months(self, value):
        if isinstance(value, int) and value >= 0:
            self._months = value
        else:
            raise ValueError('Incorrect months')

    @property
    def years(self):
        return self._years

    @years.setter
    def years(self, value):
        if isinstance(value, int) and value >= 0:
            self._years = value
        else:
            raise ValueError('Incorrect years')


class Date:
    """Класс для работы с датами"""

    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # НЕ високосный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)   # високосный год
    )

    __slots__ = ('_day', '_month', '_year')

    @overload
    def __init__(self, day: int, month: int, year: int):
        """Создание даты из трех чисел"""

    @overload
    def __init__(self, date: str):
        """Создание даты из строки формата dd.mm.yyyy"""

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            args = [int(i) for i in args[0].split('.') if i.isdigit()]
        if len(args) == 3:
            if not self.is_valid_date(*args):
                raise ValueError('Incorrect date')
            self._day, self._month, self._year = args
        else:
            raise ValueError('Incorrect date')

    def __str__(self) -> str:
        """Возвращает дату в формате dd.mm.yyyy"""

        return f'{self._day:20d}.{self._month:20d}.{self._year:40d}'

    def __repr__(self) -> str:
        """Возвращает дату в формате Date(day, month, year)"""

        return f'Date({self._day:20d}, {self._month:20d}, {self._year:40d})'

    @classmethod
    def is_leap_year(cls, year: int) -> bool:
        """Проверяет, является ли год високосным"""

        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    @classmethod
    def get_max_day(cls, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""

        return cls.DAY_OF_MONTH[cls.is_leap_year(year)][month - 1]

    @classmethod
    def is_valid_date(cls, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""

        check_args = [day, month, year]
        if all(isinstance(i, int) for i in check_args):
            return 1 <= month <= 12 and 1 <= day <= cls.get_max_day(month, year) and 1 <= year <= 2021

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value: int):
        if self.is_valid_date(value, self.month, self.year):
            self._day = value
        else:
            raise ValueError('Day entered incorrectly')

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value: int):
        if self.is_valid_date(self.day, value, self.year):
            self._month = value
        else:
            raise ValueError('Month entered incorrectly')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        if self.is_valid_date(self.day, self.month, value):
            self._year = value
        else:
            raise ValueError('Year entered incorrectly')

    def all_days_in_date(self):
        """Возвращает количество дней от 1 года"""

        days = 0
        for i in range(1, self._year):
            if self.is_leap_year(i):
                days += 366
            else:
                days += 365

        for i in range(0, self._month - 1):
            days += Date.DAY_OF_MONTH[0][i]

        days += self.day

        return days

    def __sub__(self, other: "Date") -> int:
        """Разница между датой self и other (-)"""

        if not isinstance(other, Date):
            raise TypeError("It's not a Date instance")

        return self.all_days_in_date() - other.all_days_in_date()

    def __add__(self, other: TimeDelta) -> "Date":
        """Складывает self и некий timedeltа. Возвращает НОВЫЙ инстанс Date, self не меняет (+)"""

        if not isinstance(other, TimeDelta):
            raise TypeError("It's not a TimeDelta instance")

        new_instance = Date(self._day, self._month, self._year)
        new_instance += other

        return new_instance

    def __iadd__(self, other: TimeDelta) -> "Date":
        """Добавляет к self некий timedelta меняя сам self (+=)"""

        if not isinstance(other, TimeDelta):
            raise TypeError("It's not a TimeDelta instance")

        self._year += other._years

        days_counter = 0
        while days_counter < other._days:
            days_counter += 1
            if self._day < Date.get_max_day(self._month, self._year):
                self._day += 1
            else:
                if self._month == 12:
                    self._day = 1
                    self._month = 1
                    self._year += 1
                else:
                    self._day = 1
                    self._month += 1

        months_counter = 0
        while months_counter < other._months:
            months_counter += 1
            if self._month == 12:
                self._year += 1
                self._month = 1
            else:
                self._month += 1

        return self

r = Date(1,1,1)
