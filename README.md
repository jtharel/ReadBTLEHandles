# ReadBTLEHandles
Read all handles on a BTLE device

read_all_handles.py is a Python script that utilizes the excellent gatttool utility to read all handles on a Bluetooth Low Energy (BTLE) device and automatically convert the hex values to ascii.

## Requirements
` gatttool and a working BTLE dongle `
  


## Usage 
Sample output against a Nike+ FuelBand:

`# read_all_handles.py 00:01:02:03:04:05 

Handle:  0x0001
Characteristic value\/descriptor:   00 18 
Ascii:  
************************************************** 
Handle:  0x0002
Characteristic value\/descriptor:   02 03 00 00 2a 
Ascii: * 
************************************************** 
Handle:  0x0003
Characteristic value\/descriptor:   4e 69 6b 65 2b 20 46 75 65 6c 42 61 6e 64 20 53 45 
Ascii: Nike+ FuelBand SE 
************************************************** 
Handle:  0x0004
Characteristic value\/descriptor:   02 05 00 01 2a 
Ascii: * 
************************************************** 
Handle:  0x0005
Characteristic value\/descriptor:   80 00 
Ascii: ? 
************************************************** 
Handle:  0x0006
Characteristic value\/descriptor:   01 18 
Ascii:  
************************************************** 
Handle:  0x0007
Characteristic value\/descriptor:   0a 18 
Ascii:  
************************************************** 
Handle:  0x0008
Characteristic value\/descriptor:   02 09 00 29 2a 
Ascii: 	)* 
************************************************** 
Handle:  0x0009
Characteristic value\/descriptor:   4e 69 6b 65 
Ascii: Nike 
************************************************** 
Handle:  0x000a
Characteristic value\/descriptor:   02 0b 00 24 2a 
Ascii: 
       $* 
************************************************** 
Handle:  0x000b
Characteristic value\/descriptor:   46 42 53 45 
Ascii: FBSE 
**************************************************
`
