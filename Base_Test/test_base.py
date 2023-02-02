from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



class Base_test():

    def base_for_web(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        return self.driver

    def close(self):
        self.driver.quit()
        self.driver.close()


