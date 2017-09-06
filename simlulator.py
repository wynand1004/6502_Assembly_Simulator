#Testing for Simulated Computer
import tkinter
import random

root = tkinter.Tk()
root.title("6502 Assembler Simulator")

class Display(object):
	def __init__(self, start_of_video_memory, start_of_character_memory):
		self.canvas = tkinter.Canvas(root, width=320, height=240)
		self.canvas.pack()

		self.label = tkinter.Label(root, width=40, height=5, bg="black", fg="white")
		self.label.pack()		
		
		self.start_of_video_memory = start_of_video_memory
		self.start_of_character_memory = start_of_character_memory
		# Color list based on C64 color chart REF: http://sta.c64.org/cbm64col.html
		self.colors = ["black", "white", "red", "cyan", "purple", "green", "blue", "yellow", "orange", "brown", "pink", "darkgrey", "grey", "lightgreen", "lightblue", "lightgrey"]
		
	def update(self):

		# Update Graphics Canvas
		# Clear canvas
		self.canvas.delete("all") 	
	
		# Draw 32 x 24 Squares (10 x 10 pixels)
		for x in range(0, 32):
			for y in range(0, 24):
				m = self.start_of_video_memory + (y * 32) + (x)
				color = self.colors[memory[m]]
				self.canvas.create_rectangle(x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill=color)	

		# Update text label (40 x 5 Characters)
		text = ""
		for i in range(self.start_of_character_memory, self.start_of_character_memory + 200):
			text += chr(memory[i])
			# Check for eol
			if (i - (self.start_of_character_memory - 1)) % 40 == 0:
				text += "\r"
		
		# Update label
		self.label["text"]=text

		# Update
		root.update()

display = Display(1024, 2048)

# Memory
memory = []
for _ in range(0, 65536):
	memory.append(0)


while True:
	for i in range(1024 + 768):
		memory[i] = random.randint(0, len(display.colors) - 1)

	for i in range(2048, 2248):
		memory[i] = random.randint(65, 90)
		
		
	display.update()
	

root.mainloop()
