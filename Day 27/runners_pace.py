from tkinter import *

def button_clicked():
    print("Button clicked")
    distance = int(input_1.get())
    time = int(input_2.get()) * 60

    pace = time / distance

    minutes = pace // 60
    seconds = pace % 60

    label_4["text"] = f"{int(minutes):02d}:{int(seconds):02d}"

window = Tk()

window.title("My First GUI Program")
window.minsize(300, 200)
window.config(padx=20, pady=20)


label_1 = Label( text="pace per km", font=("Arial", 12))
label_1.grid(column=0, row=2)
label_1.config(padx=5, pady=5)

label_2 = Label( text="Km", font=("Arial", 12))
label_2.grid(column=0, row=1)
label_2.config(padx=5, pady=5)

label_3 = Label( text="Time (min)", font=("Arial", 12))
label_3.grid(column=0, row=0)
label_3.config(padx=5, pady=5)

label_4 = Label( text=" ", font=("Arial", 12))
label_4.grid(column=1, row=2)
label_4.config(padx=5, pady=5)

button = Button(text="calculate",command=button_clicked)
button.grid(column=1, row=3)
button.config(padx=5, pady=5)

input_1 = Entry(width = 20)
print(input_1.get())
input_1.grid(column=1, row=1)

input_2 = Entry(width = 20)
print(input_2.get())
input_2.grid(column=1, row=0)







window.mainloop()