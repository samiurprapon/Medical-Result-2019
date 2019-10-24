from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pyautogui
import time
import os

# path = "geckodriver.exe"
browser = webdriver.Firefox();

browser.get("http://result.dghs.gov.bd/mbbs")

time.sleep(5)

roll_number = 192171

count = 0

while(True):
    count += 1
    roll_number += 1

    pyautogui.press('tab')
    pyautogui.typewrite(str(roll_number))
    pyautogui.press('enter')
    pyautogui.press('enter')        

    time.sleep(.35)

    try:
        table = browser.find_element_by_id("rockartists")
        row = table.find_elements_by_tag_name("td")
        #[0] [1]
        write_str = row[1].text + ' ' + row[0].text

        with open("result.txt", "a") as myfile:
            myfile.write(write_str + '\n')
        
        time.sleep(.1)

    except NoSuchElementException:
        with open("rangpur.txt", "a") as myfile:
            myfile.write("\n")
        continue
    except StaleElementReferenceException:
        with open("rangpur.txt", "a") as myfile:
            myfile.write("\n")
        continue


