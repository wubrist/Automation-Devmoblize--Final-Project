import allure
import requests
from pytest import mark
from Locatore.login_api_locatore import LoginConstants


class Test_Login:
    @allure.description('Login correctly')
    def test_login_correctly(self):
        url = LoginConstants.url_login
        data = LoginConstants.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description('Login username correctly')
    def test_login__username_correctly(self):
        url = LoginConstants.url_login
        data = LoginConstants.data_valid
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 20

    @allure.description('Login when password correctly')
    def test_login_with_incorrectly_password(self):
        url = LoginConstants.url_login
        data = LoginConstants.data_invalid_password
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
        assert res_data[LoginConstants.success_key] == False
        assert res_data[LoginConstants.message_key] == "password or email incorrect"

    @allure.description('Login when email correctly')
    def test_login_with_incorrectly_email(self):
        url = LoginConstants.url_login
        data = LoginConstants.data_invalid_email
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10





