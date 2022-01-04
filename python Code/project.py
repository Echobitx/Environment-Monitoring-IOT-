import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO
import threading
import datetime
import ES2EEPROMUtils
import os
import time

GPIO.setwarnings(False)

rate = 1
global interval_20
interval_20=0
eeprom = ES2EEPROMUtils.ES2EEPROM()
     
spi = busio.SPI(clock = board.SCK, MISO = board.MISO, MOSI = board.MOSI)

cs = digitalio.DigitalInOut(board.D5)

mcp = MCP.MCP3008(spi,cs)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(33, GPIO.OUT)

pwm = GPIO.PWM(33, 100)


GPIO.add_event_detect(20, GPIO.RISING, callback=updateInterval, bouncetime=400)

#eeprom.clear(20)


start = time.perf_counter()


def updateInterval(channel):

    if interval_20 == 5:
        interval_20 = 10
    else:
        interval_20 = 5

def Btn(channe1):
    #readTemparature()
    print("Started")    
   # GPIO.add_event_detect(11, GPIO.RISING, callback=start_Stop, bouncetime=200)


def eepromData():
    

    x = "google.com"
    i = 0
    response = os.system("ping -c 1 " + x)

    if response == 1:
        print ("Connected to the internet")
    else:
        print ("Not connected to internet")
    
        while(i<20):
            data_write.append(int(reading[i]))
            i=+1
        eeprom.write_block(0,data_write)    
        pass
pass



def readTemparature():
    
    
   # GPIO.add_event_detect(11,GPIO.RISING,callback=Btn)
    chan = AnalogIn(mcp, MCP.P0)
    

    
    global interval_20
    
    
    temp = (float)(chan.voltage-0.5)*100;
    #interval = perf_counter()
    thread = threading.Timer(rate, readTemparature)
    thread.daemon = True  
    thread.start()
    
    end = time.perf_counter()
   
    
    
    runtime = end - start
    if (interval_20==20):
        pwm.start(0)
        star = "    *   |"
        interval_20 = 0
    else:
        pwm.stop()
        star = "        |"
        interval_20+=5
    xy = datetime.datetime.now()   
    print( "|    ", xy.strftime("%H:%M:%S"),"      |     ","{:>3}".format(int(runtime)),"     |   ", temp ,"  C   |", star)
    
    
print("________________________________________________________________")
print("|     Time	     |   Syt Timer   |     Temp       |  Buzzer")
print("________________________________________________________________")

GPIO.add_event_detect(11,GPIO.BOTH,callback=Btn)
def destroy(): 
    GPIO.cleanup()

if __name__ == "__main__":
    #GPIO.add_event_detect(11, GPIO.BOTH, callback=start_Stop)
    try:            
        readTemparature()
     
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        pass
   
# Tell our program to run indefinitely
while True:
    pass
GPIO.cleanup()
