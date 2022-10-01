from tkinter import *
import math
import time

def transparancy(c):
    root.attributes('-transparentcolor',"light gray")

def hand():
    canvas.delete("second")
    canvas.delete("minute")

    sec = int(time.strftime("%S"))
    min = int(time.strftime("%M")) \
          + (sec / 60)
    hr = int(time.strftime("%I")) \
         + (min / 60)

    deg1 = -90 + 6 * sec
    rad = math.pi * deg1 / 180
    length = 100
    x_end = x_start + length * \
            math.cos(rad)
    y_end = y_start + length *\
            math.sin(rad)
    canvas.create_line(x_start,
        y_start, x_end, y_end,
        fill="black", width=5,
                tag="second")

    deg2 = -90 + 6 * min
    rad = math.pi * deg2 / 180
    length = 110
    x_end = x_start + length * \
            math.cos(rad)
    y_end = y_start + length * \
            math.sin(rad)
    canvas.create_line(x_start,
        y_start, x_end, y_end,
        fill="blue", width=5,
                tag="minute")

    deg3 = -90 + 30 * hr
    rad = math.pi * deg3 / 180
    length = 90
    x_end = x_start + length * \
            math.cos(rad)
    y_end = y_start + length * \
            math.sin(rad)
    canvas.create_line(x_start,
        y_start, x_end, y_end,
        fill="red", width=5,
                    tag="hour")

    lbl["text"] = time.strftime(
        "%I:%M:%S"
    )
    lbl.update()
    canvas.update()

    canvas.after(200, hand)


START = 300
x_start = START
y_start = START

root = Tk()

root.title("Analog Clock     ---Shivang Srivastava")

root.bind("<Button-1>", transparancy)
root.geometry("600x600+325+50")
root.resizable(FALSE, FALSE)

canvas = Canvas(root, height=600,
    width=600, bg="light gray")
canvas.place(x=0, y=0)

lbl = Label(root, font=("TkTextFont",
    50, "bold"), bg="light gray")
lbl.place(x=180, y=70)

hand()

root.mainloop()
