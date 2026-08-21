from Pages.Login_page import LoginPage

VALID_EMAIL = 'alekstimov@gmail.com'
VALID_PASSWORD = '1234567$Com'
INVALID_EMAIL = 'alekstimov.com'
INVALID_PASSWORD = '1234Com'

def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.is_logged() is True

def test_login_with_wrong_email(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.get_alert_text() == 'Wrong email or password'
    login_page.accept_alert()


def test_login_with_wrong_password(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(INVALID_PASSWORD)
    login_page.submit_login()

    assert login_page.get_alert_text() == 'Wrong email or password'
    login_page.accept_alert()

def test_login_with_unregistered_user(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email('alekstim@bk.ru')
    login_page.fill_password('1234567$Com')
    login_page.submit_login()

    assert login_page.get_alert_text() == 'Wrong email or password'
    login_page.accept_alert()