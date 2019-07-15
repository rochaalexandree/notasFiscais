from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import DesiredCapabilities

## Seta as preferencias de Download do chrome ##


def optionsDownAAA(defaultDirectory):
    download_dir = defaultDirectory
    chromeOptions = webdriver.ChromeOptions()
    preferences = {"download.default_directory": download_dir,
                   "download.prompt_for_download": False,
                   "directory_upgrade": True,
                   "safebrowsing.enabled": True}
    chromeOptions.add_experimental_option("prefs", preferences)
    chromedriver = "chromedriver.exe"
    # chromeOptions.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path=chromedriver, chrome_options=chromeOptions)

    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {
        'behavior': 'allow', 'downloadPath': download_dir}}
    command_result = driver.execute("send_command", params)

    return driver


def optionsDown(defaultDirectory):
    download_dir = defaultDirectory
    print(download_dir)
    # time.sleep(100)

    binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\Firefox.exe')
    fp = (r'C:\Users\rocha\AppData\Roaming\Mozilla\Firefox\Profiles\2osq2yvc.default')  
    opts = Options()
    opts.profile = fp
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    driver = webdriver.Firefox(capabilities=firefox_capabilities,firefox_binary=binary, firefox_options = opts)

    return driver 
