import allure
import pytest
from pytest import mark
from Page_Test.Home_Page import Home_page


class Test_Home:
    @allure.description("test_iphone_6")
    @pytest.mark.sanity
    def test_iphon_6(self):
        test = Home_page()
        test.test_iphone_6()

    @allure.description("test_samsung_s6")
    @pytest.mark.sanity
    def test_sumsung_s(self):
        test = Home_page()
        test.test_samsung_s6()

    @allure.description("test_assus")
    @pytest.mark.sanity
    def test_assus_full_HD(self):
        test = Home_page()
        test.test_assus()

    @allure.description("test_apple_monitor")
    @pytest.mark.sanity
    def test_Apple_Monitor(self):
        test = Home_page()
        test.test_apple_monitor()

    @allure.description("Test_Nokia_Lumui")
    @pytest.mark.sanity
    def test_Nokia_Lumi(self):
        test = Home_page()
        test.Test_Nokia_Lumui()








