import time
from tkinter import *

# from playsound import playsound

window = Tk()
window.title("Timer")
window.geometry("400x700+500+100")
window.config(bg="#24354f")
window.resizable(False, False)

window_icon = PhotoImage(file="Icons/countdown timer.png")
window.iconphoto(False, window_icon)

heading = Label(window, text="Timer", font="Arial 20 bold", bg="#24354f", fg="#FFFFFF")
heading.pack(pady=10)

# clock
Label(window, font="Arial 15 bold", text="current time: ", bg="khaki").place(x=65, y=70)


def clock():
    clock_time = time.strftime("%I:%M:%S %p")
    current_time.config(text=" " + clock_time + " ")
    current_time.after(1000, clock)


current_time = Label(window, font="Arial 15 bold", text="", fg="#000", bg="#fff")
current_time.place(x=190, y=70)
clock()

hours = StringVar()
Entry(window, textvariable=hours, width=2, font="Arial 50", fg="#fff", bg="#24354f", bd=0).place(x=30, y=155)
hours.set("00")

minutes = StringVar()
Entry(window, textvariable=minutes, width=2, font="Arial 50", fg="#fff", bg="#24354f", bd=0).place(x=150, y=155)
minutes.set("00")

seconds = StringVar()
Entry(window, textvariable=seconds, width=2, font="Arial 50", fg="#fff", bg="#24354f", bd=0).place(x=270, y=155)
seconds.set("00")

Label(window, text="hours", font="Arial 12", bg="#24354f", fg="#fff").place(x=105, y=200)
Label(window, text="min", font="Arial 12", bg="#24354f", fg="#fff").place(x=225, y=200)
Label(window, text="sec", font="Arial 12", bg="#24354f", fg="#fff").place(x=345, y=200)


def timer():
    times = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    while times > -1:
        minute, second = (times // 60, times % 60)
        # hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
            seconds.set(second)
            minutes.set(minute)
            hours.set(hour)

            window.update()
            time.sleep(1)

            if times == 0:
                # playsound("ringtone.wav")
                seconds.set("00")
                minutes.set("00")
                hours.set("00")

            times -= 1


start_button = Button(window, text="START", bg="red", fg="#fff", width=20, height=2, font="Arial 10 bold",
                      command=timer)
start_button.pack(padx=5, pady=40, side=BOTTOM)

window.mainloop()


# This program is not complete, needs to be finished
