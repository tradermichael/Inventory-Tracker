import requests
import json
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
import pyttsx3 as pyttsx
from bs4 import BeautifulSoup
import webbrowser

now = datetime.now()

what2Say = '\
    SCANNER INITATED FOR INVENTORY CHECK! \
    '

# Speaking engine
speakEngine = pyttsx.init()
speakEngine.say(what2Say)
#speakEngine.say(what2Say)
#speakEngine.runAndWait()

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
def send_text(to=1, sub=1, mes=1, item='NA'):
    fromaddr = 'lemichael.email@gmail.com'
    
    toaddr = {1: 'EMAIL', 2: 'EMAIL'}
    #cc = ['lemichael.email@gmail.com']
    #bcc = ['9713864116@tmomail.net']
    subject = {1: 'CPU/GPU TRACKING RUNNING', 2: 'https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666',3:'https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3755-kr/p/N82E16814487530',4:'https://api.bestbuy.com/click/-/6438943/cart', 5:'https://api.bestbuy.com/click/-/6439300/cart'}
    message = {1: "STATUS:GREEN", 2: "INVENTORY ITEM IN STOCK "}
    
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = subject[sub]
    
    msg.attach(MIMEText(message[mes], 'plain'))
    
    
    text = msg.as_string()
    
    print(text)
    
    
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    
    server.starttls()
    
    server.login( 'lemichael.email', '######' )
    
    server.sendmail( fromaddr, toaddr, text)

def newegg_check(): 

    
   try: 
        page_link = "https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666?item=N82E16819113666"
        #fetch content from url
        page_response = requests.get(page_link, timeout=5)
        # parse html
        now = datetime.now()
        page_content = BeautifulSoup(page_response.content, "html.parser")
        status = page_content.find('span', attrs={'class':'btn btn-message btn-wide'})
        
        if (status.contents[0] == 'Sold Out' or status.contents[0] is not None):
            print("\x1b[33m NEWEGG: 5600 : not in stock as of: " + str(now))
            return False
        else:
            webbrowser.open('https://www.youtube.com/watch?v=4HziZ3yZDJY')
            print("NEWEGG: 5600 : IN STOCK!: " + str(now))
            send_text(1,2,2,'AMD 5600')
            talk = 0
            while talk < 20:
                speakEngine.say(what2Say)
                talk += 1  
            return True
   except Exception:
            webbrowser.open('https://www.youtube.com/watch?v=4HziZ3yZDJY')
            print("NEWEGG: 5600 : IN STOCK!: " + str(now))
            send_text(1,2,2,'AMD 5600')
            talk = 0
            while talk < 20:
                speakEngine.say(what2Say)
                talk += 1  
            return True

def newegg_check_GPU(): 
    
   try: 
        page_link = "https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3755-kr/p/N82E16814487530"
        #fetch content from url
        page_response = requests.get(page_link, timeout=5)
        # parse html
        now = datetime.now()
        page_content = BeautifulSoup(page_response.content, "html.parser")
        status = page_content.find('span', attrs={'class':'btn btn-message btn-wide'})
        
        if (status.contents[0] == 'Sold Out' or status.contents[0] is not None):
            print("\x1b[33m NEWEGG: EVGA 3070 : not in stock as of: " + str(now))
            return False
        else:
            webbrowser.open('https://www.youtube.com/watch?v=4HziZ3yZDJY')
            print("NEWEGG: 5600 : IN STOCK!: " + str(now))
            send_text(1,3,2,'AMD 3070')
            talk = 0
            while talk < 20:
                speakEngine.say(what2Say)
                talk += 1        
            return True
   except Exception:
            webbrowser.open('https://www.youtube.com/watch?v=4HziZ3yZDJY')
            print("NEWEGG: 5600 : IN STOCK!: " + str(now))
            send_text(1,3,2,'AMD 3070')
            talk = 0
            while talk < 20:
                speakEngine.say(what2Say)
                talk += 1        
            return True
    
