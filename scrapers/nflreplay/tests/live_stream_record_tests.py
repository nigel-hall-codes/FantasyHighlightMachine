from ..page_objects import ok_ru_live_stream_page
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Tests(unittest.TestCase):

    def setUp(self) -> None:
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(executable_path=r"webdrivers/chromedriver.exe", chrome_options=options)
        self.live_stream = ok_ru_live_stream_page.LiveStream(self.driver)

    def test_record_live_stream(self):
        url = "https://ok.ru/video/4473789811230"
        self.driver.get(url)

        self.live_stream.log_live_stream()

