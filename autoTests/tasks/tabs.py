from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_argument('--disable-gpu')
browser1 = webdriver.Chrome()
browser2 = webdriver.Chrome()

browser1.get("http://techstepacademy.com/training-ground")
browser2.get("http://google.com")

browser1.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
browser1.execute_script('window.open("http://google.com","_blank");')
browser1.execute_script('window.open("http://yahoo.com","_blank");')
browser1.execute_script('window.open("http://google.com","_blank");')

#handles = browser1.window_handles
#browser1.switch_to.window(handles[0])
