asm = """
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

import re

lines = re.split('\n', asm)

for line in lines:
	mode = ""
	tokens = re.split(' ', line.strip())

	if len(tokens) == 1:
		# Deal with single length opcodes first
		token = tokens[0].strip()

		if token == "TAX":
			print("0xe8")
		elif token == "TXA":
			print("0x1a")

	elif len(tokens) == 2:
		
		# Decide addressing mode
		value = tokens[1].strip()

		# Check to see if the first character is a # or $
		if value[0] in "$0123456789":
			mode = "direct"
			if value[0] == "$":
				value = value[1:]
				
		elif value[0] == "#":
			mode = "immediate"
			if value[1] == "$":
				value = value[2:]
			else:
				value = value[1:]	

		# Temp output
		print(mode)
		print (value)	
	else:
		print(token)
	