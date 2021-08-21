from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("C:\python\chromedriver")
driver.get("https://www.google.com/maps/@13.1487775,79.9304626,15z")

def searchplace():
    place = driver.find_element_by_class_name("tactile-searchbox-input")
    place.send_keys("chennai")
    submit = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[10]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    submit.click()
searchplace()

def directions():
    sleep(5)
    directions = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[10]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/button")
    directions.click()
directions()

def find():
    sleep(5)
    find = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[10]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
    find.send_keys("Tiruvallur")
    sleep(5)
    search = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[10]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()
find()

def kilometers():
    sleep(5)
    totalkilometers = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[10]/div[8]/div/div[1]/div/div/div[5]/div[3]/div/div[1]/div[1]/div[2]/div")
    print("TotalKilometers:",totalkilometers.text)
    sleep(5)
    train = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[10]/div[8]/div/div[1]/div/div/div[7]/div[1]/div/div[2]/div[1]/div")
    print("Train Travel:",train.text)
kilometers()

