


:::::::::::::::::::::::::::::::::::::::::::::::::::------------------------ PC-to-PC-File-tranfer-using-LiFi ----------------------------::::::::::::::::::::::::::::::::::::::::::::::::::::



In this project, LiFi technology was used to transfer files of different formats between two laptops. The files were first converted into text files containing 0s and 1s using Python code. The text file was then transmitted through an LED and detected by a light sensor (LDR) connected to a different Arduino board and laptop. The data was then converted back into its original format. Overall, the project demonstrated the versatility of LiFi technology for transferring different types of data. It also showed the usefulness of Arduino boards for implementing communication projects. However, the speed and distance of data transmission can be limited by the quality of the LED and the sensitivity of the light sensor. Despite these limitations, LiFi technology provides an alternative to traditional wired or wireless communication technologies for transferring data.




-------------------------------------------------------------------------------------------------------------------------------------------------------------------
  To perform the Lifi project, a series of steps need to be followed to transfer data from one PC to another using light as a medium. 

1. Firstly, the hardware setup needs to be completed.This experiment is set up as shown in circuit diagram, where a transmitter part is represented by connecting an LED to pin 13 (digital Pin 13) on the Arduino UNO circuit, which connects to the transmitter PC via USB cable. The receiver part is represented by connecting an LDR detector sensor to pin (A0) of the Arduino UNO circuit connected to the receiver PC using a USB cable.

2. After setting up the hardware, the encoder_decoder.py file needs to be run on the transfer PC. This file will prompt the user to enter the name of the file they want to transfer. The code will then convert this file into a .txt file containing a sequence of 0s and 1s.

3. Next, the transmitter and receiver Arduinos need to be loaded with the transmitter.ino and receiver.ino codes, respectively.

4. Once the hardware and software are set up, the sender.py code needs to be run on the transfer PC. This code will prompt the user to provide the .txt file of 0s and 1s that was created by  encoder_decoder.py. After the file is provided, the data is sent to the transmitter Arduino via serial communication. The LED on the transmitter Arduino will blink based on the data received.


5. At the same time, the digital_write.py code needs to be run on the receiver PC. Through a serial communication port this code continuously reads the status of the Light Dependent Resistor (LDR) connected to the receiver arduino, which receives the transmitted data. The light sensor read the intensity of LED and receiver side Python Code compares it with a threshold, so that if the intensity value is greater than a threshold, it means the receiver PC receives bit 1; otherwise, it receives bit 0.The code writes this data to an output.txt file as 1s and 0s.

6. After the complete data transfer is done, the encoder_decoder.py code needs to be run again to decode the received data from binary (0s and 1s) to its original form.



