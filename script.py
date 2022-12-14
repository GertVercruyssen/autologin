# import module
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, time
from random import seed
from random import randint
from time import sleep

driver = webdriver.Chrome()

#put the start url here
driver.get("https://www.something.com/")

sleep(3)

print("Back Page load =", datetime.now().strftime("%H:%M:%S"))

email = driver.find_element(by=By.ID, value="email")
email.send_keys("user@company.com")
password = driver.find_element(by=By.ID, value="password")
password.send_keys("password")
login_button =driver.find_element(by=By.CLASS_NAME, value="btn-primary")
login_button.click()

print("Logged in at =", datetime.now().strftime("%H:%M:%S"))

#the delay
startTime = time(10, 00, 30)
while startTime > datetime.today().time(): # you can add here any additional variable to break loop if necessary
    sleep(1)# you can change 1 sec interval to any other

#add an element of randomness to start time
seed(1)
sleeprand = randint(0, 5)
sleep(sleeprand)

endTime = time(10, 00, 55)
while endTime > datetime.today().time():
    try:
        buttons = driver.find_elements(By.TAG_NAME, 'button')
        thabutton = buttons[1]
        print("pressing button "+thabutton.text+" attempt ")
        thabutton.click()
        break
    except:
        print("Failed to press button")
        sleep(3)
  
print("Finished at =", datetime.now().strftime("%H:%M:%S"))
