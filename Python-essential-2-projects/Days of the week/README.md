# Days of the Week – Weeker Class

## 📘 Lab Overview

This lab focuses on practicing **Object-Oriented Programming (OOP)** concepts in Python, including:

- Class design
- Custom exceptions
- Encapsulation (private attributes)
- Method-based state manipulation
- String representation of objects

You are required to implement a class called `Weeker` that stores and manipulates days of the week.

---

## 🎯 Objective

Implement a `Weeker` class that:

- Stores a day of the week
- Allows adding and subtracting days
- Validates input using a custom exception
- Represents itself as a string

---

## 📅 Supported Days

The class only accepts the following values:
Mon Tue Wed Thu Fri Sat Sun

Any other value must raise a `WeekDayError` exception.

---

## 🧩 Requirements

### 1. Custom Exception
Define a custom exception:
```python
class WeekDayError(Exception):
    pass
class WeekDayError(Exception):
    pass


class Weeker:
    __week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in Weeker.__week_days:
            raise WeekDayError
        self.__day_index = Weeker.__week_days.index(day)

    def __str__(self):
        return Weeker.__week_days[self.__day_index]

    def add_days(self, n):
        self.__day_index = (self.__day_index + n) % 7

    def subtract_days(self, n):
        self.__day_index = (self.__day_index - n) % 7

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
