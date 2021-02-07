from typing import Optional, overload


class TimeDelta:
    def __init__(self, days: Optional[int] = None, months: Optional[int] = None, years: Optional[int] = None):
        ...


class Date:
    """Класс для работы с датами"""

    @overload
    def __init__(self, day: int, month: int, year: int):
        """Создание даты из трех чисел"""

    @overload
    def __init__(self, date: str):
        """Создание даты из строки формата dd.mm.yyyy"""

    def __init__(self, *args, **kwargs):
        ...

    def __str__(self) -> str:
        """Возвращает дату в формате dd.mm.yyyy"""

    def __repr__(self) -> str:
        """Возвращает дату в формате Date(day, month, year)"""

    def is_leap_year(self, year: int) -> bool:
        """Проверяет, является ли год високосным"""

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""

    @property
    def day(self):
        return None

    @day.setter
    def day(self, value: int):
        """value от 1 до 31. Проверять значение и корректность даты"""

    @property
    def month(self):
        return None

    @month.setter
    def month(self, value: int):
        """value от 1 до 12. Проверять значение и корректность даты"""

    @property
    def year(self):
        return None

    @year.setter
    def year(self, value: int):
        """value от 1 до ... . Проверять значение и корректность даты"""

    def __sub__(self, other: "Date") -> int:
        """Разница между датой self и other (-)"""

    def __add__(self, other: TimeDelta) -> "Date":
        """Складывает self и некий timedeltа. Возвращает НОВЫЙ инстанс Date, self не меняет (+)"""

    def __iadd__(self, other: TimeDelta) -> "Date":
        """Добавляет к self некий timedelta меняя сам self (+=)"""
