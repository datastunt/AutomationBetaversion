import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def firefox_browser():
    options = FirefoxOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    
    # Dynamically find Firefox binary path
    firefox_binary_path = None
    for path in ['/usr/bin/firefox', '/usr/local/bin/firefox', '/usr/lib/firefox/firefox']:
        if os.path.exists(path):
            firefox_binary_path = path
            break

    if firefox_binary_path is None:
        raise FileNotFoundError("Firefox binary not found in expected locations")

    options.binary_location = firefox_binary_path

    # Set path to geckodriver
    executable_path = "/usr/local/bin/geckodriver"
    
    # Create Firefox WebDriver instance
    return webdriver.Firefox(service=Service(executable_path), options=options)


# import os
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options as FirefoxOptions

# def firefox_browser():
#     options = FirefoxOptions()
#     options.add_argument('--no-sandbox')
#     options.add_argument('--headless')
#     firefox_binary_path = "/usr/bin/firefox"  # Adjust this path according to your system
#     options.binary_location = firefox_binary_path
#     executable_path = "/usr/local/bin/geckodriver"
#     # Create Firefox WebDriver instance
#     return webdriver.Firefox(service=Service(executable_path), options=options)
