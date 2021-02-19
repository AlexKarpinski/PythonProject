from selenium import webdriver
from pages.trial_page import TrialPage

# Test setup
browser = webdriver.Chrome()
stone_answer = 'rock'

# open Trial page
trng_page = TrialPage(driver=browser)
trng_page.go()

# Positive Test
trng_page.stone_input.input_text(stone_answer)
trng_page.stone_button.click()
stone_result = trng_page.stone_result.text
trng_page.secrets_input.input_text(stone_result)
trng_page.secrets_button.click()
name_result = trng_page.name_result.text
trng_page.name_input.input_text(name_result)
trng_page.name_answer_button.click()
trng_page.check_answer_button.click()
assert trng_page.result_banner.text == 'Trial Complete'
print('Test passed')
browser.quit()
