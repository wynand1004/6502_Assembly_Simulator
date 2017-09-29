# 6502_Assembly_Simulator
A Simple Simulator for students to use to learn 6502 Assembly Language.  

It is a work in progress and nowhere near complete.

# Implementation Details
The program is a simulation of a computer running a 6502 CPU.  There is a 32x24 graphics display capable of displaying 16 colors, and a 40x5 text display. Graphics memory starts from 1024 ($0400), and text memory starts at 2048 ($0800). Execution begins at 4096 ($1000).  The text display displays standard ASCII characters - no unicode or double-byte characters.

Color List:

0 black

1 white

2 red

3 cyan

4 purple

5 green

6 blue

7 yellow

8 orange

9 brown

10 pink

11 darkgrey

12 grey

13 lightgreen

14 lightblue

15 lightgrey
		

Currently, there is no assembler to convert the assembly code to machine code (although this feature is planned). Code must be added manually to the simulator.py file.

Here is the current sample code:

memory[4096] = 0xa9 # LDA #0x01

memory[4097] = 0x02

memory[4098] = 0x8d # STA 0x400

memory[4099] = 0x00

memory[4100] = 0x04

memory[4101] = 0xee # INC 0x1003 (4099)

memory[4102] = 0x03 

memory[4103] = 0x10 

memory[4104] = 0xaa # TAX 

memory[4105] = 0xe8 # INX 

memory[4106] = 0x8a # TXA 

memory[4107] = 0xc9 # CMP #0x0f

memory[4108] = 0x0f

memory[4109] = 0xd0 # BNE (Jump ahead back 13 memory locations from start of next instruction)

memory[4110] = 0xf3 

memory[4111] = 0xea # NOP NOP NOP

memory[4112] = 0xea

memory[4113] = 0xea

memory[4114] = 0xa9 # LDA #0x01

memory[4115] = 0x01

memory[4116] = 0xea # NOP

memory[4117] = 0x4c # JMP 0x1002 (4097)

memory[4118] = 0x02

memory[4119] = 0x10

## Implemented Instructions
LDA (Immediate)

STA (Absolute)

LDX (Immediate)

STX (Absolute)

INC (Absolute)

INX

INY

JMP (Absolute)

TAX

TXA

DEX

TAY

TYA

DEY

CLC

SEC

CLI

SEI

CLV

CLD

SED

NOP

CMP (Immediate)

BEQ

BNE


# To Try It Out
 - Download the repository and run simulator.py using Python 2 or Python 3
 - You should see a number of different colored pixels (squares) appear row by row in the top half of the display.

# Known Issues
 - For some reason, the display can freeze on Mac. This is a known bug in tkinter on the Mac. Interestingly, it occurs when the background of the tkinter canvas is black along with the rectangles used as "pixels". Changing the pixel color to all white, or all green, for example seems to alleviate the issue. 
