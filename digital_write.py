import serial
import time

# Establish serial connection with Arduino
ser = serial.Serial('COM4', 9600, timeout=1)

# Create a new text file to write data
filename = "output"
f = open(filename + ".txt", "w")

# Read data from Arduino and write to text file
while True:
    ldr_value = ser.readline().decode().strip()
    print(ldr_value)
    if ldr_value:
        if int(ldr_value) > 812:
            f.write("1")
        else:
            f.write("0")
        f.flush()  # flush the buffer to ensure data is written immediately
