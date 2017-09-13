
commands = {

	#Start of ADC
	"ADC":{
		
		0x69:{
			"mode":"immediate",
			"length": 2,
			"cycles": 2
		},
	
		0x65 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0x6d : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 
	
	#End of ADC
	#Start of Branch Instructions
	#For these, it says it's two machine cycles if branch isn't taken, +1 if it is, +1 more 
	#if the branch crosses a page boundary. I just put 2 for them, but this was what I was talking about
	#in class.
	"BPL":{
		
		0x10:{
			"mode":"relative",
			"length": 2,
			"cycles": 2
		
		}
		
	},
		
	"BMI":{
		
		0x30:{
			"mode":"relative",
			"length": 2,
			"cycles": 2
			
		}
		
	},
	
	"BVC":{
		
		0x50:{
			"mode":"relative",
			"length": 2,
			"cycles": 2
		
		}

	},
		
	"BVS":{
		
		0x70:{
			"mode":"relative",
			"length": 2,
			"cycles": 2
			
		}
			
	},
	
	"BCC":{
		
		0x90:{
			"mode":"relative",
			"length": 2,
			"cycles": 2
			
		}
	
	},
		
	"BCS":{
		
		0xB0:{
			"mode":"relative",
			"length": 2,
			"cycles": 2
		
		}

	},
	
	#End of AND
	#Start of Break
	"BRK":{
	
		0x00:{
			"mode":"implied",
			"length": 1,
			"cycles": 7
			
		}
		
	},
	
	#End of Break
	#Start of Compare
	"CMP":{
		
		0xC9:{
			"mode":"immediate",
			"length": 2,
			"cycles": 2
		},
	
		0xC5 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0xCD : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 
	#End of Compare Accumulator
	#Start of Compare X Register
	"CPX":{
		
		0xE0:{
			"mode":"immediate",
			"length": 2,
			"cycles": 2
		},
	
		0xE4 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0xEC : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 
	#End of Compare X Register
	#Start of Compare Y Register
	"CPY":{
		
		0xC0:{
			"mode":"immediate",
			"length": 2,
			"cycles": 2
		},
	
		0xC4 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0xCC : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 
	#End of Compare Y Register
	#Start of Decrement Memory
	"DEC":{
	
		0xC6 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 5
		},
		
		0xCE : {
			"mode":"absolute",
			"length": 3,
			"cycles": 6
		}
		
	}, 
	#End of Decrement Memory
	#Start of Flag (Processor Status) Instructions
	"CLC":{
		
		0x18:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"SEC":{
		
		0x38:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"CLI":{
		
		0x58:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"SEI":{
		
		0x78:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"CLV":{
		
		0xB8:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"CLD":{
		
		0xD8:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"SED":{
		
		0xF8:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	#End of Flag (Processor Status) Instructions
	#Start of Increment Memory
	"INC":{
	
		0xE6 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 5
		},
		
		0xEE : {
			"mode":"absolute",
			"length": 3,
			"cycles": 6
		}
		
	}, 
	
	#End of Increment Memory
	#Start of Jump
	"JMP":{
	
		0x4C : {
			"mode":"absolute",
			"length": 3,
			"cycles": 3
		},
		
		0x6C : {
			"mode":"indirect",
			"length": 3,
			"cycles": 5
		}
		
	}, 
	
	#End of Jump
	#Start of Jump to Subroutine
	"JSR":{
		
		0x20 : {
			"mode":"absolute",
			"length": 3,
			"cycles": 6
		}
		
	}, 
	
	#End of Jump to Subroutine
	#Start of Load Accumulator
	"LDA":{
		
		0xA9:{
			"mode":"immediate",
			"length": 2,
			"cycles": 2
		},
	
		0xA5 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0xAD : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 
	
	#End of Load Accumulator
	#Start of Load X Register
	"LDX":{
		
		0xA2:{
			"mode":"immediate",
			"length": 2,
			"cycles": 2
		},
	
		0xA6 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0xAE : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 
	
	#End of Load X Register
	#Start of Load Y Register
	"LDY":{
		
		0xA0:{
			"mode":"immediate",
			"length": 2,
			"cycles": 2
		},
	
		0xA4 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0xAC : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 
	
	#End of Load Y Register
	#Start of No Operation
	"NOP":{
		
		0xEA:{
			"mode":"immediate",
			"length": 1,
			"cycles": 2
			
		}
	
	},
	
	#End of No Operation
	#Start of bitwise OR with Accumulator
	"ORA":{
		
		0x09:{
			"mode":"immediate",
			"length": 2,
			"cycles": 2
		},
	
		0x05 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0x0D : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 
	
	#End of bitwise OR with Accumulator
	#Start of Register Instructions
	"TAX":{
		
		0xAA:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"TXA":{
		
		0x8A:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"DEX":{
		
		0xCA:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"INX":{
		
		0xE8:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"TAY":{
		
		0xA8:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"TYA":{
		
		0x98:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"DEY":{
		
		0x88:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"INY":{
		
		0xC8:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	#End of Register Instructions
	#Start of Return from Interrupt
	"RTI":{
		
		0x40:{
			"mode":"implied",
			"length": 1,
			"cycles": 6

		}
	
	},
	
	#End of Return from Interrupt
	#Start of Return from Subroutine
	"RTS":{
		
		0x60:{
			"mode":"implied",
			"length": 1,
			"cycles": 6

		}
	
	},
	
	#End of Return from Subroutine
	#Start of Subtract with Carry
	"SBC":{
		
		0xE9:{
			"mode":"immediate",
			"length": 2,
			"cycles": 2
		},
	
		0xE5 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0xED : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 
	
	#End of Subtract with Carry
	#Start of Store Accumulator
	"STA":{
		
		0x85 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0x8D : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 
	
	#End of Store Accumulator
	#Start of Stack Instructions
	"TXS":{
		
		0x9A:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"TSX":{
		
		0xBA:{
			"mode":"implied",
			"length": 1,
			"cycles": 2

		}
		
	}, 
	
	"PHA":{
		
		0x48:{
			"mode":"implied",
			"length": 1,
			"cycles": 3

		}
		
	}, 
	
	"PLA":{
		
		0x68:{
			"mode":"implied",
			"length": 1,
			"cycles": 4

		}
		
	}, 
	
	"PHP":{
		
		0xB8:{
			"mode":"implied",
			"length": 1,
			"cycles": 3

		}
		
	}, 
	
	"PLP":{
		
		0xD8:{
			"mode":"implied",
			"length": 1,
			"cycles": 4

		}
		
	}, 
	
	#End of Stack Instructions
	#Start of Store X Register
	"STX":{
		
		0x86 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0x8E : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 

	#End of Store X Register
	#Start of Store Y Register
	"STY":{
		
		0x84 : {
			"mode":"zeropage",
			"length": 2,
			"cycles": 3
		},
		
		0x8C : {
			"mode":"absolute",
			"length": 3,
			"cycles": 4
		}
		
	}, 
	#End of Story Y Register
}

# For testing purposes only
import os
os.system("clear")

for command in commands:
	for hex in commands[command]:
		mode = commands[command][hex]['mode']
		length = commands[command][hex]["length"]
		cycles = commands[command][hex]["cycles"]
		print("Command: {}  Mode: {}  Length: {}  Clock Cycles: {}".format(command, mode, length, cycles))
	
	print("")	
		
		
		
		
		
		
		