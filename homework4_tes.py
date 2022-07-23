import HW4
import pytest
import logging


@pytest.mark.smoke
def test_isValid():
    """
    isValid take a date and check it
    :return: True if the date is correct, if not returns False
    """
    logging.info("valid date :")
    b1 = HW4.Date(1, 2, 2022)
    assert b1.isValid() is True


@pytest.mark.regression
def test_getNextDay():
    """
    for example: 1.3.2022
    :return:  tomorrow's date is  -> 2.3.2022
    """
    logging.info("Tomorrow\'s date ")
    b1 = HW4.Date(1, 2, 2022)
    nextDay = b1.getNextDay()
    assert str(nextDay) == '2.2.2022'


@pytest.mark.smoke
def test_getNextDays():
    """
    for example: 1.2.2022 ,  getNextDays(2) -> 3.2.2022
    :param daysToAdd: integer number
    :return: Date after daysToAdd days
    """
    logging.info("the date after 850 days ")
    b1 = HW4.Date(1, 2, 2022)
    nextDays = b1.getNextDays(850)
    assert str(nextDays) == '31.5.2024'


@pytest.mark.regression
def test___eq__():
    """
    for example: 1.2.2022 == 1.2.2021 -> False
    :param other: Date type
    :return: True or False if the dates are equal
    """
    logging.info("If date 1 equals date 2 ")
    b1 = HW4.Date(1, 2, 2022)
    b2 = HW4.Date(1, 2, 2021)
    assert b1.__eq__(b2) is False


@pytest.mark.smoke
def test___ne__():
    """
    for example: 1.2.2022 != 1.2.2021 -> True
    :param other: Date type
    :return: True or False if the dates are not equal
    """
    logging.info("If date 1 not equal date 2 ")
    b1 = HW4.Date(1, 2, 2022)
    b2 = HW4.Date(1, 2, 2021)
    assert b1.__ne__(b2) is True


@pytest.mark.regression
def test___lt__():
    """
    for example: 1.2.2022 < 1.2.2021 -> False
    :param other: Date type
    :return: True or False if the first date is less than the second date
    """
    logging.info("If date 1 less than date 2 ")
    b1 = HW4.Date(1, 2, 2022)
    b2 = HW4.Date(1, 2, 2021)
    assert b1.__lt__(b2) is False


@pytest.mark.smoke
def test___le__():
    """
    for example: 1.2.2022 <= 1.2.2021 -> False
    :param other: Date type
    :return: True or False if the first date is less than or equal the second date
    """
    logging.info("If date 1 less than or equal date 2 ")
    b1 = HW4.Date(1, 2, 2022)
    b2 = HW4.Date(1, 2, 2021)
    assert b1.__le__(b2) is False


@pytest.mark.regression
def test___ge__():
    """
    for example: 1.2.2022 >= 1.2.2021 -> True
    :param other: Date type
    :return: True or False if the first date is greater than or equal the second date
    """
    logging.info("If date 1 greater than or equal date 2 ")
    b1 = HW4.Date(1, 2, 2022)
    b2 = HW4.Date(1, 2, 2021)
    assert b1.__ge__(b2) is True


@pytest.mark.smoke
def test___gt__():
    """
    for example: 1.2.2022 > 1.2.2021 -> True
    :param other: Date type
    :return: True or False if the first date is greater than the second date
    """
    logging.info("If date 1 greater than date 2 ")
    b1 = HW4.Date(1, 2, 2022)
    b2 = HW4.Date(1, 2, 2021)
    assert b1.__gt__(b2) is True


@pytest.mark.smoke
def test___sub__():
    """
        for example: 1, 2, 2022 , 1, 2, 2021 -> -365 days
        :param other: Date type
        :return: the difference in days between a given date and another date
    """
    logging.info("the difference in days between a given date and another date")
    b1 = HW4.Date(1, 2, 2022)
    b2 = HW4.Date(1, 2, 2021)
    assert b1.__sub__(b2) == '-365 days'
