# use this to pull through the data you are interested in. 
# in my case this is a view of the current order status on a particular
# website

from sys import stdout
from time import time, sleep

from BeautifulSoup import BeautifulSoup
import mechanize
import serial

from conf import *

br = mechanize.Browser()

ESC = chr(27) #escape char

def clear_line():
    """
    Clears a line for writing
    """
    stdout.write(ESC + '[2K' + ESC + '[G')
    stdout.flush()

def login():
    """
    Logs into the system
    """
    
    clear_line()
    print "logging in",
    stdout.flush()
    br.open(LOGIN_URL)
    br.select_form(nr=FORM_NO)

    br["username"] = USERNAME
    br["password"] = PASSWORD

    br.submit()

def get_url_data():

    clear_line()
    print "Trying to get data for READ URL",
    stdout.flush()
    try:
        response = br.open(READ_URL)
    except:
        print "Couldn't open URL"
        exit
    
    return BeautifulSoup(response.read())


if __name__ == '__main__':

    #set up the serial interface
    try:
        ser = serial.Serial(SERIAL_INTERFACE, BAUD_RATE, timeout=60)    
    except:
        print "Serial interface not conencted - try it again with a different interface"

    
    login()

    cur_id = 0
    
    while True:

        soup = get_url_data()
        if cur_id != eval("soup." + DOC_PATHS["id"]):
            cur_id = eval("soup." + DOC_PATHS["id"])
            blinktime = float(eval("soup." + DOC_PATHS["price"])) * VALUE_MULTIPLIER
            clear_line()
            print "data changed (ID: %s $%s BT:%d)" % (cur_id, float(eval("soup." + DOC_PATHS["price"])), blinktime),
            stdout.flush()

            ser.write("%d\n" % blinktime)
            try:
                line = ser.readline()
            except:
                print "Some kind of issue, disconnect and restart serial"
                ser.close()
                ser = serial.Serial(SERIAL_INTERFACE, BAUD_RATE, timeout=60)
            else:
                if line in [None, ""]:
                    print "Probably timed out. No dramas. Sleep and iterate"
                    ser.close()
                    sleep(10)
                    ser = serial.Serial(SERIAL_INTERFACE, BAUD_RATE, timeout=60)
        else:
            clear_line()
            print "data unchanged",
            stdout.flush()
            sleep(1)
            
        cur = 0
        while cur < WAIT_PERIOD:
            clear_line()
            print "sleeping for %s seconds\r" % (WAIT_PERIOD-cur),
            stdout.flush()
            sleep(1)
            cur += 1
    
        
    ser.close()
    

