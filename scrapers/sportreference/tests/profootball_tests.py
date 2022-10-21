import time
import unittest
from selenium import webdriver
from ..page_objects import profootball_page

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r"sportreference/webdrivers/chromedriver.exe")
        self.profootball_page = profootball_page.ProFootballPage(self.driver)

    def test_open_week_games_page(self):
        week = 5
        self.profootball_page.open_week_games(week)

        time.sleep(5)


