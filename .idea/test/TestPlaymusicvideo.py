import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPlaymusicvideo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_playmusicvideo0(self):
    self.driver.get("https://music.youtube.com/")
    self.driver.set_window_size(1366, 701)
    self.driver.find_element(By.ID, "placeholder").click()
    self.driver.find_element(By.CSS_SELECTOR, ".search-box > #input").send_keys("indonesia raya")
    self.driver.find_element(By.CSS_SELECTOR, ".search-box > #input").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "contents").click()
    self.driver.find_element(By.ID, "icon").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".song-media-controls")
    assert len(elements) > 0
  
