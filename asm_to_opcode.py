asm = """
LDA #$02
STA $400
INC $1003
TAX 
INX 
TXA 
CMP #$0f
BNE 4098
NOP
NOP
NOP
LDA #$01
NOP
JMP $1002 
"""

def get_little_endian(value):
	# Convert value to hex string
	value = hex(value)
	# Remove 0x
	value = value[2:]
	# Get the last 2 digits
	little = value[-2:]
	# Get the first 2 digits
	big = value[:-2]
	# Convert to ints
	little = int(little, 16)
	big = int(big, 16)

	# Return result as a list
	return [little, big]

def convert_asm_to_opcodes(asm, start_of_execution):
	current_memory_location = start_of_execution

	memory = []
	opcodes = {
		"TAX": 0xaa,
		"TXA": 0x8a,
		"INX": 0xe8,
		"NOP": 0xea
	}

	import re

	lines = re.split('\n', asm)

	for line in lines:

		# Remove comments
		if ";" in line:
			index = line.index(";")
			line = line[:index].strip()

		mode = ""
		value = ""
		tokens = re.split(' ', line.strip())

		if len(tokens) == 1:
			mode = "implied"
			
			# Deal with single length opcodes first
			token = tokens[0].strip().upper()

			if token == "\n" or token == "":
				continue
			elif token == "TAX":
				memory.append(opcodes[token])
			elif token == "TXA":
				memory.append(opcodes[token])
			elif token == "INX":
				memory.append(opcodes[token])
			elif token == "NOP":
				memory.append(opcodes[token])

			current_memory_location += 1

		elif len(tokens) > 1:
			# Set the token
			token = tokens[0].strip().upper()
			# Decide addressing mode
			value = tokens[1].strip()

			# Check to see if the first character is a # or $
			if value[0] in "$0123456789":
				mode = "absolute"
				if value[0] == "$":
					value = value[1:]
					# Convert to hex value
					value = int(value, 16)
				else:
					# Convert to decimal value
					value = int(value, 10)	
				
				# Check for zero page mode
				if value <= 255:
					mode = "zeropage"
					
			elif value[0] == "#":
				mode = "immediate"
				if value[1] == "$":
					value = value[2:]
					# Convert to hex value
					value = int(value, 16)
				else:
					value = value[1:]
					# convert to decimal value
					value = int(value, 10)	

			if token == "LDA":
				if mode == "immediate":
					memory.append(0xa9)
				elif mode == "zeropage":
					memory.append(0xa5)
				elif mode == "absolute":
					memory.append(0xad) 
			
			elif token == "STA":
				if mode == "zeropage":
					memory.append(0x85)
				elif mode == "absolute":
					memory.append(0x8d)				

			elif token == "INC":
				if mode == "zeropage":
					memory.append(0xe6)
				elif mode == "absolute":
					memory.append(0xee)

			elif token == "CMP":
				if mode == "immediate":
					memory.append(0xc9)
				elif mode == "zeropage":
					memory.append(0xc5)
				elif mode == "absolute":
					memory.append(0xcd) 

			elif token == "BEQ":
				memory.append(0xf0)
				mode = "relative"

			elif token == "BNE":
				memory.append(0xd0)
				mode= "relative"

			elif token == "JMP":
				if mode == "absolute":
					memory.append(0x4c)
				elif mode == "indirect":
					memory.append(0x6c)				


		else:
			print("Parsing Error: {}".format(line))


		# Add the correct values
		if mode == "zeropage":
			memory.append(value)
			current_memory_location += 2
		elif mode == "immediate":
			memory.append(value)
			current_memory_location += 2
		elif mode == "absolute":
			address = get_little_endian(value)
			# print(mode, address)
			memory += address
			current_memory_location += 3
		# Use for branches - not a real mode
		elif mode == "relative":
			# Calculate the offset (must add plus 2 as it is calculated from start of next instruction)
			offset = value - current_memory_location -2
			print(offset)
			if offset < 0:
				offset += 256
			memory.append(offset)
			current_memory_location += 3
		
		# Temp output
		print("{: <20}; {: <3} {: <10} {: <10} {}".format(line, token, mode, value, current_memory_location))


	print("")
	#print(memory)
	return memory



# For testing purposes
if __name__ == "__main__":
	import os
	os.system("clear")
	print("Compile ASM to 6502 Opcodes\n")
	memory = convert_asm_to_opcodes(asm, 4096)
	print(memory)