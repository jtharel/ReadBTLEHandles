#!/usr/bin/python
import sys
import subprocess
import binascii

def Help():
    print("Usage:")
    print("  read_all_handles.py [Remote Bluetooth Hardware Address]")
    print(" ")
    print("  read_all_handles.py 00:01:02:03:04:05")


def Gatttool(HWADDR):
    print("BTLE Hardware addresss: " + HWADDR)
    proc = subprocess.Popen(["gatttool", "-b", HWADDR, "--char-desc"], stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        print("*"*50)
        if line != '':
            handle = line[9:15]
            print("Handle: " + handle)
            newproc = subprocess.Popen(["gatttool", "-b", HWADDR, "--char-read", "-a", handle], stdout=subprocess.PIPE)
            while True:
                newline = newproc.stdout.readline()
                newline = newline.rstrip()
                if newline != '':
                    print(newline)
                    ascii = binascii.unhexlify(newline[32:].replace(" ", ""))
                    print("Ascii: " + ascii)
                    
                else:
                    break

        else:
            break



if len(sys.argv[1]) != 17:
    Help()
else:
    HWADDR = sys.argv[1]
    Gatttool(HWADDR)

