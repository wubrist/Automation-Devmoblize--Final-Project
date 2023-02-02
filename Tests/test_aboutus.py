import allure
import pytest
from pytest import mark
from Page_Test.Aboutus_Page import Aboutus_page


class Test_Aboutus:
    @allure.description("test_aboutus_page")
    @pytest.mark.sanity
    def test_Aboutus_page(self):
        test = Aboutus_page()
        test.test_aboutus_page()

    @allure.description("test_aboutus_x_button_page")
    @pytest.mark.sanity
    def test_aboutus_x_button_page(self):
        test = Aboutus_page()
        test.test_aboutus_x_button_page()

    @allure.description("test_aboutus_close_button_page")
    @pytest.mark.sanity
    def test_aboutus_close_button_page(self):
        test = Aboutus_page()
        test.test_aboutus_close_button_page()

