# Python automation page for checking Cathay Pacific 
# Award return flight
# This script is not currently working
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Agent to bypass Cathay Pacific's user-agent check for logins
from selenium.webdriver.chrome.options import Options
options = Options()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))


driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.cathaypacific.com/cx/en_US/book-a-trip/redeem-flights/redeem-flight-awards.html")

wait = WebDriverWait(driver, 5)

# Click `Accept Cookie`
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ot-pc-content"]/div[2]/div[1]/button[4]')))
driver.find_element(By.XPATH, '//*[@id="ot-pc-content"]/div[2]/div[1]/button[4]').click()

# Click `One Way` button
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ow"]/span')))
one_way_button = driver.find_element(By.XPATH, '//*[@id="ow"]/span').click()

# Click and fill `From` box
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[1]/div/div/div/div[2]/input')))
from_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[1]/div/div/div/div[2]/input')
from_box.click()
from_box.send_keys("Taipei, Taoyuan Int'l")
from_box.send_keys(Keys.DOWN, Keys.ENTER)

# Click and fill `Going` box
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[2]/div/div/div/div[2]/input')))
going_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[2]/div/div/div/div[2]/input')
going_box.click()
going_box.send_keys("San Francisco, San Francisco Int'l (SFO) United States")
going_box.send_keys(Keys.DOWN, Keys.ENTER)

# Click and fill `Cabin class and passengers` box
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[3]/div[1]/div/div[2]/div/img')))
cabin_box_arrow= driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[3]/div[1]/div/div[2]/div/img')
cabin_box_arrow.click()

# Click inner Cabin Class but might not need this
# time.sleep(0.5)
# wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/img')))
# cabin_box_inner_arrow= driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/img')
# cabin_box_inner_arrow.click()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[3]/div[2]/div/div/div[5]/div/span')))
cabin_box_done_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[3]/div[2]/div/div/div[5]/div/span')
cabin_box_done_button.click()

# Click on `Departing on`
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[4]/div/div/div[1]/div[2]/span')))
departing_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[4]/div/div/div[1]/div[2]/span')
departing_box.click()

time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[4]/div[2]/div/div[2]/div/div[5]/div/img')))
calendar_right = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[4]/div[2]/div/div[2]/div/div[5]/div/img')
calendar_right.click()
calendar_right.click()
calendar_right.click()
calendar_right.click()
calendar_right.click()
calendar_right.click()

# Selecting individual dates in the calendar
# This was tricky - I had to make the screen fullscreen before even clicking the popup ad
driver.switch_to.active_element
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[4]/div[2]/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[4]')))
day_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[4]/div[2]/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[4]')
day_box.click()
done_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div[4]/div[2]/div/div[3]/div/div/span')
done_box.click()

# Click on `search flight`
search_flight_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/form/div[4]/div/span')
search_flight_box.click()

time.sleep(500)
driver.close()
