from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://techstepacademy.com/training-ground")

input1_xpath_locator = "//input[@id='ipt1']"
input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"

input1_elem = browser.find_element_by_xpath(input1_xpath_locator)
input2_elem = browser.find_element_by_css_selector(input2_css_locator)
button4_elem = browser.find_element_by_xpath(button4_xpath_locator)

input1_elem.send_keys("Some text")
input2_elem.send_keys("Test text")
button4_elem.click()
