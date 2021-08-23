or_login = "123"
or_password = "serg123"

login = input('Enter your login: ')
password = input('Enter your password: ')

if login == or_login and password == or_password:
    print('Hello!')
else:
    print('invalid username or password')
