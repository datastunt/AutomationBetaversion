import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def firefox_browser():
    options = FirefoxOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")

    # Adjust the Geckodriver path according to your Docker setup
    geckodriver_path = "/usr/local/bin/geckodriver"

    service = Service(geckodriver_path)  # Set the path to Geckodriver

    return webdriver.Firefox(service=service, options=options)
