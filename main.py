import serial
import time


arduinoData = serial.Serial("COM4", baudrate=2000000, timeout=100)
time.sleep(3)

a = str(15)
arduinoData.write(a.encode())
time.sleep(1)
a = str(45)
arduinoData.write(a.encode())
time.sleep(1)
a = str(90)
arduinoData.write(a.encode())
time.sleep(1)
a = str(135)
arduinoData.write(a.encode())
time.sleep(1)
a = str(180)
arduinoData.write(a.encode())
time.sleep(1)