
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


def firefox_browser():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.binary_location = r'/usr/bin/firefox-esr'
    # Set the path to Firefox binary
    service = Service('/usr/local/bin/geckodriver')
    return webdriver.Firefox(options=options, service=service)
