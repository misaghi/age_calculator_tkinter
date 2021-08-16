import tkinter as tk
import tkinter.ttk as ttk

from date_entry import dateEntry
from arithmetic import Arithmetic
from information import information

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Age calculator')
        self.resizable(False, False)

        self.date_entry_1 = dateEntry(self, mode='start')
        self.date_entry_2 = dateEntry(self, mode='end')
        self.btn = ttk.Button(self, text='Calculate', command=self.calculate, cursor='hand1')

        menu = tk.Menu(self, tearoff=False, cursor='hand1')
        menu.add_command(label='About', command=self.show_about)

        self.config(menu=menu)
        self.show_entries()

    def show_entries(self):
        try:
            self.info.pack_forget()
            self.calculate_again.pack_forget()
        except AttributeError:
            pass
        self.date_entry_1.pack(pady=(30, 10))
        self.date_entry_2.pack(pady=(10, 30))
        self.btn.pack(ipadx=5, ipady=5, pady=30)

    def calculate(self):
        date1 = self.date_entry_1.date
        date2 = self.date_entry_2.date

        if date1 is False or date2 is False:
            self.show_entries()
            return

        self.date_entry_1.pack_forget()
        self.date_entry_2.pack_forget()
        self.btn.pack_forget()

        arthimetic = Arithmetic(date1, date2)
        results = arthimetic.results
        self.show_results(date1, date2, results)
    
    def show_results(self, date1, date2, results):
        self.info = information(
            self, date_start=date1, date_end=date2, age_in_days=results[0], age_in_weeks=results[1],
            age_in_months=results[2], age_in_years=results[3], age_in_hours=results[4],
            age_in_minutes=results[5], age_in_seconds=results[6]
        )
        self.calculate_again = ttk.Button(self, text='Return', command=self.show_entries, cursor='hand1')
        
        self.info.pack()
        self.calculate_again.pack(ipadx=5, ipady=5, pady=(10, 30))

    def show_about(self):
        toplevel = tk.Toplevel(self)
        x = int(self.winfo_x())
        y = int(self.winfo_y())
        toplevel.geometry('+{}+{}'.format(x, y))
        toplevel.resizable(False, False)
        toplevel.title('About')

        toplevel.image = tk.PhotoImage(file='info.png')
        ttk.Label(
            toplevel,
            text='''This small software was built by
Seyed Amirhossein Misaghi,
CE Student at University of Guilan
Summer 1400''', style='mb.TLabel', image=toplevel.image, compound=tk.LEFT
        ).pack()

if __name__ == '__main__':
    app = App()
    app.mainloop()