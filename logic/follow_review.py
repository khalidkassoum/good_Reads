from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
class AddFriendPage(BasePage):
    community_button=(By.PARTIAL_LINK_TEXT, 'Community')
    people_button=(By.PARTIAL_LINK_TEXT,"People")
    follow_button=(By.CLASS_NAME,"actionLinkLite")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_community_button(self):
        community_element = self.wait.until(EC.element_to_be_clickable(self.community_button))
        community_element.click()

    def click_people_button(self):
        people_element = self.wait.until(EC.element_to_be_clickable(self.people_button))
        people_element.click()

    def click_follow(self):
        follow_element = self.wait.until(EC.element_to_be_clickable(self.follow_button))
        follow_element.click()

    def validate_success_message(self):

        success_message_text = self.wait.until(
            EC.visibility_of_element_located((By.ID,'follow_link_user_144918815'))
        ).text



        return success_message_text
    def follow_friend_flow(self):
        self.click_community_button()
        self.click_people_button()
        self.click_follow()
        self.click_follow()
        self.click_follow()








