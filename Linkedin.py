from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd


# val=input("Groups your are looking for??? ")
group=input("Enter group name: ")

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
time.sleep(1)

eml = driver.find_element(by=By.ID, value="username")
eml.send_keys("Enter mail id")
passwd = driver.find_element(by=By.ID, value="password")
passwd.send_keys("Enter Linkedin password")
loginbutton = driver.find_element(by=By.XPATH, value="//*[@id='organic-div']/form/div[3]/button")
loginbutton.click()
time.sleep(2)

# group=input("Enter group name: ")
url = f'https://www.linkedin.com/search/results/all/?keywords={group}&origin=GLOBAL_SEARCH_HEADER&sid=X07'
driver.get(url)
time.sleep(2)
# Details = {"LINK": [], "NAME": [], "MEMBERS": []}

soup = BeautifulSoup(driver.page_source, "html.parser")
link1 = soup.find("a", attrs={"class", "app-aware-link scale-down"}).get("href")
name = soup.find("title").text
Name = name.split('"')
member = soup.find("div", attrs={"class", "entity-result__primary-subtitle t-14 t-black t-normal"}).text
print(link1, Name[1],member)


time.sleep(5)