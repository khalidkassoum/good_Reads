from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from infra.handle import Handler
class AskPage(BasePage):

    community_button = (By.PARTIAL_LINK_TEXT, 'Community')
    ask_the_author_button=(By.LINK_TEXT,"Ask the Author")
    ask_button=(By.LINK_TEXT,"Ask")
    enter_ask=(By.ID,"qaTextArea")
    flag=(By.ID,"community_question_spoiler_flag")
    ask_Button=(By.CSS_SELECTOR,".primaryAction.submitAction.gr-form__submitButton")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def enter_ask_input(self):
        myjson = Handler()
        askk= myjson.config['ask']
        ask_input = self.wait.until(EC.visibility_of_element_located(self.enter_ask))
        ask_input.send_keys(askk)

    def press_community_button(self):
        COMMUNITY_BUTTON = self.wait.until(EC.element_to_be_clickable(self.community_button))
        COMMUNITY_BUTTON.click()

    def press_ask_author(self):
       ask_element = self.wait.until(EC.element_to_be_clickable(self.ask_the_author_button))
       ask_element.click()

    def press_ask(self):
        pres_ask = self.wait.until(EC.element_to_be_clickable(self.ask_button))
        pres_ask.click()

    def press_flag(self):
        flagg_button = self.wait.until(EC.element_to_be_clickable(self.flag))
        flagg_button.click()

    def press_ask2(self):
        ask_element2 = self.wait.until(EC.element_to_be_clickable(self.ask_Button))
        ask_element2.click()

    def validate_success_message(self):
        success_message_text = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME,"notificationMessage"))
        ).text



        return success_message_text
    def ask_author_flow(self):
        self.press_community_button()
        self.press_ask_author()
        self.press_ask()
        self.enter_ask_input()
        self.press_flag()
        self.press_ask2()
