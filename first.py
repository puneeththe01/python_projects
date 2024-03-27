from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files (x86)\cmsedgedriver.exe"

# define the driver
driver = webdriver.Edge(path)
driver.get("https://instagram.com/")
print(driver.title)

# Login into insta account
time.sleep(10)
search = driver.find_element(By.NAME, "username")
search.send_keys("puneeththe01")
search = driver.find_element(By.NAME, "password")
search.send_keys("RICHESTPR01")
search.send_keys(Keys.RETURN)

# not saving the login info
time.sleep(5)
search = driver.find_element(By.XPATH, "//button[@class = '_acan _acao _acas _aj1-']")
search.click()

time.sleep(5)
# finding off notification
search = driver.find_element(By.XPATH, "//button[@class = '_a9-- _a9_1']")
search.click()

#unseen_stories = 0

#for i in range(170):
#       search = driver.find_element(By.XPATH, f"//canvas[@height = '99'][{i+1}]")

#print(unseen_stories)

time.sleep(15)
driver.quit()
