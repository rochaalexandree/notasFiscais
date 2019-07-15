from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary 
from selenium.webdriver import DesiredCapabilities

mystring = '02963740830'
string = '003749074940'
mystring = mystring.rstrip('0 ')
string = string.rstrip('0 ')
print(mystring)
print(string)


binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\Firefox.exe')
fp = (r'C:\Users\rocha\AppData\Roaming\Mozilla\Firefox\Profiles\2osq2yvc.default')
opts = Options()
opts.profile = fp
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
driver = webdriver.Firefox(capabilities=firefox_capabilities,firefox_binary=binary, firefox_options = opts)

driver.get("https://www.whatsapp.com/download/")
driver.find_element_by_css_selector("#hide_till_load > div._2y_d._7ohy > div._2yyw._2z2z._7ohz > div > div._2zld._2zmp._7oi5._7oi1._2z36 > div:nth-child(1) > div._7oi7 > a").click()