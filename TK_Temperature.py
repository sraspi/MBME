import sys 
import time 
import datetime
import board
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import numpy as np
import psutil


start = datetime.datetime.now()
x = [start]
c=0
b=0
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
t_end = time.time()
t_start = time.time()
timeout = 0

def extr():
    Dateiname = "/home/pi/data/logfile.txt"
    d = open(Dateiname,  "r")
    d.read()
    d.close
    x=np.genfromtxt(Dateiname,skip_header=1,usecols=(6),delimiter=",")
    y1=np.genfromtxt(Dateiname,skip_header=1,usecols=(1),delimiter=",")
    y2=np.genfromtxt(Dateiname,skip_header=1,usecols=(2),delimiter=",")
    y3=np.genfromtxt(Dateiname,skip_header=1,usecols=(3),delimiter=",")
    y4=np.genfromtxt(Dateiname,skip_header=1,usecols=(4),delimiter=",")
    y5=np.genfromtxt(Dateiname,skip_header=1,usecols=(5),delimiter=",")
    

    l = len(x)
    t = [0]*(l)
    for i in range(0,l):
        #print(x1[i])
        t[i] = datetime.datetime.utcfromtimestamp(x[i]).strftime('%Y-%m-%d %H:%M:%S')
        
    x = float(t)
    

extr


### Prepare the plot

# Clean up and exit on matplotlib window close
def on_close(event):
    #print("Cleaning up...")
    GPIO.cleanup()
    #print("Bye :)")
    sys.exit(0)
    



plt.ion() # Interactive mode otherwise plot won't update in real time
fig = plt.figure(figsize=(7, 9))
fig.canvas.manager.set_window_title("TK-Temperatur")
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

humidity1 = y1[0]
humidity2 = y2[0]
humidity3 = y3[0]
humidity4 = y4[0]
humidity5 = y5[0]
timestr = time.strftime("%Y.%m.%d %H:%M:%S")
plt.title(str(timestr) + "   S1: " + str(round((humidity1),0)) + " S2: " +str(round((humidity2),0)) + " S3: " + str(round((humidity3),0)) + " S4: " + str(round((humidity4),0)) + " S5: " + str(round((humidity5),0)),fontsize=10) # To display 0 initially. Will be updated 
plt.xlabel("Zeit", color="#000000")

           

#Start = time.time()
try:
    while True:
        try:
                   
            Dateiname = "/home/pi/data/logfile.txt"
            d = open(Dateiname,  "r")
            d.read()
            d.close
            x=np.genfromtxt(Dateiname,skip_header=1,usecols=(6),delimiter=",")
            y1=np.genfromtxt(Dateiname,skip_header=1,usecols=(1),delimiter=",")
            y2=np.genfromtxt(Dateiname,skip_header=1,usecols=(2),delimiter=",")
            y3=np.genfromtxt(Dateiname,skip_header=1,usecols=(3),delimiter=",")
            y4=np.genfromtxt(Dateiname,skip_header=1,usecols=(4),delimiter=",")
            y5=np.genfromtxt(Dateiname,skip_header=1,usecols=(5),delimiter=",")
            

            l = len(x)
            t = [0]*(l)
            for i in range(0,l):
                #print(x1[i])
                t[i] = datetime.datetime.utcfromtimestamp(x[i]).strftime('%Y-%m-%d %H:%M:%S')
                
            
            
            # ..update plot..
            x = t
            humidity1 = y1[l-1]
            humidity2 = y2[l-1]
            humidity3 = y3[l-1]
            humidity4 = y4[l-1]
            humidity5 = y5[l-1]
            timestr = time.strftime("%Y.%m.%d %H:%M:%S")
            plt.title(str(timestr) + "     S1: " + str(round((humidity1),2)) + "   S2: " +str(round((humidity2),2)) + "   S3: " + str(round((humidity3),2)) + "   S4: " + str(round((humidity4),2)) + "   S5: " + str(round((humidity5),2)),fontsize=10) # To display 0 initially. Will be updated 
                    
            x = list(t)
            y1 =list(y1)
            y2 =list(y2)
            y3 =list(y4)
            y4 =list(y4)
            y5 =list(y5)
            
            
            A0_line.set_xdata((x))
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
           
            ax.set_ylim(19.5, 20.5)
            #plt.ylim(970,1030)
            plt.xlabel("Uhrzeit", fontsize=10, color="#000000")
            
            fig.canvas.draw()
            fig.canvas.flush_events()
            time.sleep(6.0)
            b=b+1
        except:
            c=c+1
            timestr = time.strftime("%Y.%m.%d %H:%M:%S")
            t_end = time.time()
            error = "/home/pi/data/error.log"
            f = open(error,  "a")
            f.write("Temperature-loops: " + str(b) + " errors: " + str(c) + '\n')
            f.close()
        #print(b,c)
        #print(max(y1),max(y2), max(y3), max(y4), max(y5))
        #print(np.mean(y1),np.mean(y2), np.mean(y3), np.mean(y4), np.mean(y5))
           
            
            


except KeyboardInterrupt:
    print("keyboardInterrupt")
    GPIO.cleanup()
    print("\nBye")
    sys.exit()

