#!/usr/bin/env python

import requests
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def writeName(name,xpath):
    formName = driver.find_element_by_xpath(xpath)
    formName.send_keys("%s" % (name))
    time.sleep(1)
    print("[*]Nom introduit correctament.")

def writePhone(phone,xpath):
    formPhone = driver.find_element_by_xpath(xpath)
    formPhone.send_keys("%s" % (phone))
    time.sleep(1)
    print("[*]Telefon introduit correctament.")

def writeEmail(email,xpath):
    formEmail = driver.find_element_by_xpath(xpath)
    formEmail.send_keys("%s" % (email))
    time.sleep(1)
    print("[*]Email introduit correctament.")

def clickBtn(xpath):
    btn = driver.find_element_by_xpath(xpath)
    btn.click()
    time.sleep(1)

print("Introdueix el nom:")
name = input()
print("Introdueix el telefon:") 
phone = input()
print("Introdueix el email:") 
email = input()

driver = webdriver.Firefox()

##### MARINADOR #####
driver.get("https://www.marinador.com/es/motivo-abandono")
print("[*] Introduint les dades a Marina d'Or...")
time.sleep(7)
writePhone(phone,"//*[@id='TelefonoC']")
clickBtn("//*[@id='submitButtonP']")
time.sleep(5)
print("[OK] Marina d'Or.")

##### ALUMINIONS CANCUYAS #####
driver.get("https://www.aluminioscancuyas.com/te-llamamos-gratis/")
print("[*] Introduint les dades a Aluminions Cancuyas...")
time.sleep(7)
writePhone(phone,"//*[@id='Telefono']")
writeEmail(email,"/html/body/div[1]/div[2]/section/div/div/div[2]/div/div/div/form/p[2]/span/input")
clickBtn("/html/body/div[1]/div[2]/section/div/div/div[ 2]/div/div/div/form/p[3]/span/span/span/input")
clickBtn("/html/body/div[1]/div[2]/section/div/div/div[2]/div/div/div/form/p[4]/span/span/span/input")
clickBtn("/html/body/div[1]/div[2]/section/div/div/div[2]/div/div/div/form/p[5]/input")
time.sleep(5)
print("[OK] Aluminions Cacnuyas.")

##### CASER SALUD #####
driver.get("https://caser.isalud.com/llama-gratis")
print("[*] Introduint les dades a Caser Salud...")
time.sleep(7)
writeName(name,"//*[@id='name']")
writePhone(phone,"//*[@id='phone']")
writeEmail(email,"//*[@id='email']")
clickBtn("/html/body/div[1]/section[1]/div[2]/form/div/div[5]/div/a")
clickBtn("//*[@id='contact_freecall']")
time.sleep(5)
print("[OK] Caser Salud.")

##### TALLERES ROFER #####
driver.get("//*[@id='widgetu1874_input']")
print("[*] Introduint les dades a Talleres Rofer...")
time.sleep(7)
writeName(name,"//*[@id='widgetu1874_input']")
writePhone(phone,"//*[@id='widgetu1869_input']")
clickBtn("/html/body/div[1]/div[1]/div[4]/form/div/div[3]/div[1]/div/label")
clickBtn("//*[@id='u1868-4']")
time.sleep(5)
print("[OK] Talleres rofer.")

##### PIKOLIN #####
driver.get("https://www.pikolin.com/es/te-llamamos")
print("[*] Introduint les dades a Pikolin...")
time.sleep(7)
writeName(name,"//*[@id='name']")
writePhone(phone,"//*[@id='phone']")
clickBtn("//*[@id='action']")
time.sleep(5)
print("[OK] Pikolin.")

time.sleep(1)
print("[*] Ending program...")
driver.quit()
