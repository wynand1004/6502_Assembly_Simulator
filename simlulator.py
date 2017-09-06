#Testing for Simulated Computer

import tkinter
import random

root = tkinter.Tk()
root.title("6502 Assembler Simulator")


class Display(object):
	def __init__(self):
		self.canvas = tkinter.Canvas(root, width=320, height=240)
		self.canvas.pack()
		
		self.start_of_video_memory = 1024
		self.start_of_characater_memory = 2048
		self.colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]
		
		
	def update(self):
		# Clear canvas
		self.canvas.delete("all") 	
	
		# Draw 32 x 24 Squares (10 x 10)
		for x in range(0, 32):
			for y in range(0, 24):
				m = self.start_of_video_memory + (y * 24) + (x * 32)
				color = self.colors[memory[m]]
				self.canvas.create_rectangle(x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill=color)	
		
		# Update
		root.update()

		# Wait 30 ms and do it again
		root.after(30, self.update)

display = Display()

# Memory
memory = []
for _ in range(0, 65535):
	memory.append(random.randint(0, 7))

#root.after(50, draw_random_colors)
root.after(50, display.update)

root.mainloop()