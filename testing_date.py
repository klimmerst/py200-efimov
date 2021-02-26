import pytest
from date import Date, TimeDelta


@pytest.mark.parametrize("days, months, years", [
    (None, 1, 1),
    (10, None, 10),
    (100, 100, None),
])
def test_create_time_delta(days, months, years):
    ex = TimeDelta(days, months, years)
    assert ex.days == 0 if days is None else days
    assert ex.months == 0 if months is None else months
    assert ex.years == 0 if years is None else years


@pytest.mark.parametrize("days, months, years", [
    (-1, 1, 1),
    (10, 'some_str', 10),
    (100, 100, [100])
])
def test_create_err_time_delta(days, months, years):
    with pytest.raises(ValueError):
        TimeDelta(days, months, years)


@pytest.mark.parametrize('args', [
    [11, 1, 2001],
    ('10.10.2001',)
])
def test_create_date_int_or_str(args):
    ex = Date(*args)

    assert str(ex) == f'{ex.day:20d}.{ex.month:20d}.{ex.year:40d}'
    assert repr(ex) == f'Date({ex.day:20d}, {ex.month:20d}, {ex.year:40d})'


@pytest.mark.parametrize('args', [
    ('10', 10, 2010),
    (10, -10, 2010),
    (10, 10, 0),
    ('100.10.2010',),
    ('1.1.1.1',),
    ('-1.10.1000',)
])
def test_create_err_date_int_or_str(args):
    with pytest.raises(ValueError):
        Date(*args)


@pytest.mark.parametrize("day", [1, 30])
@pytest.mark.parametrize("month", [1, 12])
@pytest.mark.parametrize("year", [1, 2000])
def test_successful_setters_in_date(day, month, year):
    ex = Date(10, 10, 10)
    ex.day = day
    assert ex.day == day
    ex.month = month
    assert ex.month == month
    ex.year = year
    assert ex.year == year


@pytest.mark.parametrize("err_day", ['-11', 40, 0])
@pytest.mark.parametrize("err_month, err_year", [
    [-10, -10],
    [40, 0]
])
def test_failure_setters_in_date(err_day, err_month, err_year):
    ex = Date(10, 10, 10)
    with pytest.raises(ValueError):
        ex.day = err_day
    with pytest.raises(ValueError):
        ex.month = err_month
    with pytest.raises(ValueError):
        ex.year = err_year


@pytest.mark.parametrize('minuend', [Date(1, 1, 2002)])
@pytest.mark.parametrize('subtrahend, difference', [
    (Date(31, 12, 2001), 1),
    (Date(22, 12, 2001), 10),
    (Date(5, 7, 2001), 180),
    (Date(1, 1, 2001), 365)
])
def test_successful_sub(minuend, subtrahend, difference):
    sub = minuend - subtrahend
    assert sub == difference


@pytest.mark.parametrize('minuend', [Date(1, 1, 2002)])  # в столбик subtrahend или в строчку
@pytest.mark.parametrize('subtrahend', [
    'some_str',
    1,
    None,
    TimeDelta(1, 1, 1)
])
def test_failure_sub(minuend, subtrahend):
    with pytest.raises(TypeError):
        minuend - subtrahend


@pytest.mark.parametrize('date', [Date(1, 1, 2001)])
@pytest.mark.parametrize('timedelta, up_date', [
    (TimeDelta(1, 0, 0), Date(2, 1, 2001)),
    (TimeDelta(30, 0, 0), Date(31, 1, 2001)),
    (TimeDelta(365, 0, 0), Date(1, 1, 2002)),
    (TimeDelta(0, 1, 0), Date(1, 2, 2001)),
    (TimeDelta(0, 12, 0), Date(1, 1, 2002)),
    (TimeDelta(0, 0, 1), Date(1, 1, 2002))

])
def test_successful_add(date, timedelta, up_date):
    assert str(up_date) == str(date + timedelta)


@pytest.mark.parametrize('date', [Date(1, 1, 2002)])
@pytest.mark.parametrize('timedelta', [
    'some_str',
    1,
    None,
    Date(1, 1, 2001)
])
def test_failure_add(date, timedelta):
    with pytest.raises(TypeError):
        date + timedelta


@pytest.mark.parametrize('date', [Date(1, 1, 2001)])
@pytest.mark.parametrize('timedelta, up_date', [
    (TimeDelta(1, 0, 0), Date(2, 1, 2001)),
    (TimeDelta(30, 0, 0), Date(1, 2, 2001)),
    (TimeDelta(365, 0, 0), Date(1, 2, 2002)),
    (TimeDelta(0, 1, 0), Date(1, 3, 2002)),
    (TimeDelta(0, 12, 0), Date(1, 3, 2003)),
    (TimeDelta(0, 0, 1), Date(1, 3, 2004))

])
def test_successful_iadd(date, timedelta, up_date):
    date += timedelta
    assert str(up_date) == str(date)


@pytest.mark.parametrize('date', [Date(1, 1, 2002)])
@pytest.mark.parametrize('timedelta', [
    'some_str',
    1,
    None,
    Date(1, 1, 2001)
])
def test_failure_iadd(date, timedelta):
    with pytest.raises(TypeError):
        date += timedelta
