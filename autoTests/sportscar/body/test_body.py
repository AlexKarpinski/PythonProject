from pytest import mark


@mark.skip
@mark.smoke
@mark.body
@mark.ui
class BodyTests:
    def test_can_navigate_to_body_page(self, chrome_browser):
        chrome_browser.get('http://www.motortrend.com/')
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True
