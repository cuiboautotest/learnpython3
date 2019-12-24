from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://user.qunar.com/passport/login.jsp?')
driver.maximize_window()
#对页面进行截图
driver.save_screenshot('quna.png')