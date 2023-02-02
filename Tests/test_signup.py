import allure
import pytest
from pytest import mark
from Page_Test.Signup_Page import Signup_page


class Test_Signup:
    @allure.description("test_signup_username_passward_correct_page")
    @pytest.mark.sanity
    def test_signup_page(self):
        test = Signup_page()
        test.test_signup_username_passward_correct_page()

    @allure.description("test_signup_username_passward_correct_page_Close_button")
    @pytest.mark.sanity
    def test_signup_username_passward_correct_page_Close_button(self):
        test = Signup_page()
        test.test_signup_username_passward_correct_page_Close_button()

    @allure.description("test_signup_username_passward_Page_NULL")
    @pytest.mark.sanity
    def test_signup_username_passward_Page_NULL(self):
        test = Signup_page()
        test.test_signup_username_passward_NULL()

    @allure.description("test_signup_username_NULL_passward_Correct_page")
    @pytest.mark.sanity
    def test_signup_username_NULL_passward_Correct_page(self):
        test = Signup_page()
        test.test_signup_username_NULL_passward_Correct_page()

    @allure.description("test_signup_username_Correct_passward_null_page")
    @pytest.mark.sanity
    def test_signup_username_Correct_passward_null_page(self):
        test = Signup_page()
        test.test_signup_username_Correct_passward_null_page()
