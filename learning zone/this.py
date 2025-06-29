import tkinter as tk

def say_hello():
    user_input = entry.get()
    label.config(text=f"Hello, {user_input}!")

window = tk.Tk()
window.title("My First App")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Say Hello", command=say_hello)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()
