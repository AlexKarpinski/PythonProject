from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://techstepacademy.com/trial-of-the-stones")

inputStone_css_locator = "input[id='r1Input']"
inputSecrets_css_locator = "input[id='r2Input']"
inputName_css_locator = "input[id='r3Input']"
buttonStoneAnswer_css_locator = "button[id='r1Btn']"
buttonSecretsAnswer_css_locator = "button[id='r2Butn']"
buttonNameAnswer_css_locator = "button[id='r3Butn']"
buttonCheckAnswer_css_locator = "button[id='checkButn']"

inputStone_elem = browser.find_element_by_css_selector(inputStone_css_locator)
inputSecrets_elem = browser.find_element_by_css_selector(inputSecrets_css_locator)
inputName_elem = browser.find_element_by_css_selector(inputName_css_locator)
buttonStoneAnswer_elem = browser.find_element_by_css_selector(buttonStoneAnswer_css_locator)
buttonSecretsAnswer_elem = browser.find_element_by_css_selector(buttonSecretsAnswer_css_locator)
buttonNameAnswer_elem = browser.find_element_by_css_selector(buttonNameAnswer_css_locator)
buttonCheckAnswer_elem = browser.find_element_by_css_selector(buttonCheckAnswer_css_locator)

stone_result = browser.find_element_by_css_selector(
    "div#passwordBanner > h4"
)
richest_merchant_name = browser.find_element_by_xpath(
    "//p[text()='3000'] /.. /span"
)
complete_msg = browser.find_element_by_css_selector(
    "div#trialCompleteBanner > h4"
)

inputStone_elem.send_keys("rock")
buttonStoneAnswer_elem.click()
inputSecrets_elem.send_keys(stone_result.text)
buttonSecretsAnswer_elem.click()
inputName_elem.send_keys(richest_merchant_name.text)
buttonNameAnswer_elem.click()
buttonCheckAnswer_elem.click()
assert complete_msg.text == 'Trial Complete'

