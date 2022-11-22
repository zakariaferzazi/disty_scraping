from lib2to3.pgen2 import driver
from typing import List
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="G:\Python Projects\chromedriver_win32\chromedriver.exe")


driver.get("https://disty.ma/25850-accessoires-image-et-son")

print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[1]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[2]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[3]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[4]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[5]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[6]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[7]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[8]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[9]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[10]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[11]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[12]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[13]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[14]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[15]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[16]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[17]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[18]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[19]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[20]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[21]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[23]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[24]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[25]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[26]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[27]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[28]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[29]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[30]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[31]/div[1]/div/div[1]/a").get_attribute("href")+'",')
print('"'+driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[32]/div[1]/div/div[1]/a").get_attribute("href")+'",')
