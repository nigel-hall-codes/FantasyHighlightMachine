import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pandas as pd
import re
import urllib

class ProFootballPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.pro-football-reference.com/"

    def open_week_games(self, week_number: int):
        url = self.base_url + f"years/2022/week_{week_number}.htm"
        self.driver.get(url)

    def games(self):
        game_summaries = self.driver.find_elements(By.CLASS_NAME, "game_summary")




