import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def firefox_browser():
    options = FirefoxOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    # executable_path = Service(os.environ.get("geckodriver.exe"))
    # return webdriver.Firefox(service=executable_path, options=options)
    return webdriver.Firefox(options=options)
