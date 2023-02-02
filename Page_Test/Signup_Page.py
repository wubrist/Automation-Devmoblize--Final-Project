import time
import allure
from selenium.webdriver.common.by import By
from Base_Test.test_base import Base_test
from Locatore.signup_locatore import signup_Page_Locatore


class Signup_page(Base_test):

    def __init__(self):
        self.signup_button = signup_Page_Locatore.signup_button

        self.user_name = signup_Page_Locatore.correct_user_name

        self.passward = signup_Page_Locatore.correct_passward

        self.signup = signup_Page_Locatore.signup

        self.close = signup_Page_Locatore.close_signup_button

    #        self.x_button = signup_Page_Locatore.x_button_page

    def common(self):
        super().base_for_web()

    @allure.step
    @allure.description("test_signup_username_passward_correct_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signup_username_passward_correct_page(self):
        self.common()
        self.driver.implicitly_wait(5)

        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.signup_button).click()

        self.driver.find_element(By.XPATH, self.user_name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456345")

        self.driver.find_element(By.XPATH, self.signup).click()

        # self.driver.find_element(By.XPATH, self.close).click()

    @allure.step
    @allure.description("test_signup_username_passward_correct_page_Close_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signup_username_passward_correct_page_Close_button(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.signup_button).click()

        self.driver.find_element(By.XPATH, self.user_name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456345")

        # self.driver.find_element(By.XPATH, self.signup).click()
        # time.sleep(3)
        self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_signup_username_passward_Page_NULL")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signup_username_passward_Page_NULL(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.signup_button).click()

        self.driver.find_element(By.XPATH, self.user_name).send_keys()

        self.driver.find_element(By.XPATH, self.passward).send_keys()

        # self.driver.find_element(By.XPATH, self.signup).click()

        self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_signup_username_NULL_passward_Correct_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signup_username_NULL_passward_Correct_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.signup_button).click()

        self.driver.find_element(By.XPATH, self.user_name).send_keys()

        self.driver.find_element(By.XPATH, self.passward).send_keys("Wub123456345")

        # self.driver.find_element(By.XPATH, self.signup).click()

        self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_signup_username_Correct_passward_null_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signup_username_Correct_passward_null_page(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.signup_button).click()

        self.driver.find_element(By.XPATH, self.user_name).send_keys("Wubrist")

        self.driver.find_element(By.XPATH, self.passward).send_keys()

        self.driver.find_element(By.XPATH, self.signup).click()

        # self.driver.find_element(By.XPATH, self.close).click()

