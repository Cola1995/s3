from appium import webdriver

desired_caps={}

desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:62001'
desired_caps['platforVersion']='4.4.2'

desired_caps['app']=r'C:\Users\Administrator\Desktop\testU.apk'
desired_caps['appPackage']='com.youjian.migratorybirds'
desired_caps['appActivity']='com.youjian.migratorybirds.android.activity.StartPageActivity'
webdriver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)