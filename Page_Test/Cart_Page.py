import time
import allure
from selenium.webdriver.common.by import By

from Base_Test.test_base import Base_test
from Locatore.Cart_Locatore import Cart_Page_Locatore


class Cart_page(Base_test):

    def __init__(self):
        self.button = Cart_Page_Locatore.cart_button

        self.order = Cart_Page_Locatore.click_place_order_button

        self.name = Cart_Page_Locatore.total_name

        self.country = Cart_Page_Locatore.country_name

        self.city = Cart_Page_Locatore.city_name

        self.card = Cart_Page_Locatore.cridit_carde

        self.month = Cart_Page_Locatore.month

        self.year = Cart_Page_Locatore.year

        self.purchase = Cart_Page_Locatore.purchase

        self.close = Cart_Page_Locatore.close_button

        # self.null = Cart_Page_Locatore.NULL

    def common(self):
        super().base_for_web()

    @allure.step
    @allure.description("test_cart_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.country).send_keys("israel")

        self.driver.find_element(By.XPATH, self.city).send_keys("bersheva")

        self.driver.find_element(By.XPATH, self.card).send_keys("3456789765456787")

        self.driver.find_element(By.XPATH, self.month).send_keys("januray")

        self.driver.find_element(By.XPATH, self.year).send_keys("1/30/2023")

        self.driver.find_element(By.XPATH, self.purchase).click()

        self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_cart_page_Username_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_Username_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("null")

        self.driver.find_element(By.XPATH, self.country).send_keys("israel")

        self.driver.find_element(By.XPATH, self.city).send_keys("bersheva")

        self.driver.find_element(By.XPATH, self.card).send_keys("3456789765456787")

        self.driver.find_element(By.XPATH, self.month).send_keys("januray")

        self.driver.find_element(By.XPATH, self.year).send_keys("1/30/2023")

        # self.driver.find_element(By.XPATH, self.purchase).click()

        self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_cart_page_Country_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_Country_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.country).send_keys()

        self.driver.find_element(By.XPATH, self.city).send_keys("bersheva")

        self.driver.find_element(By.XPATH, self.card).send_keys("3456789765456787")

        self.driver.find_element(By.XPATH, self.month).send_keys("januray")

        self.driver.find_element(By.XPATH, self.year).send_keys("1/30/2023")

        self.driver.find_element(By.XPATH, self.purchase).click()

        self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_cart_page_City_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_City_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.country).send_keys("israel")

        self.driver.find_element(By.XPATH, self.city).send_keys()

        self.driver.find_element(By.XPATH, self.card).send_keys("3456789765456787")

        self.driver.find_element(By.XPATH, self.month).send_keys("januray")

        self.driver.find_element(By.XPATH, self.year).send_keys("1/30/2023")

        self.driver.find_element(By.XPATH, self.purchase).click()

        self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_cart_page_Card_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_Card_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.country).send_keys("israel")

        self.driver.find_element(By.XPATH, self.city).send_keys("bersheva")

        self.driver.find_element(By.XPATH, self.card).send_keys()

        self.driver.find_element(By.XPATH, self.month).send_keys("januray")

        self.driver.find_element(By.XPATH, self.year).send_keys("1/30/2023")

        self.driver.find_element(By.XPATH, self.purchase).click()

        self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_cart_page_month_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_month_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.country).send_keys("israel")

        self.driver.find_element(By.XPATH, self.city).send_keys("bersheva")

        self.driver.find_element(By.XPATH, self.card).send_keys("3456789765456787")

        self.driver.find_element(By.XPATH, self.month).send_keys()

        self.driver.find_element(By.XPATH, self.year).send_keys("1/30/2023")

        self.driver.find_element(By.XPATH, self.purchase).click()

        self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_cart_page_Year_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_Year_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.country).send_keys("israel")

        self.driver.find_element(By.XPATH, self.city).send_keys("bersheva")

        self.driver.find_element(By.XPATH, self.card).send_keys("3456789765456787")

        self.driver.find_element(By.XPATH, self.month).send_keys("januray")

        self.driver.find_element(By.XPATH, self.year).send_keys()

        self.driver.find_element(By.XPATH, self.purchase).click()

        self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_cart_page_Close")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_Close(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.country).send_keys("israel")

        self.driver.find_element(By.XPATH, self.city).send_keys("bersheva")

        self.driver.find_element(By.XPATH, self.card).send_keys("3456789765456787")

        self.driver.find_element(By.XPATH, self.month).send_keys("januray")

        self.driver.find_element(By.XPATH, self.year).send_keys("1/30/2023")

        # self.driver.find_element(By.XPATH, self.purchase).click()
        # time.sleep(3)
        self.driver.find_element(By.XPATH, self.close).click()

