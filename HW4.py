import logging
from datetime import datetime, timedelta, date


class Date:
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

    def __str__(self) -> str:
        """
        to print the date
        :return: day.month.year -> 1.3.2022
        """
        s = f'{self._day}.{self._month}.{self._year}'
        return s

    def isValid(self) -> bool:
        """
        isValid take a date and check it
        :return: True if the date is correct, if not returns False
        """
        if not isinstance(self._day, int):
            raise TypeError("The day must be a number..")
            return False
        if not isinstance(self._month, int):
            raise TypeError("The month must be a number..")
            return False
        if not isinstance(self._year, int):
            raise TypeError("The year must be a number..")
            return False

        if self._month == 1 or self._month == 3 or self._month == 5 or self._month == 7 or self._month == 8 or self._month == 10 or self._month == 12:
            if self._day < 1 or self._day > 31:
                return False
        if self._month == 4 or self._month == 6 or self._month == 9 or self._month == 11:
            if self._day < 1 or self._day > 30:
                return False
        if self._month == 2:
            if self._day < 1 or self._day > 29:
                return False
            if self._day == 29:
                if self._year % 4 != 0:
                    return False
        return True

    def getNextDay(self) -> "Date":
        """
        for example: 1.3.2022
        :return:  tomorrow's date is  -> 2.3.2022
        """
        tom_day, tom_month, tom_year = self._day, self._month, self._year
        if self._month == 2:
            if self._day == 28:
                if self._year % 4 == 0:
                    tom_day = 29
                else:
                    tom_day = 1
                    tom_month = 3
            elif self._day == 29:
                tom_day = 1
                tom_month = 3
            else:
                tom_day = self._day + 1

        if self._month == 1 or self._month == 3 or self._month == 5 or self._month == 7 or self._month == 8 or self._month == 10:
            if self._day == 31:
                tom_day = 1
                tom_month = self._month + 1
            else:
                tom_day = self._day + 1

        if self._month == 4 or self._month == 6 or self._month == 9 or self._month == 11:
            if self._day == 30:
                tom_day = 1
                tom_month = self._month + 1
            else:
                tom_day = self._day + 1

        if self._month == 12:
            if self._day == 31:
                tom_day = 1
                tom_month = 1
                tom_year = self._year + 1
            else:
                tom_day = self._day + 1
        return Date(tom_day, tom_month, tom_year)

    def getNextDays(self, daysToAdd: int) -> "Date":
        """
        for example: 1.2.2022 ,  getNextDays(2) -> 3.2.2022
        :param daysToAdd: integer number
        :return: Date after daysToAdd days
        """
        if not isinstance(daysToAdd, int):
            raise TypeError("The daysToAdd must be a number..")
            return Date(self._day, self._month, self._year)
        else:
            specific_date = datetime(self._year, self._month, self._day)
            new_date = specific_date + timedelta(daysToAdd)
        return Date(new_date.day, new_date.month, new_date.year)

    def __eq__(self, other) -> bool:
        """
        for example: 1.2.2022 == 1.2.2021 -> False
        :param other: Date type
        :return: True or False if the dates are equal
        """
        first_date = date(self._year, self._month, self._day)
        second_date = date(other._year, other._month, other._day)
        if first_date == second_date:
            return True
        else:
            return False

    def __ne__(self, other) -> bool:
        """
        for example: 1.2.2022 != 1.2.2021 -> True
        :param other: Date type
        :return: True or False if the dates are not equal
        """
        first_date = date(self._year, self._month, self._day)
        second_date = date(other._year, other._month, other._day)
        if first_date != second_date:
            return True
        else:
            return False

    def __lt__(self, other) -> bool:
        """
        for example: 1.2.2022 < 1.2.2021 -> False
        :param other: Date type
        :return: True or False if the first date is less than the second date
        """
        first_date = date(self._year, self._month, self._day)
        second_date = date(other._year, other._month, other._day)
        if first_date < second_date:
            return True
        else:
            return False

    def __le__(self, other) -> bool:
        """
        for example: 1.2.2022 <= 1.2.2021 -> False
        :param other: Date type
        :return: True or False if the first date is less than or equal the second date
        """
        first_date = date(self._year, self._month, self._day)
        second_date = date(other._year, other._month, other._day)
        if first_date <= second_date:
            return True
        else:
            return False

    def __ge__(self, other) -> bool:
        """
        for example: 1.2.2022 >= 1.2.2021 -> True
        :param other: Date type
        :return: True or False if the first date is greater than or equal the second date
        """
        first_date = date(self._year, self._month, self._day)
        second_date = date(other._year, other._month, other._day)
        if first_date >= second_date:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        """
        for example: 1.2.2022 > 1.2.2021 -> True
        :param other: Date type
        :return: True or False if the first date is greater than the second date
        """
        first_date = date(self._year, self._month, self._day)
        second_date = date(other._year, other._month, other._day)
        if first_date > second_date:
            return True
        else:
            return False

    def __sub__(self, other) -> str:
        """
        for example: 1, 2, 2022 , 1, 2, 2021 -> -365 days
        :param other: Date type
        :return: the difference in days between a given date and another date
        """
        start = date(self._year, self._month, self._day)
        end = date(other._year, other._month, other._day)
        difference_day = (end - start).days
        if difference_day == 0:
            return difference_day
        elif difference_day == 1 or difference_day == -1:
            return str(difference_day) + " day"
        else:
            return str(difference_day) + " days"


b1 = Date(1, 2, 2022)
b2 = Date(1, 2, 2021)
print(f'valid date : {b1.isValid()}')
print(f'Tomorrow\'s date from {str(b1)} is {str(b1.getNextDay())}')
print(f'the date after 850 days is: {str(b1)} --> {str(b1.getNextDays(850))}')
print(f'if {str(b1)} is equal "==" {str(b2)} : {b1.__eq__(b2)}')
print(f'if {str(b1)} is not equal "!=" {str(b2)} : {b1.__ne__(b2)}')
print(f'if {str(b1)} is less than "<" {str(b2)} : {b1.__lt__(b2)}')
print(f'if {str(b1)} is less than or equal "<=" {str(b2)} : {b1.__le__(b2)}')
print(f'if {str(b1)} is greater than or equal ">=" {str(b2)} : {b1.__ge__(b2)}')
print(f'if {str(b1)} is greater than ">" {str(b2)} : {b1.__gt__(b2)}')
print(f'the difference in days between a given {str(b1)} and {str(b2)} is {b1.__sub__(b2)}')
