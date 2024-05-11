# BareMetal-HTB-writeup

* First thing you should do is to read challenge description. You will find name of microcontroller from which you received firmware dump.
* Then you should google about .hex files and try to disassemble it with avr-ob***** tool and save terminal output.
* Lateral steps of solving includes reading datsheets and instructions sets of microcontroller, but there are only 2 instructions that you should understand well.
* When you decide what microcontroller do with these instructions, write a python script to extract 0 and 1, decode them with python or CyberChef.

I've attached Python script which decodes flag but not the disassembled firmware itself! 

#HINT:

- microcontroller do some I/O operations to bitbang data
