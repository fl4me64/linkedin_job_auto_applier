from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Account information constants
EMAIL_ADDRESS = "name@example.com"
PASSWORD = "12345"
PHONE_NUMBER = "5555555555"
SEARCH_CRITERIA = "Search"

# Open LinkedIn
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.linkedin.com/")

# Login
email = driver.find_element(By.ID, "session_key")
email.send_keys(EMAIL_ADDRESS)

password = driver.find_element(By.ID, "session_password")
password.send_keys(PASSWORD)

login_btn = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-btn--full-width")
login_btn.click()

# Delay to solve security check
time.sleep(10)

# Search for job
search = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
search.send_keys(SEARCH_CRITERIA)
search.send_keys(Keys.ENTER)

time.sleep(5)

# Select Jobs category
jobs = driver.find_element(By.CLASS_NAME, "search-reusables__filter-pill-button")
jobs.click()

time.sleep(5)

# Easy Apply filter
easy_apply_filter = driver.find_element(By.CSS_SELECTOR, "[aria-label='Easy Apply filter.']")
easy_apply_filter.click()

time.sleep(2)

# Easy Apply
easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
easy_apply.click()

# Input phone number if the phone number field is empty
phone_number = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
if phone_number.text == "":
    phone_number.send_keys(PHONE_NUMBER)

next = driver.find_element(By.CSS_SELECTOR, "[aria-label='Continue to next step']")
next.click()

# Select resume
time.sleep(2)
next.click()

# Delay for multi-step applications
time.sleep(10)

# Review and submit application
review = driver.find_element(By.CSS_SELECTOR, "[aria-label='Review your application']")
review.click()

time.sleep(5)
submit = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
submit.click()

while True:
    pass