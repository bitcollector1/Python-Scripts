from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import lxml
import smtplib
import time

options = Options()
options.headless = True

mylist = []
not_found = ''

driver = webdriver.Firefox(options=options)
driver.get("https://www.website.com)

# Try and fix the random timing errors --> better way is with selenium waitfor
time.sleep(5)

# Look for the state "no product in stock" --> "0 matches, that stinks"
try:
    not_found = driver.find_element_by_class_name("css-1ctldcn.ew1p50q2")
    not_found_html = not_found.get_attribute('innerHTML')

# handle the exception of product actually being found.
except NoSuchElementException as e:
    print (str(e))

# print "not found message" and exit program
if(not_found):
    print (not_found_html)
    driver.close()
    exit()

try: 

    # They have stock; now find how many products they have at runtime.
    products = driver.find_element_by_class_name("css-hecap1.ettsl931")
    total_products = products.get_attribute('innerHTML')

# handle the exception of product elements not being found and exit program
except NoSuchElementException as e:
    print (str(e))
    driver.close()
    exit()

# Find all of the Grid Elements, or all of the products available - all products use the same grid ID
element = driver.find_element_by_class_name("css-19ofktj.e29d1tf2")
html = element.get_attribute('innerHTML')
soup = bs(html, "lxml")

print (total_products)

for a in soup.find_all('a', href=True):
    mylist.append("Found the URL: https://www.website.com" + a['href'])

# Python 3 only
print (*mylist, sep="\n")

# See the whole tree with price and description for each item
# prettyHTML = soup.prettify()
# print (prettyHTML)

port = 587  
sender_email = "SENDER@gmail.com"
receiver_email = "RECEIVER@email.com"

message = """\
Subject: new products have arrived!

{}. """ .format(total_products) + str(mylist)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender_email, "SENDERPASSWORD")
server.sendmail(sender_email, receiver_email, message)
server.quit()

driver.close()


