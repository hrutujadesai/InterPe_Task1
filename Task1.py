from tkinter import *
from time import strftime

window = Tk()
window.title("Unique Digital Clock")

def present_time():
    time_string = strftime('%H:%M:%S %p')
    time_label.config(text=time_string)
    
    day_string = strftime('%A')
    day_label.config(text=day_string)
    
    date_string = strftime('%B %d, %Y')
    date_label.config(text=date_string)
    
    time_label.after(1000, present_time)

time_label = Label(window, font=("DS-Digital", 100), background="black", foreground="cyan")
time_label.pack(anchor='center')

day_label = Label(window, font=("DS-Digital", 50), highlightbackground="black")
day_label.pack(anchor='center')

date_label = Label(window, font=("DS-Digital", 30), highlightbackground="black")
date_label.pack(anchor='center')

present_time()
window.mainloop()



