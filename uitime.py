# Developed by Aleksandr Mack 2022

import tkinter as tk
from datetime import datetime
import pyautogui as pg

i = 0
id = ""


def dragged(event):
    cx, cy = pg.position()
    # wx, wy = window.winfo_x(), window.winfo_y()
    window.geometry('%dx%d+%d+%d' % (172, 92, cx, cy))


# Window settings
root = tk.Tk()
window = tk.Toplevel(root)
root.title('UITimer')
root.attributes('-alpha', 0.0)
root.attributes('-topmost', True)
root.iconify()

window.geometry('172x92')
window.attributes('-topmost', True)
window.overrideredirect(1)
window.bind('<B1-Motion>', dragged)


def popup(event):
    menu.post(event.x_root, event.y_root)


def tick():
    global i, id
    f_out = datetime.utcfromtimestamp(i).strftime("%H:%M:%S")
    i += 1
    display.config(text=str(f_out))
    id = window.after(1000, start)


def start():
    if start_button["state"] == "normal":
        start_button["state"] = "disabled"
        pause_button["state"] = "normal"
        reset_button["state"] = "normal"
    tick()


def pause():
    global id
    window.after_cancel(id)
    if start_button["state"] == "disabled":
        start_button["state"] = "normal"
        pause_button["state"] = "disabled"
        reset_button["state"] = "normal"


def reset():
    global i, id
    root.after_cancel(id)
    if start_button["state"] == "disabled":
        start_button["state"] = "normal"
    reset_button["state"] = "disabled"
    pause_button["state"] = "disabled"
    i = 0
    f_out = datetime.utcfromtimestamp(i).strftime("%H:%M:%S")
    display.config(text=str(f_out))


def exit():
    root.destroy()


# Window frontend
playimg = tk.PhotoImage(file="play.png")
pauseimg = tk.PhotoImage(file="pause.png")
refreshimg = tk.PhotoImage(file="refresh.png")

display = tk.Label(window, text="00:00:00", font=("System", 20))
start_button = tk.Button(window, image=playimg, command=start)
pause_button = tk.Button(window, image=pauseimg, command=pause)
reset_button = tk.Button(window, image=refreshimg, command=reset)
menu = tk.Menu(tearoff=0)
menu.add_command(label="Exit", command=exit)

window.bind('<Button-3>', popup)

display.grid(row=0, rowspan=1, column=0, columnspan=3)
start_button.grid(row=1, column=0, padx=0, ipady=11, sticky="e,w,n,s")
pause_button.grid(row=1, column=1, padx=0, ipady=11, sticky="e,w,n,s")
reset_button.grid(row=1, column=2, padx=0, ipady=11, sticky="e,w,n,s")

pause_button["state"] = "disabled"
reset_button["state"] = "disabled"

window.mainloop()
