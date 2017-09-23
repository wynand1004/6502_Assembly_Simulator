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
		
		#Opcode Length
		self.opcode_length = {0: 1, 192: 2, 132: 2, 5: 2, 134: 2, 136: 1, 9: 2, 138: 1, 140: 3, 13: 3, 142: 3, 237: 3, 16: 2, 152: 1, 56: 1, 24: 1, 154: 1, 133: 2, 160: 2, 176: 2, 162: 2, 164: 2, 165: 2, 166: 2, 96: 1, 168: 1, 169: 2, 170: 1, 172: 3, 173: 3, 174: 3, 48: 2, 200: 1, 184: 1, 88: 1, 186: 1, 76: 3, 64: 1, 32: 3, 196: 2, 197: 2, 198: 2, 72: 1, 201: 2, 202: 1, 204: 3, 205: 3, 206: 3, 141: 3, 80: 2, 248: 1, 216: 1, 229: 2, 224: 2, 144: 2, 228: 2, 101: 2, 230: 2, 232: 1, 105: 2, 234: 1, 236: 3, 109: 3, 238: 3, 112: 2, 104: 1, 108: 3, 233: 2, 120: 1, 0xc9: 2, 0xf0: 2}

	def get_location(self, low, high = 0x00):
		return (high * 0x100) + low

	def convert_unsigned_to_signed(self, value):
		"""Converts an unsigned integer to a signed integer"""
		#
		#
		#
		# NOT IMPLEMENTED
		#
		#
		#
		return value

	def trace(self, msg):
		print(msg)

	def tick(self, memory):
		opcode = memory[self.program_counter]

		# Get the length of the opcode_offset for the next command
		# This should be 0 for jmp, jsr, ret

		opcode_offset = self.opcode_length[opcode]

		# LDA Immediate
		if opcode == 0xa9:
			self.a = memory[self.program_counter + 0x01]

			if self.a == 0:
				self.zero = True
			else:
				self.zero = False

			self.trace("LDA {}".format(self.a))

		# STA Absolute
		elif opcode == 0x8d:
			location = self.get_location(memory[self.program_counter + 0x01], memory[self.program_counter + 0x02])
			
			memory[location] = self.a

			self.trace("STA {}".format(location))

		# LDX Immediate
		elif opcode == 0xa2:
			self.x = memory[self.program_counter + 0x01]

			self.trace("LDX {}".format(self.x))

		# STX Absolute
		elif opcode == 0x8e:
			location = self.get_location(memory[self.program_counter + 0x01], memory[self.program_counter + 0x02])
			
			memory[location] = self.x

			self.trace("STX {}".format(location))

		# INC Absolute
		elif opcode == 0xee:
			location = self.get_location(memory[self.program_counter + 0x01], memory[self.program_counter + 0x02])
			
			value = memory[location]						
			
			value += 0x01
			
			if value > 0xff:
				value = 0x00

			memory[location] = value

			self.trace("INC {}".format(location))

		# INX
		elif opcode == 0xe8:
			self.x += 0x01

			if self.x > 0xff:
				self.x = 0x00

			self.trace("INX")

		# INY
		elif opcode == 0xc8:
			self.y += 0x01

			if self.y > 0xff:
				self.y = 0x00	
			
			self.trace("INY")

		# JMP Absolute
		elif opcode == 0x4c:
			location = self.get_location(memory[self.program_counter + 0x01], memory[self.program_counter + 0x02])
			self.program_counter = location

			# Do not change PC by opcode length
			opcode_offset = 0

			self.trace("JMP {}".format(location))
			
		# TAX
		elif opcode == 0xAA:
			self.x = self.a
			
			self.trace("TAX")
			
		# TXA
		elif opcode == 0x8A:
			self.a = self.x
			
			self.trace("TXA")
		
		# DEX
		elif opcode == 0xCA:
			self.x -= 0x01

			if self.x < 0x00:
				self.x = 0xff
			
			self.trace("DEX")
		
		# TAY
		elif opcode == 0xA8:
			self.y = self.a

			self.trace("TAY")
		
		# TYA
		elif opcode == 0x98:
			self.a = self.y
			
			self.trace("TYA")
			
		# DEY
		elif opcode == 0x88:
			self.y -= 0x01		

			if self.y < 0x00:
				self.y = 0xff
			
			self.trace("DEY")

		# CLC
		elif opcode == 0x18:
			self.carry = False		
			
			self.trace("CLC")
		
		# SEC
		elif opcode == 0x38:
			self.carry = True		
			
			self.trace("SEC")
			
		# CLI
		elif opcode == 0x58:
			self.interrupt = False		
			
			self.trace("CLI")
			
		# SEI
		elif opcode == 0x78:
			self.carry = True		
			
			self.trace("SEI")
			
		# CLV
		elif opcode == 0xB8:
			self.overflow = False		
			
			self.trace("CLV")
		
		# CLD
		elif opcode == 0xD8:
			self.decimal = False		
			
			self.trace("CLD")
		
		# SED
		elif opcode == 0xF8:
			self.decimal = True		

			self.trace("SED")
			
		# NOP
		elif opcode == 0xEA:

			self.trace("NOP")

		# CMP Immediate CMP #0xff
		elif opcode == 0xC9:
			value = memory[self.program_counter + 0x01]
			if value == self.a:
				self.zero = True
			elif value > self.a:
				self.carry = True

			self.trace("CMP {}".format(value))

		# BNE
		elif opcode == 0xD0:
			pass

		# BEQ
		elif opcode == 0xF0:
			if self.zero == True:
				# Get the value of the offset
				value = memory[self.program_counter + 0x01]
				# Convert that to a positive or negative number
				branch_offset = self.convert_unsigned_to_signed(value)
				# Update the program counter
				self.program_counter += branch_offset
				
				self.trace("BEQ Offset: {}".format(branch_offset))

			else:
				self.trace("BEQ: NOT EQUAL")

		# Set the PC to the new location
		self.program_counter += opcode_offset


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
