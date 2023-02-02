import time
import allure
from selenium.webdriver.common.by import By

from Base_Test.test_base import Base_test
from Locatore.Aboutus_Locatore import AboutUs_Page_Locatore

from selenium.webdriver.support.wait import WebDriverWait

class Aboutus_page(Base_test):

    def __init__(self):
        self.button = AboutUs_Page_Locatore.Aboutus_button

        self.link = AboutUs_Page_Locatore.Aboutus_link

        self.close = AboutUs_Page_Locatore.Close_button_link

        self.x_button = AboutUs_Page_Locatore.x_button

    def common(self):
        super().base_for_web()


    @allure.step
    @allure.description("test_aboutus_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_aboutus_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.link).click()

        self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_aboutus_x_button_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_aboutus_x_button_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        # self.driver.find_element(By.XPATH, self.link).click()

        self.driver.find_element(By.XPATH, self.x_button).click()

    @allure.step
    @allure.description("test_aboutus_close_button_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_aboutus_close_button_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.link).click()

        # self.driver.find_element(By.XPATH, self.x_button).click()

        self.driver.find_element(By.XPATH, self.close).click()


