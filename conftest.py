from selenium import webdriver
from pytest import fixture


@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    return browser


# @fixture(params=[
#     webdriver.Chrome,
#     webdriver.Firefox,
#     webdriver.Edge#
#   ]
# )
# def browser(request):
#    driver = request.param
#    drvr = driver()
#    yield drvr
#    drvr.quit()





