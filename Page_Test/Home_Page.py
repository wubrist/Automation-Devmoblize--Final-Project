import time
import allure
from selenium.webdriver.common.by import By

from Base_Test.test_base import Base_test
from Locatore.Home_Locators import Home_Page_Locators


class Home_page(Base_test):

    def __init__(self):
        self.iphone = Home_Page_Locators.iphone_6
        self.Add_Cart = Home_Page_Locators.Add_to_cart
        self.iphone_Assert = Home_Page_Locators.ipone_name
        self.cart = Home_Page_Locators.cart
        self.samsung = Home_Page_Locators.samsung_s6
        self.sums_assert = Home_Page_Locators.sumsung_name
        self.Next = Home_Page_Locators.next_button
        self.Sony = Home_Page_Locators.sony_vaio_5
        self.sony_name = Home_Page_Locators.Sony_name
        self.laptop = Home_Page_Locators.laptop_button
        self.monitor = Home_Page_Locators.monitor_button
        self.Apple_Monitor = Home_Page_Locators.Apple_monitor
        self.Apple_Name = Home_Page_Locators.Apple_name
        self.Nokia_lu = Home_Page_Locators.nokia_lumi
        self.Nokia_Name = Home_Page_Locators.Nokia_lumi_delete

    def common(self):
        super().base_for_web()

    @allure.step
    @allure.description("test_cart_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_iphone_6(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.iphone).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()

        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title = self.driver.find_element(By.XPATH, self.iphone_Assert).text
        assert title == "Iphone 6 32gb"


    @allure.step
    @allure.description("test_cart_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_samsung_s6(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.samsung).click()
      
        self.driver.find_element(By.XPATH, self.Add_Cart).click()

        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title2 = self.driver.find_element(By.XPATH, self.sums_assert).text
        assert title2 == "Samsung galaxy s6"


    @allure.step
    @allure.description("test_assus")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_assus(self):
        self.common()
        self.driver.implicitly_wait(5)

        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.Sony).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()

        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title3 = self.driver.find_element(By.XPATH, self.sony_name).text
        assert title3 == "Sony vaio i5"


    @allure.step
    @allure.description("test_apple_monitor")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_apple_monitor(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.monitor).click()

        self.driver.find_element(By.XPATH, self.Apple_Monitor).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()

        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title3 = self.driver.find_element(By.XPATH, self.Apple_Name).text
        assert title3 == "Apple monitor 24"


    @allure.step
    @allure.description("Test_Nokia_Lumui")
    @allure.severity(allure.severity_level.CRITICAL)
    def Test_Nokia_Lumui(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.Nokia_lu).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()

        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        self.driver.find_element(By.XPATH, self.Nokia_Name).click()

