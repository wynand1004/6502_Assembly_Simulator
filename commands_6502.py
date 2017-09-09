
commands = {

	# Start of ADC
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
	# End of ADC

	# Start of BPL
	"BPL":{
		
		0x10:{
			"mode":"",
			"length": 1,
			"cycles": 3
		}
		
	} 
	# End of BPL
		
}

# For testing purposes only
import os
os.system("clear")

for command in commands:
	for hex in commands[command]:
		mode = commands[command][hex]['mode']
		length = commands[command][hex]["length"]
		cycles = commands[command][hex]["cycles"]
		print("Command: {} Op Code: {} Mode: {:10s}  Length: {}  Clock Cycles: {}".format(command, hex, mode, length, cycles))
	
	print("")	
		
		
		
		
		
		
		