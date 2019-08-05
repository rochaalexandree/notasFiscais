from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import DesiredCapabilities

## Seta as preferencias de Download do chrome ##


# def optionsDown(defaultDirectory):
#     download_dir = defaultDirectory
#     chromeOptions = webdriver.ChromeOptions()
#     preferences = {"download.default_directory": download_dir,
#                    "download.prompt_for_download": False,
#                    "directory_upgrade": True,
#                    "safebrowsing.enabled": True}
#     chromeOptions.add_experimental_option("prefs", preferences)
#     chromedriver = "chromedriver.exe"
#     # chromeOptions.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

#     #driver.command_executor._commands["send_command"] = (
#     #    "POST", '/session/$sessionId/chromium/send_command')
#     #params = {'cmd': 'Page.setDownloadBehavior', 'params': {
#     #    'behavior': 'allow', 'downloadPath': download_dir}}
#     #command_result = driver.execute("send_command", params)

#     return driver


# def optionsDown(defaultDirectory):
#     download_dir = defaultDirectory
#     print(download_dir)
#     # time.sleep(100)

#     binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
#     #fp = (r'C:\Users\RobCav1\AppData\Roaming\Mozilla\Firefox\Profiles\fqpgbzl9.default')  
#     fp = (r'C:\Users\rocha\AppData\Roaming\Mozilla\Firefox\Profiles\quv7tnv1.default')
#     opts = Options()
#     opts.binary = binary
#     opts.profile = fp
#     firefox_capabilities = DesiredCapabilities.FIREFOX
#     firefox_capabilities['marionette'] = True
#     driver = webdriver.Firefox(capabilities=firefox_capabilities,firefox_binary=binary, firefox_options = opts)

#     return driver 

def optionsDown(defaultDirectory):
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "/down")
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip, application/zip, application/xml")

    driver = webdriver.Firefox(firefox_profile=profile)

    return driver