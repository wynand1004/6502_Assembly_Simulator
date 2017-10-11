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

memory = []
opcodes = {
	"TAX": 0xe8,
	"TXA": 0x1a
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

	elif len(tokens) == 2:
		# Set the token
		token = tokens[0].strip().upper()
		# Decide addressing mode
		value = tokens[1].strip()

		# Check to see if the first character is a # or $
		if value[0] in "$0123456789":
			mode = "direct"
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

	else:
		print("Parsing Error: {}".format(line))

	# Temp output
	print("{: <20}; {: <3} {: <10} {: <10}".format(line, token, mode, value))


print("")
print(memory)
	