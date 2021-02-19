from selenium.webdriver.common.by import By

from base_element import BaseElement
from base_page import BasePage
from locator import Locator


class TrialPage(BasePage):
    url = 'http://techstepacademy.com/trial-of-the-stones'

    @property
    def stone_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r1Input')
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def stone_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r1Btn')
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def secrets_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r2Input')
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def secrets_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r2Butn')
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def stone_result(self):
        locator = Locator(By.CSS_SELECTOR, "div#passwordBanner > h4")
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def name_input(self):
        locator = Locator(By.CSS_SELECTOR, "input#r3Input")
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def name_result(self):
        locator = Locator(By.XPATH, "//p[text()='3000'] /.. /span")
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def name_answer_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r3Butn')
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def check_answer_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#checkButn')
        return BaseElement(
            self.driver,
            locator=locator
        )

    @property
    def result_banner(self):
        locator = Locator(By.CSS_SELECTOR, "div#trialCompleteBanner > h4")
        return BaseElement(
            self.driver,
            locator=locator
        )

