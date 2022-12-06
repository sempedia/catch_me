# Catch me if you can! - simple game using tkinter and Pyhton
# 
#
# The rules are:
#
# - The game goes on between TkInter and the user.
# - We have a 500x500 pixel main window with a button inside named 'Catch me!'.
# - The button is located in the top-left corner of the window.
# - If the user moves the mouse cursor over the button, the button immediately
# jumps to another location inside the window.
# - The button must not cross the window's boundaries during the jump!
#
# Enjoy the game!



import tkinter as tk
import random

# Set the new random locations of the 'Catch me!' button
# when the cursor of the mouse moves over the button.
def new_locations(xy):
    new_location = random.randint(1, 440)
    while abs(xy - new_location) < 50:
        new_location = random.randint(1, 440)
    return new_location

# Set the behaviour of the 'Catch me!' button
# when the cursor of the mouse moves over the button.
def mouse_over(event):
    global x, y
    x = new_locations(x)
    y = new_locations(y)
    catch_button.place(x=x, y=y)

# Create the main window and
# set its dimensions (width and height) at 500x500 using geometry() method.
win = tk.Tk()
win.geometry('500x500')

# Create Title of the Aplicattion:
blank_space = ' '
win.title(60 * blank_space + 'Catch me!')

# Create the 'Catch me!' button and bind the callback to it
# so the button moves randomly in our new locations
# every time the mouse is over it.
catch_button = tk.Button(win, text="Catch me!")
catch_button.bind('<Enter>', mouse_over)
x = y = 10
catch_button.place(x=x, y=y)

# Create a random number based on the seed value choosed
random.seed()

# Display the Aplication and then end it.
win.mainloop()
