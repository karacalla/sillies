import tkinter as tk
import random
import time
import tkinter.font as tkFont
from tkinter import ttk
from shinybuttonremake import textwizard

root = tk.Tk()
# messing around with display
x_offset = 0
y_offset = 0
x_coeff = 1
y_coeff = 1
width = 600
height = 400
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.minsize(600, 400)
root.maxsize(900,600)
root.iconbitmap('bergentruck_caine.ico')


def buttontime():
    root.title('Welcome back my Skibidi Sigmas!')

    # find the center point
    center_x = int(screen_width / 2 - width / 2)
    center_y = int(screen_height / 2 - height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{width}x{height}+{center_x}+{center_y}')
 
    message = tk.Label(root, text="insert text here")
    message.pack()
    cooltext = tk.StringVar()
    entry_color = ttk.Entry(root, textvariable = cooltext)
    entry_color.pack()
    entry_color.focus()

    output_label = ttk.Label(root)
    output_label.pack()
    
    entry_color.bind('<Return>', lambda event: textwizard(event.widget.get()))




buttontime()

def skibidiware():
    root.title('skibidi virus')
    message = tk.Label(root, text="you have a virus, pay 15 gazillion dollars now")
    message.pack()

    bold_font = tkFont.Font(weight="bold")
    button = tk.Button(root, text="Je paie $15ga", fg="red", font="bold_font")
    button.pack()

root.attributes('-alpha',1)

def DVD_icon():
    while True:
        if x_offset == screen_width - width:
            x_coeff = -1
        if x_offset == 0:
            x_coeff = 1    
        if y_offset == screen_height - height :
            y_coeff = -1
        if y_offset == 0:
            y_coeff = 1
        x_offset = x_offset + x_coeff
        y_offset = y_offset + y_coeff
        root.geometry(f"{width}x{height}+{x_offset}+{y_offset}")  
        root.update()
        time.sleep(0.01)



root.mainloop()
