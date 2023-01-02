import sys 
import time 
import datetime
import board
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import numpy as np
import psutil
import adafruit_tca9548a
from adafruit_bme280 import basic as adafruit_bme280

import socket
import time
import ip_mail
import os

#IP-Check:
time.sleep(30)
IPA0 = os.popen('hostname -I').readline(15)
print(IPA0)
f = open("/home/pi/ip.txt", "w")
f.write(str(IPA0))
f.close()
ip_mail.ip_mail()
   

# Create I2C bus as normal
i2c = board.I2C()
# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)
# Create each BME280 using the TCA9548A channel instead of the I2C object
bme1 = adafruit_bme280.Adafruit_BME280_I2C(tca[1]) # TCA Channel 0
bme2 = adafruit_bme280.Adafruit_BME280_I2C(tca[1]) # TCA Channel 1
bme3 = adafruit_bme280.Adafruit_BME280_I2C(tca[2]) # TCA Channel 2
bme4 = adafruit_bme280.Adafruit_BME280_I2C(tca[3]) # TCA Channel 3
bme5 = adafruit_bme280.Adafruit_BME280_I2C(tca[4]) # TCA Channel 4


start = datetime.datetime.now()
x = [start]
y1 = [0]
y2 = [0]
y3 = [0]
y4 = [0]
y5 = [0]

A0 = 0
A1 = 0
A2 = 0
A3 = 0
A4 = 0

H1 = [0]
H2 = [0]
H3 = [0]
H4 = [0]
H5 = [0]

P1 = [0]
P2 = [0]
P3 = [0]
P4 = [0]
P5 = [0]

# writing headers data.txt and logfile.txt
timestr = time.strftime("%Y.%m.%d %H:%M:%S")
t_end = time.time()
data = "/home/pi/data/" + "TK_Temp" + timestr+ ".txt"
f = open(data,  "w")
f.write("Datum/Zeit,         Temp1,          Temp2,          Temp3,         Temp4,         Temp5,      H1,      H2,      H3,      H4,      H5,    P1,     P2,     P3,     P4,     P5       cpu[%]" + '\n')
f.close()
log = "/home/pi/data/logfile.txt"
f = open(log,  "w")
f.write("Datum/Zeit,         Temp1,          Temp2,          Temp3,         Temp4,         Temp5,      H1,      H2,      H3,      H4,      H5,    P1,     P2,     P3,     P4,     P5       cpu[%]" + '\n')
f.close()


   
# Access each sensor via its instance
pressure1 = bme1.pressure
pressure2 = bme2.pressure
pressure3 = bme3.pressure
pressure4 = bme4.pressure
pressure5 = bme5.pressure
temperature1 = bme1.temperature
temperature2 = bme2.temperature
temperature3 = bme3.temperature
temperature4 = bme4.temperature
temperature5 = bme5.temperature
humidity1 = bme1.humidity
humidity2 = bme2.humidity
humidity3 = bme3.humidity
humidity4 = bme4.humidity
humidity5 = bme5.humidity

cpu = psutil.cpu_percent(1)
          
try:
    while True :
        t_start = time.time()
        
        # Access each sensor via its instance
        pressure1 = bme1.pressure
        pressure2 = bme2.pressure
        pressure3 = bme3.pressure
        pressure4 = bme4.pressure
        pressure5 = bme5.pressure
        temperature1 = bme1.temperature #orange
        temperature2 = bme2.temperature-0.04 #green
        temperature3 = bme3.temperature+0.01 #blue
        temperature4 = bme4.temperature+0.12 #magenta
        temperature5 = bme5.temperature+0.52 #red
        humidity1 = bme1.humidity
        humidity2 = bme2.humidity+0.2
        humidity3 = bme3.humidity+0.5
        humidity4 = bme4.humidity-0.05
        humidity5 = bme5.humidity-2.1  

        cpu = psutil.cpu_percent(1)
        timestr = time.strftime("%Y.%m.%d %H:%M:%S")
        Time = time.time()
        
        
        
        
        z = datetime.datetime.now()
        A0 = temperature1
        A1 = temperature2
        A2 = temperature3
        A3 = temperature4
        A4 = temperature5
        
        H1 = humidity1
        H2 = humidity2
        H3 = humidity3
        H4 = humidity4
        H5 = humidity5
        
        P1 = pressure1
        P2 = pressure2
        P3 = pressure3
        P4 = pressure4
        P5 = pressure5
        
        f = open(data,  "a")
        f.write(timestr + ",   " + str(A0) + ",       " + str(A1) + ",      " + str(A2) + ",    "   +  str(A3)  + ",    " + str(A4)  + ",    "  + str(Time) + ",    " + str(H1) + ",    " + str(H2)+ ",    " + str(H3) + ",    " + str(H4) + ",    " + str(H5)  + ",    " + str(P1) + ",    " + str(P2) +  ",    " + str(P3) + ",    " + str(P4) + ",    " + str(P5) + ",    " + str(cpu) + '\n')
        f.close()
        
        f = open(log,  "a")
        f.write(timestr + ",   " + str(A0) + ",       " + str(A1) + ",      " + str(A2) + ",    "   +  str(A3)  + ",    " + str(A4)  + ",    "  + str(Time) + ",    " + str(H1) + ",    " + str(H2)+ ",    " + str(H3) + ",    " + str(H4) + ",    " + str(H5)  + ",    " + str(P1) + ",    " + str(P2) +  ",    " + str(P3) + ",    " + str(P4) + ",    " + str(P5) + ",    " + str(cpu) + '\n')
        f.close()
        
        x.append(z)
        y1.append(A0)
        y2.append(A1)
        y3.append(A2)
        y4.append(A3)
        y5.append(A4)      
        
        #IP-Check:
        try:
            IPA0 = os.popen('hostname -I').readline(15)
            time.sleep(10)
            IPA1 = os.popen('hostname -I').readline(15)
    
            if IPA0 != IPA1:
                f = open("/home/pi/ip.txt", "w")
                f.write(str(IPA1))
                f.close()
                ip_mail.ip_mail()
                time.sleep(20)
                
        except:
            print("Email-error")
        time.sleep(20)
        
except KeyboardInterrupt:
    print("keyboardInterrupt")
    GPIO.cleanup()
    print("\nBye")
    sys.exit()
