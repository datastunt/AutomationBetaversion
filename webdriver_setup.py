import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def firefox_browser():
    options = FirefoxOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")

    # Set the path to Firefox binary
    options.binary_location = '/usr/bin/firefox'  # Update this path to your Firefox binary

    executor = "/usr/local/bin/geckodriver"  # Set the path to Geckodriver
    return webdriver.Firefox(service=Service(executor), options=options)
