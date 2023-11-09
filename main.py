from tkinter import *


# def convert():
#     F = float(fahrenheit_entry.get())
#     C = (F - 32) * 5 / 9
#     display_celsius_label_1['text'] = str(C)


my_window = Tk()

# 30. FAHRENHEIT TO CELSIUS
# fahrenheit_label_1 = Label(my_window,
#                            text='Enter Fahrenheit')
# celsius_label_1 = Label(my_window,
#                         text='Celsius temperature')
# display_celsius_label_1 = Label(my_window)
# fahrenheit_entry = Entry(my_window)
# convert_button = Button(my_window,
#                         text='Convert',
#                         command=convert)
#
# fahrenheit_label_1.grid(row=0, column=0)
# fahrenheit_entry.grid(row=0, column=1)
# celsius_label_1.grid(row=1, column=0)
# display_celsius_label_1.grid(row=1, column=1)
# convert_button.grid(row=2, column=0)


# 31. ALTERNATIVE PYTHON FAHRENHEIT TO CELSIUS
def convert():
    F = float(fahrenheit.get())
    C = (F - 32) * 5 / 9
    celsius.set(str(C))


celsius = StringVar()
fahrenheit = StringVar()

fahrenheit_label_1 = Label(my_window,
                           text='Enter Fahrenheit')
celsius_label_1 = Label(my_window,
                        text='Celsius temperature')
display_celsius_label_1 = Label(my_window,
                                textvariable=celsius)
fahrenheit_entry = Entry(my_window,
                         textvariable=fahrenheit)
convert_button = Button(my_window,
                        text='Convert',
                        command=convert)

fahrenheit_label_1.grid(row=0, column=0)
fahrenheit_entry.grid(row=0, column=1)
celsius_label_1.grid(row=1, column=0)
display_celsius_label_1.grid(row=1, column=1)
convert_button.grid(row=2, column=0)

fahrenheit_entry.focus()

my_window.mainloop()
