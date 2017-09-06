#Testing for Simulated Computer

import tkinter
import random

root = tkinter.Tk()
root.title("6502 Assembler Simulator")

screen = tkinter.Canvas(root, width=320, height=240)
screen.pack()

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]

def draw_random_colors():
    # Clear canvas
    screen.delete("all") 

    # Draw 32 x 24 Squares (10 x 10) with random colors
    for x in range(0, 32):
        for y in range(0, 24):
            color = random.choice(colors)
            screen.create_rectangle(x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill=color)    

    # Show changes
    root.update()

    # Wait 30 ms and do it again
    root.after(30, draw_random_colors)

root.after(50, draw_random_colors)

root.mainloop()