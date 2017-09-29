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

tokens = re.split(' |\n', asm)

for token in tokens:
	token = token.strip()
	if token == "TAX":
		print("0xe8")
	elif token == "TXA":
		print("0x1a")
	elif len(token) == 0:
		pass
	else:
		print(token)
	