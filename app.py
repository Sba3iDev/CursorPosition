# Modules
import pyautogui
import pyperclip
from tkinter import *
from tkinter import messagebox

# Create the main app window
app = Tk()
app.iconbitmap("icon/icon.ico")
app.title("Cursor Position")
app.geometry("400x200")
app.resizable(False, False)
app.config(bg="#ffffff")

# Message label
message_label = Label(
    app,
    text="Press [SPACE] to copy coordinates",
    height=2,
    font=("Arial", 13),
    fg="#265d80",
    bg="#ffffff",
)
message_label.pack()


# Update function
def update():
    x_position.configure(text=f"X: {pyautogui.position()[0]}")
    y_position.configure(text=f"Y: {pyautogui.position()[1]}")
    app.after(1, update)


# Copy function
def copy(event):
    pyperclip.copy(f"({pyautogui.position()[0]},{pyautogui.position()[1]})")
    messagebox.showinfo("Cursor Position", "Coordinates copied successfully")


# X postion of cursor
x_position = Label(app, text="", height=2, font=30, fg="#000000", bg="#ffffff")
x_position.pack()

# Y postion of cursor
y_position = Label(app, text="", height=2, font=30, fg="#000000", bg="#ffffff")
y_position.pack()

# Call update function
update()

# Press key event
app.bind("<KeyPress-space>", copy)

# About label
about_label = Label(
    app, text="By Sba3i", height=2, font=("Times", 13), fg="#aa4f4f", bg="#ffffff"
)
about_label.pack(side="right")

# Running app
app.mainloop()
