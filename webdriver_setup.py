import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def firefox_browser():
    options = FirefoxOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    firefox_binary_path = "/usr/bin/firefox"  # Adjust this path according to your system
    options.binary_location = firefox_binary_path
    executable_path = "/usr/local/bin/geckodriver"
    # Create Firefox WebDriver instance
    return webdriver.Firefox(service=Service(executable_path), options=options)


# def firefox_browser():
#     options = FirefoxOptions()
#     # options.add_argument('--no-sandbox')
#     # options.add_argument("--headless")
#     executable_path = Service(os.environ.get("geckodriver.exe"))
#     return webdriver.Firefox(service=executable_path, options=options)



# def firefox_browser():
#     options = FirefoxOptions()
#     options.add_argument('--no-sandbox')
#     options.add_argument('--headless')
#     firefox_binary_path = "/usr/bin/firefox"  # Adjust this path according to your system
#     options.binary_location = firefox_binary_path
#     executable_path = "/usr/local/bin/geckodriver"
#     # Create Firefox WebDriver instance
#     return webdriver.Firefox(service=Service(executable_path), options=options)



