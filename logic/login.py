from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from infra.handle import Handler
class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, 'ap_email')
    PASSWORD_INPUT = (By.ID, 'ap_password')
    SUBMIT_BUTTON = (By.XPATH, '//input[@type="submit"]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def enter_email(self, email):
        email_input = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_input.send_keys(password)

    def click_sign_in(self):
        sign_in_button = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        sign_in_button.click()

    def login(self):
        myjson=Handler()
        email=myjson.config['username']
        self.enter_email(email)
        password=myjson.config['password']
        self.enter_password(password)
        self.click_sign_in()
