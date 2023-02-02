import allure
import pytest
from pytest import mark
from Page_Test.Cart_Page import Cart_page


class Test_Cart:
    @allure.description("test_cart_page")
    @pytest.mark.sanity
    def test_cart_page(self):
        test = Cart_page()
        test.test_cart_page()

    @allure.description("test_cart_page_Username_NULL")
    @pytest.mark.sanity
    def test_cart_page_Username_NULL(self):
        test = Cart_page()
        test.test_cart_page_Username_NULL()

    @allure.description("test_cart_page_Country_NULL")
    @pytest.mark.sanity
    def test_cart_page_Country_NULL(self):
        test = Cart_page()
        test.test_cart_page_Country_NULL()

    @allure.description("test_cart_page_City_NULL")
    @pytest.mark.sanity
    def test_cart_page_City_NULL(self):
        test = Cart_page()
        test.test_cart_page_City_NULL()

    @allure.description("test_cart_page_Card_NULL")
    @pytest.mark.sanity
    def test_cart_page_Card_NULL(self):
        test = Cart_page()
        test.test_cart_page_Card_NULL()

    @allure.description("test_cart_page_month_NULL")
    @pytest.mark.sanity
    def test_cart_page_month_NULL(self):
        test = Cart_page()
        test.test_cart_page_month_NULL()

    @allure.description("test_cart_page_Year_NULL")
    @pytest.mark.sanity
    def test_cart_page_Year_NULL(self):
        test = Cart_page()
        test.test_cart_page_Year_NULL()

    @allure.description("test_cart_page_Close")
    @pytest.mark.sanity
    def test_cart_page_Close(self):
        test = Cart_page()
        test.test_cart_page_Close()

