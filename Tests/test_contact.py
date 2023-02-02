import allure
import pytest

from Page_Test.Contact_Page import Contact_page

from pytest import mark
class Test_Contact:
    @allure.description("test_contact_page")
    @pytest.mark.sanity
    def test_contact_page(self):
        test = Contact_page()
        test.test_contact_page()

    @allure.description("test_contact_page_message_null")
    @pytest.mark.sanity
    def test_contact_page_message_null(self):
        test = Contact_page()
        test.test_contact_page_message_null()

    @allure.description("test_contact_page_email_null")
    @pytest.mark.sanity
    def test_contact_page_email_null(self):
        test = Contact_page()
        test.test_contact_page_email_null()

    @allure.description("test_contact_page_username_null")
    @pytest.mark.sanity
    def test_contact_page_username_null(self):
        test = Contact_page()
        test.test_contact_page_username_null()

    @allure.description("test_contact_page_message_null")
    @pytest.mark.sanity
    def test_contact_page_message_Null(self):
        test = Contact_page()
        test.test_contact_page_message_null()

    @allure.description("test_contact_page_close_button")
    @pytest.mark.sanity
    def test_contact_page_close_button(self):
        test = Contact_page()
        test.test_contact_page_close_button()

    @allure.description("test_contact_page_x_button")
    @pytest.mark.sanity
    def test_contact_page_x_button(self):
        test = Contact_page()
        test.test_contact_page_x_button()

    @allure.description("test_contact_page_x_button_incorrect")
    @pytest.mark.sanity
    def test_contact_page_x_button_null_incorrect(self):
        test = Contact_page()
        test.test_contact_page_x_button_null_incorrect()

    @allure.description("test_contact_page_close_button_incorrect")
    @pytest.mark.sanity
    def test_contact_page_close_button_null_incorrect(self):
        test = Contact_page()
        test.test_contact_page_close_button_incorrect()

    @allure.description("test_contact_page_close_button_incorrect")
    @pytest.mark.sanity
    def test_contact_page_send_button_send_button(self):
        test = Contact_page()
        test.test_contact_page_close_button_incorrect()