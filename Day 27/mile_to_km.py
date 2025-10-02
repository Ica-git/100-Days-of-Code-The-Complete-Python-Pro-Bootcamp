from tkinter import *

def button_clicked():
    print("Button clicked")
    label_4["text"] = int(input.get()) * 1.60934

window = Tk()

window.title("My First GUI Program")
window.minsize(300, 150)
window.config(padx=20, pady=20)


label_1 = Label( text="is equal to", font=("Arial", 12))
label_1.grid(column=0, row=1)
label_1.config(padx=5, pady=5)

label_2 = Label( text="Miles", font=("Arial", 12))
label_2.grid(column=2, row=0)
label_2.config(padx=5, pady=5)

label_3 = Label( text="Km", font=("Arial", 12))
label_3.grid(column=2, row=1)
label_3.config(padx=5, pady=5)

label_4 = Label( text="0", font=("Arial", 12))
label_4.grid(column=1, row=1)
label_4.config(padx=5, pady=5)

button = Button(text="calculate",command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)

input = Entry(width = 20)
print(input.get())
input.grid(column=1, row=0)







window.mainloop()