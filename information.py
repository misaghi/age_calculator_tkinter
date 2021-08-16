import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont

from sub_information import subInformation

class information(ttk.Frame):
    """Please provide these options: date_start|date_end|age_in_years|age_in_months|age_in_days|
    age_in_hours|age_in_minutes|age_in_seconds 
    """

    def __init__(self, master=None, **kw):
        date_start = kw.pop('date_start')
        date_end = kw.pop('date_end')
        age_in_years = kw.pop('age_in_years')
        age_in_weeks = kw.pop('age_in_weeks')
        age_in_months = kw.pop('age_in_months')
        age_in_days = kw.pop('age_in_days')
        age_in_hours = kw.pop('age_in_hours')
        age_in_minutes = kw.pop('age_in_minutes')
        age_in_seconds = kw.pop('age_in_seconds')

        super().__init__(master=master, **kw)

        style = ttk.Style()
        font = tkFont.Font(self, weight='bold', size=10)
        style.configure('header.TLabel', font=font, background='#518428')

        self.cal_image = tk.PhotoImage(file='calendar.png')
        self.check_image = tk.PhotoImage(file='check.png')

        label_1 = ttk.Label(
            self, text='Provided dates', style='header.TLabel', image=self.cal_image, compound=tk.LEFT
        )
        label_2 = ttk.Label(
            self, text='Results', style='header.TLabel', image=self.check_image, compound=tk.LEFT
        )

        subInformation(
            self, labelwidget=label_1, mode='info', date_start=date_start, date_end=date_end
        ).pack(padx=30, pady=(30, 10), ipadx=38)
        subInformation(
            self, labelwidget=label_2, mode='result', age_in_years=age_in_years, age_in_months=age_in_months,
            age_in_weeks=age_in_weeks, age_in_days=age_in_days, age_in_hours=age_in_hours,
            age_in_minutes=age_in_minutes, age_in_seconds=age_in_seconds
        ).pack(padx=30, pady=(10, 30), ipadx=15)