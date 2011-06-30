# use this to pull through the data you are interested in. 
# in my case this is a view of the current order status on a particular
# website

from BeautifulSoup import BeautifulSoup
import mechanize

from conf import *

br = mechanize.Browser()

br.open(LOGIN_URL)
br.select_form(nr=FORM_NO)

br["username"] = USERNAME
br["password"] = PASSWORD

br.submit()

try:
    response = br.open(READ_URL)
except:
    print "Couldn't open URL"
    exit
    
soup = BeautifulSoup(response.read())

theid = eval("soup." + DOC_PATHS["id"])
price = eval("soup." + DOC_PATHS["price"])

print theid
print price

