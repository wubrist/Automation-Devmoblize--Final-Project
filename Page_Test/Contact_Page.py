import time
import allure
from selenium.webdriver.common.by import By

from Base_Test.test_base import Base_test
from Locatore.Contact_Locatore import Contact_Page_Locatore


class Contact_page(Base_test):

    def __init__(self):
        self.button = Contact_Page_Locatore.contact_button

        self.email = Contact_Page_Locatore.contact_email

        self.name = Contact_Page_Locatore.contact_name

        self.message = Contact_Page_Locatore.contact_message

        self.send = Contact_Page_Locatore.contact_send_message

        self.close = Contact_Page_Locatore.close_send_message

        self.x_button = Contact_Page_Locatore.x_button

    def common(self):
        super().base_for_web()

    @allure.step
    @allure.description("test_contact_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.email).send_keys("wubristasnakew@gmail.com")

        self.driver.find_element(By.XPATH, self.name).send_keys("wubrist")

        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")

        self.driver.find_element(By.XPATH, self.send).click()


    @allure.step
    @allure.description("test_contact_page_email_null")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_email_null(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.email).send_keys("")

        self.driver.find_element(By.XPATH, self.name).send_keys("wubrist")

        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")

        self.driver.find_element(By.XPATH, self.send).click()


    @allure.step
    @allure.description("test_contact_page_username_null")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_username_null(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.email).send_keys("wubristasnakew@gmail.com")

        self.driver.find_element(By.XPATH, self.name).send_keys("")

        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")

        self.driver.find_element(By.XPATH, self.send).click()


    @allure.step
    @allure.description("test_contact_page_message_null")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_message_null(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.email).send_keys("wubristasnakew@gmail.com")

        self.driver.find_element(By.XPATH, self.name).send_keys("wubrist")

        self.driver.find_element(By.XPATH, self.message).send_keys()

        self.driver.find_element(By.XPATH, self.send).click()


    @allure.step
    @allure.description("test_contact_page_close_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_close_button(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.email).send_keys("wubristasnakew@gmail.com")

        self.driver.find_element(By.XPATH, self.name).send_keys("wubrist")

        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")

        self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_contact_page_NULL_username_Passward")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_NULL_username_Passward(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.email).send_keys("wubristasnakew@gmail.com")

        self.driver.find_element(By.XPATH, self.name).send_keys()

        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")

        self.driver.find_element(By.XPATH, self.send).click()


    @allure.step
    @allure.description("test_contact_page_x_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_x_button(self):
        self.common()
        self.driver.implicitly_wait(5)

        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.email).send_keys("wubristasnakew@gmail.com")

        self.driver.find_element(By.XPATH, self.name).send_keys("wubrist")

        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")

        # self.driver.find_element(By.XPATH, self.send).click()
        # time.sleep(3)
        self.driver.find_element(By.XPATH, self.x_button).click()


    @allure.step
    @allure.description("test_contact_page_x_button_incorrect_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_x_button_incorrect_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.email).send_keys("wubristasnakew@gmail.com")

        self.driver.find_element(By.XPATH, self.name).send_keys("wubrist")

        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")

        # self.driver.find_element(By.XPATH, self.send).click()

        self.driver.find_element(By.XPATH, self.x_button).click()


    @allure.step
    @allure.description("test_contact_page_close_button_incorrect_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_close_button_incorrect_page(self):
        self.common()
        self.driver.implicitly_wait(5)

        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.email).send_keys("wubristasnakew@gmail.com")

        self.driver.find_element(By.XPATH, self.name).send_keys("wubrist")

        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")

        # self.driver.find_element(By.XPATH, self.send).click()
        self.driver.find_element(By.XPATH, self.x_button).click()


    @allure.step
    @allure.description("test_contact_page_send_button_incorrect")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_contact_page_send_button_incorrect(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.email).send_keys("wubristasnakew@gmail.com")

        self.driver.find_element(By.XPATH, self.name).send_keys("wubrist")

        self.driver.find_element(By.XPATH, self.message).send_keys("Hellow world")

        self.driver.find_element(By.XPATH, self.send).click()

        self.driver.find_element(By.XPATH, self.x_button).click()
