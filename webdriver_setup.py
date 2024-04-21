import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def firefox_browser():
    options = FirefoxOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")

    # Set the path to Firefox binary
    executable_path = os.environ.get("/usr/local/bin/geckodriver")
    return webdriver.Firefox(service=Service(executable_path), options=options)
