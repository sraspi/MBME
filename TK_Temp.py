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



### Prepare the plot

# Clean up and exit on matplotlib window close
def on_close(event):
    #print("Cleaning up...")
    GPIO.cleanup()
    #print("Bye :)")
    sys.exit(0)
    
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

plt.ion() # Interactive mode otherwise plot won't update in real time
fig = plt.figure(figsize=(7, 9))
fig.canvas.manager.set_window_title("TK-Temp")
#fig.canvas.manager.full_screen_toggle()
fig.canvas.mpl_connect("close_event", on_close) # Connect the plot window close event to function on_close
ax = fig.add_subplot(111)
#ax2 = ax.twinx() # Get a second y axis

(A0_line,) = ax.plot(x, y1, label="A0", color="#FFAB60", linestyle="--") ##FFAB60 is orange
ax.set_ylabel("Temperatur [°C]", color="#000000")

(A1_line,) = ax.plot(x, y2, label="A1", color="#00FF00", linestyle="--") #00FF00 is green
#ax.set_ylabel("counts", color="#000000")

(A2_line,) = ax.plot(x, y3, label="A2", color="#00549F", linestyle="--") #00549F is blue
#ax.set_ylabel("counts", color="#000000")

(A3_line,) = ax.plot(x, y4, label="A3", color="#9C60FF", linestyle="--") #magenta is magenta
#ax.set_ylabel("counts", color="#000000")

(A4_line,) = ax.plot(x, y5, label="A4", color="#CC071E", linestyle="--") #CC071E is red
#ax.set_ylabel("counts", color="#000000")


#(A2_line,) = ax2.plot(x, y3, label="A2", color="#00549F") #00FFFF
#ax2.set_ylabel("Druck [mbar]", color="#00549F")

#(A3_line,) = ax2.plot(x, y4, label="A3", color="#00FF00") #auf 2.y-Achse  00549F is the RWTH blue color
#ax2.set_ylabel("pressure [mbar]", color="#000000") #auf 2.y-Achse 

cpu = psutil.cpu_percent(1)
plt.title(str(timestr) + "   S1: " + str(round((temperature1),2)) + " S2: " +str(round((temperature2),2)) + " S3: " + str(round((temperature3),2)) + " S4: " + str(round((temperature4),2)) + " S5: " + str(round((temperature5),2)),fontsize=10) # To display 0 initially. Will be updated 
plt.xlabel("Zeit", color="#000000")

           

#Start = time.time()
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
        temperature3 = bme3.temperature+0.15 #blue
        temperature4 = bme4.temperature+0.22 #magenta
        temperature5 = bme5.temperature+0.39 #red
        humidity1 = bme1.humidity
        humidity2 = bme2.humidity
        humidity3 = bme3.humidity+1
        humidity4 = bme4.humidity-1
        humidity5 = bme5.humidity-2
        #print("-"*20)
    

        cpu = psutil.cpu_percent(1)
        timestr = time.strftime("%Y.%m.%d %H:%M:%S")
        Time = time.time()
        f = open(data,  "a")
        f.write(timestr + ",   " + str(A0) + ",       " + str(A1) + ",      " + str(A2) + ",    "   +  str(A3)  + ",    " + str(A4)  + ",    "  + str(Time) + ",    " + str(H1) + ",    " + str(H2)+ ",    " + str(H3) + ",    " + str(H4) + ",    " + str(H5)  + ",    " + str(P1) + ",    " + str(P2) +  ",    " + str(P3) + ",    " + str(P4) + ",    " + str(P5) + ",    " + str(cpu) + '\n')
        f.close()
        
        f = open(log,  "a")
        f.write(timestr + ",   " + str(A0) + ",       " + str(A1) + ",      " + str(A2) + ",    "   +  str(A3)  + ",    " + str(A4)  + ",    "  + str(Time) + ",    " + str(H1) + ",    " + str(H2)+ ",    " + str(H3) + ",    " + str(H4) + ",    " + str(H5)  + ",    " + str(P1) + ",    " + str(P2) +  ",    " + str(P3) + ",    " + str(P4) + ",    " + str(P5) + ",    " + str(cpu) + '\n')
        f.close()
        
        
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
        
        x.append(z)
        y1.append(A0)
        y2.append(A1)
        y3.append(A2)
        y4.append(A3)
        y5.append(A4)    
       
        # ..update plot..
        
        plt.title(str(timestr) + "     S1: " + str(round((temperature1),2)) + "   S2: " +str(round((temperature2),2)) + "   S3: " + str(round((temperature3),2)) + "   S4: " + str(round((temperature4),2)) + "   S5: " + str(round((temperature5),2)),fontsize=10) # To display 0 initially. Will be updated 
        A0_line.set_xdata(x)
        A0_line.set_ydata(y1)
        A1_line.set_xdata(x)
        A1_line.set_ydata(y2)
        A2_line.set_xdata(x)
        A2_line.set_ydata(y3)
        A3_line.set_xdata(x)
        A3_line.set_ydata(y4)
        A4_line.set_xdata(x)
        A4_line.set_ydata(y5)
                    
        ax.relim()  # Rescale data limit for first line
        ax.autoscale_view()  # Rescale view limit for first line
        #ax2.relim()  # Rescale data limit for second line
        #ax2.autoscale_view()  # Rescale view limit for second line
       
        ax.set_ylim(18, 20)
        #plt.ylim(970,1030)
        plt.xlabel("Uhrzeit", fontsize=10, color="#000000")
        fig.canvas.draw()
        fig.canvas.flush_events()      
           
        time.sleep(20)

except KeyboardInterrupt:
    print("keyboardInterrupt")
    GPIO.cleanup()
    print("\nBye")
    sys.exit()