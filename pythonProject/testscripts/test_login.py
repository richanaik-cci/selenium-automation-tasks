import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
Test : A user with valid credentials should able to login successfully
URL : https://login-app-iota.vercel.app
"""


@pytest.mark.login
def test_login_with_valid_user_credentials():
    # Open the browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # navigate to the URl
    driver.get("https://login-app-iota.vercel.app")

    username = "admin"
    password = "admin123"

    username_txtbox = driver.find_element(By.ID, 'username_textbox')
    password_txtbox = driver.find_element(By.ID, 'password_textbox')

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_txtbox.send_keys(username)
    password_txtbox.send_keys(password)
    login_btn.click()
    current_url = driver.current_url
    login_msg = driver.find_element(By.XPATH, "//h1")
    login_msg_txt = login_msg.text

    assert current_url == "https://login-app-iota.vercel.app/about", "URL is incorrect."
    assert login_msg.is_displayed(), "Login message is not displayed."
    assert login_msg_txt == "Welcome to Selenium Learning Group", "Login text message does not match."

    driver.quit()


"""
Test : A user with valid credentials should able to login successfully and logout successfully
URL : https://login-app-iota.vercel.app
"""


@pytest.mark.login
def test_login_logout_with_valid_user_credentials():
    # Open the browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # navigate to the URl
    driver.get("https://login-app-iota.vercel.app")

    username = "admin"
    password = "admin123"

    username_txtbox = driver.find_element(By.ID, 'username_textbox')
    password_txtbox = driver.find_element(By.ID, 'password_textbox')
    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    username_txtbox.send_keys(username)
    password_txtbox.send_keys(password)
    login_btn.click()

    login_msg = driver.find_element(By.XPATH, "//h1")
    login_msg_txt = login_msg.text
    time.sleep(2)
    assert login_msg.is_displayed(), "Login message is not displayed."

    # logout from the app
    logout_btn = driver.find_element(By.XPATH, "//a[text()='Logout']")
    logout_btn.click()
    current_url = driver.current_url

    assert current_url == "https://login-app-iota.vercel.app/login", "URL after logging in is correct."
    assert login_msg_txt == "Welcome to Selenium Learning Group", "Login text message does not match."

    driver.quit()
