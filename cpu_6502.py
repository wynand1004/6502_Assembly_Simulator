class CPU(object):
	def __init__(self, program_counter=0x1000):
		# Create registers
		self.a = 0
		self.x = 0
		self.y = 0
		
		# Create flags
		self.carry = False
		self.decimal = False
		self.interrupt = False
		self.negative = False
		self.overflow = False
		self.zero = False
		
		# Create program counter
		self.program_counter = program_counter
		
		# Create stack pointer
		self.stack_pointer = 0xff
		
	def tick(self, memory):
		
		opcode = memory[self.program_counter]

		#LDA Immediate
		if opcode == 0xa9:
			self.a = memory[self.program_counter + 1]
			self.program_counter += 0x02
			print ("LDA {}".format(self.a))

		#STA Absolute
		if opcode == 0x8d:
			low = memory[self.program_counter + 0x01]
			high = memory[self.program_counter + 0x02]
			location = (high * 0x100) + low
			memory[location] = self.a
			self.program_counter += 0x03
			print("STA {}".format(location))

		#LDX Immediate
		if opcode == 0xa2:
			self.x = memory[self.program_counter + 1]
			self.program_counter += 0x02
			print ("LDX {}".format(self.x))

		#STX Absolute
		if opcode == 0x8e:
			low = memory[self.program_counter + 0x01]
			high = memory[self.program_counter + 0x02]
			location = (high * 0x100) + low
			memory[location] = self.x
			self.program_counter += 0x03
			print("STX {}".format(location))

		#INC Absolute
		if opcode == 0xee:
			low = memory[self.program_counter + 0x01]
			high = memory[self.program_counter + 0x02]
			location = (high * 0x100) + low
			value = memory[location]						
			value += 0x01
			if value > 0xff:
				value = 0x00
			self.carry = True
			memory[location] = value
			self.program_counter += 0x03
			print("INC {}".format(location))

		#INX
		if opcode == 0xe8:
			self.x += 0x01
			if self.x > 0xff:
				self.x = 0x00
				self.carry_flag = True
			self.program_counter += 0x01
		
		#INY
		if opcode == 0xc8:
			self.y += 0x01
			if self.y > 0xff:
				self.y = 0x00
				self.carry_flag = True		
			self.program_counter += 0x01

		#JMP Absolute
		if opcode == 0x4c:
			low = memory[self.program_counter + 0x01]
			high = memory[self.program_counter + 0x02]
			location = (high * 0x100) + low
			self.program_counter = location
			print("JMP {}".format(location))



if __name__ == "__main__":	
	# For testing purposes only
	import os
	os.system("clear")

	cpu = CPU(0x1000)

	print("6502 CPU Simulator")
	print("Registers:")
	print("A: {}".format(cpu.a))
	print("X: {}".format(cpu.x))
	print("Y: {}".format(cpu.y))
	print("")
	print("Flags:")
	print("Carry: {}".format(cpu.carry))
	print("Decimal: {}".format(cpu.decimal))
	print("Interrupt Disable: {}".format(cpu.interrupt))
	print("Negative: {}".format(cpu.negative))
	print("Overflow: {}".format(cpu.overflow))
	print("Zero: {}".format(cpu.zero))
	print("")
	print("Miscellaneous:")
	print("Program Counter: {}".format(cpu.program_counter))
	print("Stack Pointer: {}".format(cpu.stack_pointer))
