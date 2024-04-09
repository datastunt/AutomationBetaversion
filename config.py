import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument('--no-sandbox')
options.add_argument("--headless")
executor = Service(os.environ.get("geckodriver.exe"))
driver = webdriver.Firefox(service=executor, options=options)
