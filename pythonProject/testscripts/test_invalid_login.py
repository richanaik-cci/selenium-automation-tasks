import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
Test : A user with invalid username should not able to login 
URL : https://login-app-iota.vercel.app
"""


@pytest.mark.login
def test_login_with_invalid_username():
    # Open the browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # navigate to the URl
    driver.get("https://login-app-iota.vercel.app")

    username = "admin1"
    password = "admin123"

    username_txtbox = driver.find_element(By.ID, 'username_textbox')
    password_txtbox = driver.find_element(By.ID, 'password_textbox')

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_txtbox.send_keys(username)
    password_txtbox.send_keys(password)
    login_btn.click()
    current_url = driver.current_url

    # fetch error message
    error_msg = driver.find_element(By.XPATH, "//button[@type='submit']/following::div[1]")
    error_msg_text = error_msg.text
    error_msg.is_displayed(), "Error message is not displayed."

    assert current_url == "https://login-app-iota.vercel.app/login", "URL after logging in is correct."
    assert error_msg_text == 'Invalid Credentials', "Invalid credentials message not displayed."


"""
Test : A user with invalid password should not able to login 
URL : https://login-app-iota.vercel.app
"""


@pytest.mark.login
def test_login_with_invalid_password():
    # Open the browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # navigate to the URl
    driver.get("https://login-app-iota.vercel.app")

    username = "admin"
    password = "admin1234"

    username_txtbox = driver.find_element(By.ID, 'username_textbox')
    password_txtbox = driver.find_element(By.ID, 'password_textbox')

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_txtbox.send_keys(username)
    password_txtbox.send_keys(password)
    login_btn.click()
    current_url = driver.current_url

    # fetch error message
    error_msg = driver.find_element(By.XPATH, "//button[@type='submit']/following::div[1]")
    error_msg_text = error_msg.text
    error_msg.is_displayed(), "Error message is not displayed."

    assert current_url == "https://login-app-iota.vercel.app/login", "URL after logging in is correct."
    assert error_msg_text == 'Invalid Credentials', "Invalid credentials message not displayed."
