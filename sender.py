import serial
import time

# Open a serial connection to the Arduino
ser = serial.Serial('COM4', 9600)

# Prompt the user for the filename of the text file to send
filename = input("Enter the filename of the text file to send: ")

# Open the file for reading
with open(filename, 'r') as file:
    # Loop through the contents of the file
    for line in file:
        # Strip any leading/trailing whitespace from the line
        line = line.strip()
        
        # Send the line over the serial port
        ser.write(line.encode())
        
        # Wait for a short period of time ( this will define the speed of data transfer) ( same for the arduino programs for LED and LDR)
        time.sleep(0.300)

# Close the serial connection
ser.close()