def best_buy_check():
     now = datetime.now()
     try:
        snav_timetable_url = "https://api.bestbuy.com/v1/products(sku=6438943)?apiKey=RYrG9EvjaQGzxsDy3LVfoQZT&sort=onlineAvailability.asc&show=addToCartUrl,onlineAvailability,onlineAvailabilityText,url&format=json"
        r = requests.get(snav_timetable_url)
        time.sleep(10)
        json_data = json.loads(r.text)
        time.sleep(1)
        new_list = []
        
        newdict = json_data['products']
        
        new_list = [i["onlineAvailability"] for i in newdict]
        
        
        
        if (new_list[0] == False):
            print("\x1b[35m BESTBUY: 5600 : not in stock as of: " + str(now))
            return False
        else:
            webbrowser.open('https://www.youtube.com/watch?v=4HziZ3yZDJY')    
                #checkout code
                
            driver = webdriver.Chrome('C:/BrowserDriver/chromedriver')
            driver.get("https://www.bestbuy.com/site/amd-ryzen-5-5600x-4th-gen-6-core-12-threads-unlocked-desktop-processor-with-wraith-stealth-cooler/6438943.p?skuId=6438943")
            time.sleep(2)
                #driver.get("https://api.bestbuy.com/click/-/6356277/cart")
            driver.find_element_by_class_name('fulfillment-add-to-cart-button').click()
            time.sleep(5)
            driver.get("https://www.bestbuy.com/checkout/r/fast-track")
            inputElement = driver.find_element_by_id("user.emailAddress")
            inputElement.send_keys('linsa.le@yahoo.com')
            inputElement = driver.find_element_by_id("user.phone")
            inputElement.send_keys('5034539135')
            driver.find_element_by_class_name('button--continue').click()
    
            print("BESTBUY: 5600 : IN STOCK!  " + str(now))
                # Send text message through SMS gateway of destination number
            send_text(1,4,2,'AMD 5600')
            talk = 0
            while talk < 20:
                speakEngine.say(what2Say)
                talk += 1        
            return True
        
     except Exception:
            pass
    
def best_buy_check_GPU():
    
    now = datetime.now()
    try:
        snav_timetable_url = "https://api.bestbuy.com/v1/products(sku=6439300)?apiKey=RYrG9EvjaQGzxsDy3LVfoQZT&sort=onlineAvailability.asc&show=addToCartUrl,onlineAvailability,onlineAvailabilityText,url&format=json"
        r = requests.get(snav_timetable_url)
        time.sleep(10)
        json_data = json.loads(r.text)
        time.sleep(1)
        new_list = []
        
        newdict = json_data['products']
        
        new_list = [i["onlineAvailability"] for i in newdict]
        
        
        
        if (new_list[0] == False):
            print("\x1b[35m BESTBUY: EVGA 3070 : not in stock as of: " + str(now))
            return False
        else:
            webbrowser.open('https://www.youtube.com/watch?v=4HziZ3yZDJY')    
                #checkout code
                
            driver = webdriver.Chrome('C:/BrowserDriver/chromedriver')
            driver.get("https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-black-gaming-8gb-gddr6x-pci-express-4-0-graphics-card/6439300.p?skuId=6439300")
            time.sleep(2)
                #driver.get("https://api.bestbuy.com/click/-/6356277/cart")
            driver.find_element_by_class_name('fulfillment-add-to-cart-button').click()
            time.sleep(5)
            driver.get("https://www.bestbuy.com/checkout/r/fast-track")
            inputElement = driver.find_element_by_id("user.emailAddress")
            inputElement.send_keys('linsa.le@yahoo.com')
            inputElement = driver.find_element_by_id("user.phone")
            inputElement.send_keys('5034539135')
            driver.find_element_by_class_name('button--continue').click()
    
            print("BESTBUY: EVGA 3070 : IN STOCK!  " + str(now))
            send_text(1,5,2,'AMD 5600')
            talk = 0
            while talk < 20:
                speakEngine.say(what2Say)
                talk += 1   
            return True
    except Exception:
            pass
    
x = 1
while 1 ==1: 
    hour = int('{:02d}'.format(now.hour))
    best_buy_check()
    newegg_check()
    best_buy_check_GPU()
    newegg_check_GPU()
    x += 1
    if hour > 6 and hour < 24 and x%100 == 0:
        print(str((x*23)/60)+" minutes of checks have been initiated as of " + str(now))
    else:
        False