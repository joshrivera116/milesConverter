from tkinter import *

FONT = ('Arial', 10)

new_num = 0


def calculate_miles():
    num = int(input_box.get())
    newnum = round(num * 1.609, 4)
    conversion.config(text=newnum)

options = [
    'Miles',
    'Foot',
    'Meter',
    'Centimeter',
    'yard'
]

window = Tk()
window.title('Miles to Kile Converter')
window.minsize(width=200, height=150)
window.config(pady=20)

input_box = Entry(width=15)
input_box.grid(row=0, column=1)

click = StringVar()

drop = OptionMenu(window, click, *options)
drop.grid(row=0, column=3)

conversion = Label(text=f'{new_num}', font=FONT)
conversion.grid(row=1, column=1)

km = Label(text='Km', font=FONT)
km.grid(row=1, column=2)

label = Label(text='is equal to', font=FONT)
label.grid(row=1, column=0)
label.config(padx=20)

button = Button(text='Calculate', font=FONT, command=calculate_miles)
button.grid(row=3, column=1)

window.mainloop()
