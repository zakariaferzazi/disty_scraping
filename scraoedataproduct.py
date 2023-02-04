from lib2to3.pgen2 import driver
from typing import List
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="G:\Python Projects\chromedriver_win32\chromedriver.exe")
categories = ["Serveurs/réseaux>Serveurs","Serveurs/réseaux>Switch","Serveurs/réseaux>Routeurs","Serveurs/réseaux>Options Serveurs et réseaux","Image et son>Appareils Photos","Image et son>Appareils Videos","Image et son>Téléviseurs","Image et son>Accessoires image et son","Autres>Onduleurs","Autres>Périphériques de stockage","Consommables>Toners","Consommables>Cartouches"]
linkcategories=["https://disty.ma/25845-serveurs","https://disty.ma/25847-switch","https://disty.ma/25858-routeurs","https://disty.ma/25859-options-serveurs-et-reseaux","https://disty.ma/25848-appareils-photos","https://disty.ma/25849-appareils-videos","https://disty.ma/26866-televiseurs","https://disty.ma/25850-accessoires-image-et-son","https://disty.ma/25873-onduleurs","https://disty.ma/26673-peripheriques-de-stockage", "https://disty.ma/25860-toners","https://disty.ma/25861-cartouches","",""]
filesnames = ["Serveurs","Switch","Routeurs","Serveursetréseaux","AppareilsPhotos","ImageetsonAppareilsVideos","Téléviseurs","sonAccessoiresimage","AutresOnduleurs","AutresPériphériquestockage","ConsommablesToners","ConsommablesCartouches"]


for category, linkcategory,filename in zip(categories, linkcategories,filesnames):
    links = []
    driver.get(linkcategory)

    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[1]/div[1]/div/div[1]/a").get_attribute("href"))
    except:                         
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[2]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[3]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")                         
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[4]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[5]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[6]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[7]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[8]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[9]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[10]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[11]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[12]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[13]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[14]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[15]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[16]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[17]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        ("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[18]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[19]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[20]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[21]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[22]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[23]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[24]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[25]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[26]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[27]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[28]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[29]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[30]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[31]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[32]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[33]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[34]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[35]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[36]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[37]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[38]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[39]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[40]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[41]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[42]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[43]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[44]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[45]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[46]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[47]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[48]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[49]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[50]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[51]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[52]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[53]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[54]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[55]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[56]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[57]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[58]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[59]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[60]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[61]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[62]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[63]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[64]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[65]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[66]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[67]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[68]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[69]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[70]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[71]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[72]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[73]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[74]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[75]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[76]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[77]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[78]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[79]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[80]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[81]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[82]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[83]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[84]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[85]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[86]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[87]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[88]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[89]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[90]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[91]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[92]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[93]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[94]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[95]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[96]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[97]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[98]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[99]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[100]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[101]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[102]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[103]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[104]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[105]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[106]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[107]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[108]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[109]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[110]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[111]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[112]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[113]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[114]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[115]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[116]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[117]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[118]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[119]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[120]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[121]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[122]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[123]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[124]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[125]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[126]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[127]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[128]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[129]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[130]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[131]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[132]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[133]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[134]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[135]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[136]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[137]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[138]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[139]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[140]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[141]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[142]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[143]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[144]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[145]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[146]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[147]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[148]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[149]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[150]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[151]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[152]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[153]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[154]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[155]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[156]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[157]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[158]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[159]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[160]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[161]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[162]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[163]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[164]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[165]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[166]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[167]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[168]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[169]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[170]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[171]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[172]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[173]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[174]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[175]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[176]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[177]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[178]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[179]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[180]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[181]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[182]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[183]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[184]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[185]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[186]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[187]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[188]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[189]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[190]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[191]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[192]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[193]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[194]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[195]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[196]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[197]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[198]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[199]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[200]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[201]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[202]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[203]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[204]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[205]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[206]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[207]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[208]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[209]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[210]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[211]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[212]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[213]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[214]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[215]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[216]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[217]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[218]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[219]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[220]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[221]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[222]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[223]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[224]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[225]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[226]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[227]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[228]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[229]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[230]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[231]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[232]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[233]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[234]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[235]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[236]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[237]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[238]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[239]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[240]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[241]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[242]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[243]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[244]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[245]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[246]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[247]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[248]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[249]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[250]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[251]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[252]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[253]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[254]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[255]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[256]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[257]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[258]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[259]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[260]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[261]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[262]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[263]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[264]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[265]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[266]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[267]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[268]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[269]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
    try:
        links.append(driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/section/div/div[3]/div/div[1]/div[1]/div/div/ul/li[270]/div[1]/div/div[1]/a").get_attribute("href"))
    except:
        print("we passed")
        

    titles = []
    prices = []
    images = []
    descs = []
    skus = []


    for link in links:

            try:
                response = requests.get(link)
                soup = BeautifulSoup(response.text, "html.parser")
                try:
                    sku = soup.find("p", id="product_reference")
                    skus.append(sku.text.replace("-BH4", ""))
                    skuwithnoBH4=sku.text.replace("-BH4", "")
                except:
                    sku = "Not Available"
                    skus.append(sku.text.replace("-BH4", ""))
                try:
                    title = soup.find("h2")
                    titles.append(title.text+" "+skuwithnoBH4)
                except:
                    title = "Not Available"
                    titles.append(title)
                try:
                    price = soup.find("p", class_="our_price_display")
                    prices.append(price.text)
                except:
                    price = "Not Available"
                    prices.append(price)
                try:
                    image = soup.find("img", id="bigpic")
                    images.append(image.get('src'))
                except:
                    image = "Not Available"
                    images.append(image)
                try:
                    desc = soup.find("p", id="short_description_content")
                    descs.append(desc.text)
                except:
                    desc = "Not Available"
                    descs.append(desc)

                print('product has been scraped successfully.....')
            except:
                pass

    df_marks = pd.DataFrame({'Type': 'simple',
    'Name': titles,
    'Regular price': prices,
    'Images': images,
    'Short description': descs,
    'SKU': skus,
    'Published': 1,
    'Is featured?': 1,
    'Visibility in catalog': 'visible',
    'Categories': category
    })
    writer = pd.ExcelWriter(filename+'.xlsx')
    df_marks.to_excel(writer, 'products')
    writer.save()
    print('products has been saved ad excel file successfully.....')