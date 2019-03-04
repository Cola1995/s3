from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()   #全屏
driver.get("http://124.95.129.86:9000/manage/index")
driver.execute_script("alert('来了，老弟')")