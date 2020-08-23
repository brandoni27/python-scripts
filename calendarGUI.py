from tkinter import *
import calendar

# Initializing Tkinter
root = Tk()

# Setting title of our GUI
root.title("GUI Calendar")

# Year for which we want the calendar to be shown on our GUI
year = 2020

# Storing 2020 year calendar data inside myCal
myCal = calendar.calendar(year)

# Showing calendar data using label widget
cal_year = Label(root, text = myCal, font = "Consolas 10 bold")

# Packing the Label Widget
cal_year.pack()

# Running the program in ready state
root.mainloop()
