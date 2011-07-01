# use this to pull through the data you are interested in. 
# in my case this is a view of the current order status on a particular
# website

from time import sleep

from BeautifulSoup import BeautifulSoup
import mechanize
import serial

from conf import *

br = mechanize.Browser()

def login():

    br.open(LOGIN_URL)
    br.select_form(nr=FORM_NO)

    br["username"] = USERNAME
    br["password"] = PASSWORD

    br.submit()

def get_url_data():

    try:
        response = br.open(READ_URL)
    except:
        print "Couldn't open URL"
        exit
    
    return BeautifulSoup(response.read())


if __name__ == '__main__':
    login()
    soup = get_url_data()

    theid = eval("soup." + DOC_PATHS["id"])
    price = eval("soup." + DOC_PATHS["price"])

    print theid
    print price
    #get serial interface
    try:
        ser = serial.Serial(SERIAL_INTERFACE, 9600)    
    except:
        print "Serial interface not conencted - try it again with a different interface"
    
    val = float(price) * 100
    print ("%d\n" % val)
    ser.write("%d\n" % val)

    sleep(15)
    ser.close()
    

