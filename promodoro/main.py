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
    window.after_cancel(timer)
    canva.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_Sec = LONG_BREAK_MIN * 60
    if reps % 8 ==0:
        countdown(long_break_Sec)
        title_label.config(text="Break", fg=RED)
    if reps % 2 ==0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 0:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"
    canva.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
            check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canva = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canva.create_image(100, 112, image=image)
timer_text = canva.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35 ,"bold" ))
canva.grid(column=1, row=1)


start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0 , row=2)

reset_button = Button(text="Reset", highlightthickness=0 ,command=reset_timer)
reset_button.grid(column=2, row=2)

check = Label(text="", fg=GREEN, bg=YELLOW)
check.grid(column = 1, row=3)

window.mainloop()
