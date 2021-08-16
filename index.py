# from date_entry import dateEntry
# import tkinter as tk
# from information import information

# class App(tk.Tk):

#     def __init__(self):
#         super().__init__()

#         de = dateEntry(self, mode='start')
#         de1 = dateEntry(self, mode='end')
#         tk.Button(self, text='show')
#         de.pack()
#         de1.pack()
#         # info = information(self, date_start=1, date_end=2, age_in_years=3, age_in_months=4,
#         # age_in_days=5, age_in_hours=6, age_in_minutes=7, age_in_seconds=8)
#         # info.pack()

# if __name__ == '__main__':
#     app = App()
#     app.mainloop()

from datetime import datetime

date = datetime(2000, 10, 1).date()
now = datetime.now().date()
date2 = datetime(2021, 10, 1).date()
print(date, now)
weight = {1: 31, 2: 29, 3: 31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# print(now - date)
d = date2 - now
print(d.days)