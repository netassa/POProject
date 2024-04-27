import time
from selenium import webdriver


server = 'http://localhost:4444'
options = webdriver.EdgeOptions()
driver = webdriver.Remote(command_executor=server, options=options)
driver.get('http://www.baidu.com')
time.sleep(60)
driver.quit()
