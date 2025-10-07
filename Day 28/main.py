from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_clicked():
    print("Button start clicked")

def reset_clicked():
    print("Button reset clicked")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)

canvas = Canvas(window, width = 250, height = 274, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(120, 132, image=tomato_img)
canvas.create_text(120,160, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.pack()

title_label = Label(text="Timer", fg = GREEN, bg = YELLOW, font=(FONT_NAME, 30, "bold"))
title_label.place(x=60, y=-30)

btn_start = Button(text = "Start", command = start_clicked, font=(FONT_NAME, 8, "bold"))
btn_start.place(x=-30, y=235)

btn_start = Button(text = "Reset", command = reset_clicked, font=(FONT_NAME, 8, "bold"))
btn_start.place(x=210, y=235)

my_label = Label(text="✔", fg = GREEN, bg = YELLOW, font=(FONT_NAME, 15, "bold"))
my_label.place(x=110, y=255)

window.mainloop()


