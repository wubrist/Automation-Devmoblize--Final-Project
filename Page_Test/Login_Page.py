import time
import allure
from selenium.webdriver.common.by import By

from Base_Test.test_base import Base_test
from Locatore.Login_Locatore import Login_Page_Locatore


class Login_page(Base_test):

    def __init__(self):
        self.login_button = Login_Page_Locatore.login_button

        self.name = Login_Page_Locatore.correct_user_name

        self.passward = Login_Page_Locatore.correct_passward

        self.login = Login_Page_Locatore.login

        self.close = Login_Page_Locatore.close_button

        self.x_button = Login_Page_Locatore.x_path_button

    def common(self):
        super().base_for_web()

    @allure.step
    @allure.description("test_login_username_passward_correct_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_passward_correct_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456")

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_login_username_passward_correct_Close_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_passward_correct_Close_button(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456")

        # self.driver.find_element(By.XPATH, self.login).click()

        self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_login_username_NULL_passward_correct_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_NULL_passward_correct_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456")

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_login_correct_username_passward_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_correct_username_passward_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456")

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_login_username_passward_correct_page_x_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_passward_correct_page_x_button(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456")

        self.driver.find_element(By.XPATH, self.x_button).click()

        # self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_login_username_Page_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_Page_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys()

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456")

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_login_passward_page_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_passward_page_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.passward).send_keys()

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_login_username_passward_page_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_passward_page_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys()

        self.driver.find_element(By.XPATH, self.passward).send_keys()

        self.driver.find_element(By.XPATH, self.login).click()

        # self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_login_username_passward_page_incorrect")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_passward_page_incorrect(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys()

        self.driver.find_element(By.XPATH, self.passward).send_keys()

        self.driver.find_element(By.XPATH, self.login).click()

        self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_login_username_correct_passward_page_incorrect")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_username_correct_passward_page_incorrect(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.login_button).click()

        self.driver.find_element(By.XPATH, self.name).send_keys()

        self.driver.find_element(By.XPATH, self.passward).send_keys()

        self.driver.find_element(By.XPATH, self.login).click()

        self.driver.find_element(By.XPATH, self.close).click()
