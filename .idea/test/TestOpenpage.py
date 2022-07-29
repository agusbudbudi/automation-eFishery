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

class TestOpenpage():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_openpage(self):
    self.driver.get("https://music.youtube.com/")
    self.driver.set_window_size(1366, 701)
    elements = self.driver.find_elements(By.ID, "left-content")
    assert len(elements) > 0
    self.driver.close()
  
