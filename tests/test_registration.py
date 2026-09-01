import uuid

from models.user import User
from pages.registration_page import RegistrationPage

VALID_EMAIL = 'aleks_timov@gmail.com'
VALID_PASSWORD = '1234567$Com'
INVALID_EMAIL = 'alekstimov.com'
INVALID_PASSWORD = '1234Com'

def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        f"tony_{random_suffix}@gmail.com",
        "Password123$"

    )
    print(random_suffix)

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert registration_page.is_logged() is True

def test_registration_wrong_email(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_form()
    registration_page.fill_email(INVALID_EMAIL)
    registration_page.fill_password(VALID_PASSWORD)
    registration_page.submit_registration()

    assert 'Wrong email or password format' in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "",
        "Password123$"
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert 'Wrong email or password format' in registration_page.get_alert_text()
    registration_page.accept_alert()


def test_registration_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_form()
    registration_page.fill_email(VALID_EMAIL)
    registration_page.fill_password(INVALID_PASSWORD)
    registration_page.submit_registration()

    assert 'Wrong email or password format' in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "aleks_timov@gmail.com",
        ""

    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert 'Wrong email or password format' in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_exists_user(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open_registration_form()
    registration_page.fill_email('alekstimov@gmail.com')
    registration_page.fill_password('1234567$Com')
    registration_page.submit_registration()

    assert registration_page.get_alert_text()=='User already exist'
    registration_page.accept_alert()