from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://techstepacademy.com/iframe-training")

iframe = browser.find_element_by_css_selector("iframe")
browser.switch_to_frame(iframe)

text_in_iframe = browser.find_element_by_css_selector("div#block-ec928cee802cf918d26c div p")

assert text_in_iframe.text == 'Welcome to the Training Ground. The ability find the right Web Elements is crucial' \
                              ' to automation, and a competent engineer can navigate the DOM swiftly and efficiently. ' \
                              'Use this space to practice finding different kinds of elements using CSS Selectors, XPATH, ' \
                              'and other methods.'
