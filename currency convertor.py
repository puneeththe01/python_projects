from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files (x86)\cmsedgedriver.exe"

currencies = ["US Dollar", "Canadian Dollar", "Indian rupee", "Euro"]

for i in range(len(currencies)):
    print(f'{i+1}. {currencies[i]}')

first_currency = int(input("Enter the number of the currency you have in the above list >>> "))
first_amount = int(input(f"Enter the amount in {currencies[first_currency - 1]} >>> "))
second_currency = int(input("Enter the number of the currency to convert into in the above list >>> "))

driver = webdriver.Edge(path)
driver.get("https://www.oanda.com/currency-converter/en/")

time.sleep(5)
search = driver.find_element(By.ID, 'baseCurrency_currency_autocomplete')
for i in range(20):
    search.send_keys(Keys.BACKSPACE)
search.send_keys(currencies[first_currency - 1])
search.send_keys(Keys.ARROW_DOWN)
search.send_keys(Keys.RETURN)
time.sleep(3)
search = driver.find_element(By.ID, 'quoteCurrency_currency_autocomplete')
for i in range(20):
    search.send_keys(Keys.BACKSPACE)
search.send_keys(currencies[second_currency - 1])
search.send_keys(Keys.ARROW_DOWN)
search.send_keys(Keys.RETURN)
search = driver.find_element(By.XPATH, "//input[@tabindex = '4']")
time.sleep(5)
converted_value = search.get_attribute('value')
print(converted_value * first_amount)
time.sleep(10)
