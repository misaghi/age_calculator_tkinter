from datetime import datetime

class Arithmetic:
    '''All the programs calculation goes here. Returns a list of results.
    '''

    # Different months have different days.
    MONTHS_DAYS = {1: 31, 2: 28, 3: 31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    def __init__(self, first_date, second_date):
        date1 = datetime(first_date[0], first_date[1], first_date[2]).date()
        date2 = datetime(second_date[0], second_date[1], second_date[2]).date()
        self.__results = []

        self.age_in_days(date1, date2)

    @property
    def results(self):
        return self.__results
    
    def age_in_days(self, date1, date2) -> 'int':
        in_days = date2 - date1
        in_days = in_days.days
        self.__results.append(in_days)

        self.age_in_weeks(in_days)

    def age_in_weeks(self, in_days) -> 'tuple(weeks, days)':
        in_weeks = divmod(in_days, 7)
        self.__results.append(in_weeks)

        self.age_in_years(in_days)

    def age_in_years(self, in_days) -> 'tuple(years, months, days)':
        years, days_without_leap = divmod(in_days, 365)
        leap_days, _ = divmod(years, 4) # Every 4 years we have a leap year
        days = days_without_leap - leap_days
        if days < 0: # For negative number of days
            years -= 1
            days += 365
        months = 0
        #* At here consider we have years and days with leaps are counted.
        for _, d in self.MONTHS_DAYS.items():
            days -= d
            if days < 0:
                days += d
                break
            months += 1
        
        in_months = (years * 12 + months, days)
        self.__results.append(in_months)

        self.__results.append((years, months, days))

        self.age_in_hours(in_days)
    
    def age_in_hours(self, in_days) -> 'int':
        in_hours = in_days * 24
        self.__results.append(in_hours)

        self.age_in_minutes(in_hours)

    def age_in_minutes(self, in_hours) -> 'int':
        in_minutes = in_hours * 60
        self.__results.append(in_minutes)
        
        self.age_in_seconds(in_minutes)

    def age_in_seconds(self, in_minutes) -> 'int':
        in_seconds = in_minutes * 60
        self.__results.append(in_seconds)