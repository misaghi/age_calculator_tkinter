import tkinter as tk
import tkinter.ttk as ttk

class subInformation(ttk.LabelFrame):
    """A class representing a ttk.LabelFrame that is used for displaying the provided dates
    and the results.
    mode='result' or 'info'
    Other necssary args are: date_start,date_end,age_in_years,age_in_months,age_in_days,
    age_in_hours,age_in_minutes,age_in_seconds
    """

    def __init__(self, master=None, **kw):
        mode = kw.pop('mode')
        if mode == 'info':
            date_start = kw.pop('date_start')
            date_end = kw.pop('date_end')
        elif mode == 'result':
            age_in_years = kw.pop('age_in_years')
            age_in_months = kw.pop('age_in_months')
            age_in_weeks = kw.pop('age_in_weeks')
            age_in_days = kw.pop('age_in_days')
            age_in_hours = kw.pop('age_in_hours')
            age_in_minutes = kw.pop('age_in_minutes')
            age_in_seconds = kw.pop('age_in_seconds')

        super().__init__(master=master, **kw)
        
        if mode == 'info':
            opts = {'padx': (10, 0), 'pady': 5, 'sticky': tk.W}

            ttk.Label(self, text='Birthday').grid(row=0, column=0, **opts)
            ttk.Label(
                self, text='{}.{}.{}'.format(date_start[0], date_start[1], date_start[2])
            ).grid(row=0, column=1, **opts)
            ttk.Label(self, text='Age at').grid(row=1, column=0, **opts)
            ttk.Label(
                self, text='{}.{}.{}'.format(date_end[0], date_end[1], date_end[2])
            ).grid(row=1, column=1, **opts)
        elif mode == 'result':
            opts = {'anchor': tk.W, 'pady': 5, 'padx': 10}

            ttk.Label(self, text='Age:').pack(**opts)
            ttk.Label(
                self, text='{} years {} months {} days'.format(age_in_years[0], age_in_years[1], age_in_years[2])
            ).pack(**opts)
            ttk.Label(self, text='{} months {} days'.format(age_in_months[0], age_in_months[1])).pack(**opts)
            ttk.Label(self, text='{} weeks {} days'.format(age_in_weeks[0], age_in_weeks[1])).pack(**opts)
            ttk.Label(self, text='{} days'.format(age_in_days)).pack(**opts)
            ttk.Label(self, text='{} hours'.format(age_in_hours)).pack(**opts)
            ttk.Label(self, text='{} minutes'.format(age_in_minutes)).pack(**opts)
            ttk.Label(self, text='{} seconds'.format(age_in_seconds)).pack(**opts)