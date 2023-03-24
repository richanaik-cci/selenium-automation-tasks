import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.login1
def test_google_search():
    # Open the browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # navigate to the URl
    driver.get("https://www.duckduckgo.com/")

    google_search_txtbox = driver.find_element(By.XPATH, "//input[@id='searchbox_input']")
    google_search_txtbox.send_keys("Selenium webdriver")
    search_btn=driver.find_element(By.XPATH, "//*[@id='searchbox_homepage']/div[1]/div/button[2]")
    search_btn.click()

    '''
    search_result_text = driver.find_element(By.XPATH, "//body[@id='gsr']/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']")
    search_text: object=search_result_text.text()
    assert 'selenium' in search_text
    '''