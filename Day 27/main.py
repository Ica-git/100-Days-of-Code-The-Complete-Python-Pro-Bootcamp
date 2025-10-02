from tkinter import *

def button_clicked():
    print("Button clicked")
    my_label["text"] = input.get()

window = Tk()

window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20)


my_label = Label( text="Im an Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

button = Button(text="Click Me",command=button_clicked)
button.grid(column=1, row=1)

button = Button(text="Click Me 2",command=button_clicked)
button.grid(column=2, row=0)

input = Entry(width = 10)
print(input.get())
input.grid(column=3, row=2)







window.mainloop()
