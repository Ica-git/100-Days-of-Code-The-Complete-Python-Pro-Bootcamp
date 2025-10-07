import math
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(fg=GREEN, text="Timer")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_clicked():
    global reps
    if reps == 9:
        reps = 0
        return
    else:
        reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(fg = RED, text = "Long Break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(fg = PINK, text = "Break")
    else:
        count_down(WORK_MIN * 60)
        title_label.config(fg=GREEN, text="Work")




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_clicked()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔ "
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)


canvas = Canvas(window, width = 250, height = 274, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(120, 132, image=tomato_img)
timer_text = canvas.create_text(120,160, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)


title_label = Label(text="Timer", fg = GREEN, bg = YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column = 1, row = 0)

btn_start = Button(text = "Start", command = start_clicked, font=(FONT_NAME, 8, "bold"))
btn_start.grid(column = 0, row = 2)

btn_start = Button(text = "Reset", command = reset_timer, font=(FONT_NAME, 8, "bold"))
btn_start.grid(column = 2, row = 2)

check_marks = Label(fg = GREEN, bg = YELLOW, font=(FONT_NAME, 15, "bold"))
check_marks.grid(column = 1, row = 3)

window.mainloop()