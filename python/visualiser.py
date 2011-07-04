# use this to pull through the data you are interested in. 
# in my case this is a view of the current order status on a particular
# website

from time import time, sleep

from BeautifulSoup import BeautifulSoup
import mechanize
import serial

from conf import *

br = mechanize.Browser()

def login():

    print "logging in"
    br.open(LOGIN_URL)
    br.select_form(nr=FORM_NO)

    br["username"] = USERNAME
    br["password"] = PASSWORD

    br.submit()

def get_url_data():

    print "Trying to get data for READ URL"
    try:
        response = br.open(READ_URL)
    except:
        print "Couldn't open URL"
        exit
    
    return BeautifulSoup(response.read())


if __name__ == '__main__':

    #set up the serial interface
    try:
        ser = serial.Serial(SERIAL_INTERFACE, 9600, timeout=60)    
    except:
        print "Serial interface not conencted - try it again with a different interface"

    
    login()

    cur_id = 0
    
    while True:

        soup = get_url_data()
        if cur_id != eval("soup." + DOC_PATHS["id"]):
            cur_id = eval("soup." + DOC_PATHS["id"])
            print "changed (%s %s)" % (cur_id, float(eval("soup." + DOC_PATHS["price"])))
            blinktime = float(eval("soup." + DOC_PATHS["price"])) * VALUE_MULTIPLIER
            print ("%d\n" % blinktime)
            ser.write("%d\n" % blinktime)
            while (ser.readline() != '0\r\n'):
                pass
        else:
            print "Unchanged"
            
        print "sleeping for %s seconds" % WAIT_PERIOD
        sleep(WAIT_PERIOD)
    
        
    ser.close()
    

