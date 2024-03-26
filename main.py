from tkinter import *

RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
timer_value = None # Value is set by the 5 & 10 second button functions.
timer = 5

### Functions ###
def set_five_seconds():
    """Sets the countdown timer to start from 10 seconds."""
    global timer, timer_value
    timer_value = 5
    timer = 5
    canvas.itemconfig(timer_text, text="5")


def set_ten_seconds():
    """Sets the countdown timer to start from 5 seconds. Default starts timer at 5 seconds."""
    global timer, timer_value
    timer_value = 10
    timer = 10
    canvas.itemconfig(timer_text, text="10")

def reset():
    """Resets the countdown timer and text on-screen. Buttons and text entry is also re-enabled. Can be ran while timer is running or at 0."""
    global timer
    textbox.delete("1.0", END) # Clears textbox
    window.after_cancel(timer)
    countdown_label.config(text="Countdown Duration", fg=GREEN)
    ten_sec_button.config(command=set_ten_seconds) 
    five_sec_button.config(command=set_five_seconds)
    canvas.itemconfig(timer_text, text=f"{timer_value}") 
    textbox.config(state="normal") # Re-enables text box
    textbox.bind("<KeyPress>", key_pressed) # Re-enables bind
    timer = 5


def start_timer():
    """Starts countdown timer."""
    textbox.config(state="normal")
    count_down(timer)
    ten_sec_button.config(command="") # Disable button
    five_sec_button.config(command="") # Disable button


def count_down(seconds):
    """Countdown mechanism. If at 0, text disappears and app key entry is disabled."""
    global timer
    canvas.itemconfig(timer_text, text=seconds)
    if seconds == 0:
        countdown_label.config(text="Oh no... time is up!", fg=RED)
        textbox.unbind("<KeyPress>") # Disable bind 
        textbox.delete("1.0", END) # Clear text
        textbox.config(state="disabled") # Disable text box
    if seconds > 0:
        timer = window.after(1000,count_down, seconds -1)
        textbox.bind("<KeyPress>", key_pressed)


def key_pressed(event):
    """Listens for key presses. When keystroke is detected, timer is reset to the specified countdown value and countdown is restarted."""
    global timer
    if timer_value == 10:
        window.after_cancel(timer)
        timer = 10
        start_timer()
    else:
        window.after_cancel(timer)
        timer = 5
        start_timer()


### GUI INTERFACE ###
# Window Setup
window = Tk()
window.title("Tkinter Disappearing Text Application")
window.config(padx=20, pady=20, bg=YELLOW, highlightthickness=0)
window.minsize(height=800, width=800)

# Canvas Setup
canvas = Canvas(width=100, height=100, bg=YELLOW)
timer_text = canvas.create_text(50, 50, text="5", fill=RED, font=(FONT_NAME, 45, "bold"))
canvas.place(x=330, y=50)

# Select contdown label
countdown_label = Label(text="Countdown Duration", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
countdown_label.place(x=150, y=20)
#Text Entry label
typing_label = Label(text="Start Typing to begin countdown", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
typing_label.place(x=0, y=200)

# Five seconds button
five_sec_button = Button(text="5 Seconds", highlightthickness=0, command=set_five_seconds)
five_sec_button.place(x=300, y=160)

# Ten seconds button
ten_sec_button = Button(text="10 Seconds", highlightthickness=0, command=set_ten_seconds)
ten_sec_button.place(x=400, y=160)

# Reset button
reset = Button(text="Reset", highlightthickness=0, command=reset)
reset.place(x=0, y=720)

# Text Box
textbox = Text(width=75, height=25, font=(FONT_NAME))
textbox.place(x=0, y=240)
textbox.bind("<KeyPress>", key_pressed)

window.mainloop()