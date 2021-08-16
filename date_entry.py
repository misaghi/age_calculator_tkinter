 #TODO Create my own custom show warning

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb

from arithmetic import Arithmetic

from datetime import date, datetime
from functools import partial

class dateEntry(ttk.Frame):
    """Define a 'mode' option to determine which date entry is it. 'mode' must have a value of
    'start' or 'end'.
    """

    MONTHS = (
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    )
    NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    def __init__(self, master=None, **kw):
        mode = kw.pop('mode')

        super().__init__(master=master, **kw)

        # Wether it is birthday or not...
        if mode == 'end':
            today = date.today()
        else:
            today = datetime(year=1900, month=1, day=1).date()
        
        # We need it later
        self.year = date.today().year

        self.month_var = tk.StringVar()
        self.month_var.set(self.MONTHS[today.month - 1])
        self.year_var = tk.IntVar()
        self.year_var.set(today.year)
        self.day_var = tk.IntVar()
        self.day_var.set(today.day)

        self.month_var.trace('w', self.config_days)

        yvcmd_day = (self.register(partial(self.validate_if_number, mode='day')), '%P')
        yvcmd_year = (self.register(partial(self.validate_if_number, mode='year')), '%P')
        yvcmd_month = (self.register(self.validate_month))

        self.year_entry = ttk.Spinbox(
            self, from_=1900, to=self.year, validate='key', validatecommand=yvcmd_year, textvariable=self.year_var,
            width=5
        )
        self.day_entry = ttk.Spinbox(
            self, from_=1, to=31, validate='key', validatecommand=yvcmd_day, textvariable=self.day_var,
            width=3
        )
        self.month_entry = ttk.Combobox(
            self, values=self.MONTHS, validate='key', validatecommand=yvcmd_month, textvariable=self.month_var,
            width=11
        )

        self.month_entry.pack(side=tk.LEFT, padx=(30, 10))
        self.day_entry.pack(side=tk.LEFT, padx=10)
        self.year_entry.pack(side=tk.LEFT, padx=(10, 30))
    
    def validate_if_number(self, inp, mode):
        '''mode defines if it is for year or day
        '''

        try:
            int_inp = int(inp)
        except ValueError:
            int_inp = 0

        # This part checks if the input is number or not
        for i in inp:
            if i in self.NUMBERS:
                continue
            else:
                return False
        
        # This part checks if the input is not to small or too large
        if mode == 'year':
            if int_inp > self.year or len(inp) > 4:
                return False
        else:
            if int_inp > self.day_entry.cget('to') or len(inp) > 2:
                return False

        return True
    
    def validate_month(self): # A method prevents us from entering anything to month_entry
        return False

    def config_days(self, *args):
        if self.month_var.get() == 'February':
            self.day_entry.config(to=28)
        elif self.month_var.get() in ['April', 'June', 'September', 'November']:
            self.day_entry.config(to=30)
        else:
            self.day_entry.config(to=31)

    @property
    def date(self):
        '''Returns a tuple on success. Otherwise returns False
        '''
        try:
            year = self.year_var.get()
            day = self.day_var.get()
            month = self.MONTHS.index(self.month_var.get()) + 1
            return year, month, day
        except tk.TclError:
            mb.showerror('Error', 'Please enter a valid date')
            return False