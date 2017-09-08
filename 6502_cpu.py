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
		
		#INX
		if value == 0xe8:
			self.x += 0x01
			if self.x > 0xff:
				self.x = 0x00
				self.carry_flag = True
			self.pc += 0x01
		
		#INY
		if value == 0xc8:
			self.y += 0x01
			if self.y > 0xff:
				self.y = 0x00
				self.carry_flag = True		
			self.pc += 0x01


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
