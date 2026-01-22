class WeekDayError(Exception):
    pass
	

class Weeker:
    week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in Weeker.week_days:
            raise WeekDayError
        self.__day = day
        self.__day_index = Weeker.week_days.index(day) 
        

    def __str__(self):
        return self.__day

    def add_days(self, n):
        n %= 7
        self.__day = Weeker.week_days[self.__day_index + n]


    def subtract_days(self, n):
        n %= 7
        self.__day = Weeker.week_days[self.__day_index - n]


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
    
