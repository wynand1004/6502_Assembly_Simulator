# 6502_Assembly_Simulator
A Simple Simulator for students to use to learn 6502 Assembly Language.  

It is a work in progress and nowhere near complete.

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
