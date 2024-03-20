from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


email = "hebert.pratama@cloudmails.apu.edu.my"

password = "Fjheb4gaIj6b"

c = webdriver.ChromeOptions()
#incognito parameter passed
c.add_argument("--incognito")

driver = webdriver.Chrome(options=c)

wait = WebDriverWait(driver, 30)

driver.get("https://ta-payroll.azurewebsites.net/")


element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='nav-link text-dark']"))    
)

element.click()

emailInput = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@class='form-control ltr_override input ext-input text-box ext-text-box']"))    
)

#emailInput = driver.find_element(By.XPATH, "//input[@class='form-control ltr_override input ext-input text-box ext-text-box']")


emailInput.send_keys(email)

driver.implicitly_wait(5)

emailInput.send_keys(Keys.RETURN)


passwordInput = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))    
)



passwordInput.send_keys(password)

time.sleep(2)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

time.sleep(2)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()

#driver.execute_script('''window.open("https://ta-payroll.azurewebsites.net/SignIns","_blank");''')



signInHistoryTab = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/SignIns']"))    
)

signInHistoryTab.click()

actions = ActionChains(driver)
actions.send_keys(Keys.TAB * 10)

actions.send_keys(Keys.ENTER)

actions.pause(1)

actions.send_keys(Keys.TAB * 2)
actions.send_keys(Keys.ENTER)
#actions.send_keys(Keys.TAB * 1)
#ctions.send_keys(Keys.ENTER)
actions.perform()

submitBtn = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@value='Submit']"))    
)

submitBtn.click()

selectBtn = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//select[@class='form-select form-select-sm']"))    
)

select = Select(selectBtn)

select.select_by_value('100')

selectBtn = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.TAG_NAME, "tbody"))    
)

html = selectBtn.get_attribute('innerHTML')

htmlArr = html.split(" ")

while True:
    if '' in htmlArr :
        htmlArr.remove('')
        continue
    
    break

tree = BeautifulSoup(html, features="html.parser")
good_html = tree.prettify()




print(good_html.split('\n'))

#actions.send_keys(Keys.TAB  * 5)
#actions.send_keys(Keys.ENTER)



#actions.send_keys(Keys.DOWN * 3)
#actions.send_keys(Keys.RETURN)



#actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)

#actions.send_keys(Keys.ENTER)



time.sleep(3)

#a = driver.execute_script("document.getElementsByTagName('table')[0]")

#print(a)


"""
periodPicker = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@type='month']"))    
)

periodPicker.send_keys("November")
"""
"""
#passwordInput.send_keys()

#signInInput = driver.find_element(By.XPATH, "//input[@class='win-button button_primary button ext-button primary ext-primary']")

#signInInput.click()



"""


time.sleep(100000)