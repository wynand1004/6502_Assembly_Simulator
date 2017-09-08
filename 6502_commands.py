
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
		
	} 
	# End of ADC


		
}

# For testing purposes only
import os
os.system("clear")

for command in commands:
	for hex in commands[command]:
		mode = commands[command][hex]['mode']
		length = commands[command][hex]["length"]
		cycles = commands[command][hex]["cycles"]
		print("Command: {}  Mode: {:10s}  Length: {}  Clock Cycles: {}".format(command, mode, length, cycles))
	
	print("")	
		
		
		
		
		
		
		