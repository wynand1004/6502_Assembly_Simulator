asm = """
LDA $C0
LDA #$01
STA $400
INC $1003
TAX
INX
TXA
CMP #$0f
BEQ $1012
JMP $1002
LDA #$01
NOP
JMP $1002
"""

def convert_asm_to_opcodes(asm):


	memory = []
	opcodes = {
		"TAX": 0xe8,
		"TXA": 0x1a,
		"INX": 0xe8,
		"NOP": 0xea
	}

	import re

	lines = re.split('\n', asm)

	for line in lines:
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

			elif token == "JMP":
				if mode == "absolute":
					memory.append(0x4c)
				elif mode == "indirect":
					memory.append(0x6c)				


		else:
			print("Parsing Error: {}".format(line))

		# Temp output
		print("{: <20}; {: <3} {: <10} {: <10}".format(line, token, mode, value))


	print("")
	#print(memory)
	return memory



# For testing purposes
if __name__ == "__main__":
	memory = convert_asm_to_opcodes(asm)
	print(memory)