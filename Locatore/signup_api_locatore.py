from random import randint

class RegisterConstants:
    num = randint(1, 2500)
    url_register = 'https://api.demoblaze.com/signup'
    data_valid = {'name': "Alelignalelign",
                  'password': "123"}
    data_invalid_passwerd = {'name': "alelignalelign",
                             'password': "1234"}
    data_invalid_empty_user_name = {'name': " ",
                                    'password': "123"}
    data_invalid_empty_passwerd = {'name': "alelignalelign@#$ ",
                                   'password': ""}
    data_invalid_invalid_user_name = {'name': "alelign ",
                                    'password': "123@#$%"}