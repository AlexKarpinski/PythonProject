from selenium import webdriver
from pages.training_ground_page import TrainingGroundPage

# Test setup
browser = webdriver.Chrome()

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1'
browser.quit()
