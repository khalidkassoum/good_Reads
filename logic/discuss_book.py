from logging import Handler

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from infra.handle import Handler
class DiscussBookPage(BasePage):

    discussions_button=(By.XPATH,"//span[@class='headerPersonalNav__icon headerPersonalNav__icon--discussions']")
    start_new_topic=(By.PARTIAL_LINK_TEXT,'start new')
    enter_your_book_name=(By.ID,'context_id_ac_1')
    choose_book=(By.CLASS_NAME,"autocompleteSearchText")
    enter_topic_title=(By.ID,'topic_title')
    click_window=(By.ID,'topic_question_flag')
    comment_input=(By.ID,'comment_body_usertext')
    post_button=(By.XPATH,"//input[@value='Post']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def press_discuss_button(self):
         disusion_element=self.wait.until(EC.element_to_be_clickable(self.discussions_button))
         disusion_element.click()

    def press_start_topic(self):
        start_topic=self.wait.until(EC.element_to_be_clickable(self.start_new_topic))
        start_topic.click()
    def enter_book_name(self):
        myjson = Handler()
        book_toDiscuss =myjson.config['bookToDiscuss']
        book_input = self.wait.until(EC.visibility_of_element_located(self.enter_your_book_name))
        #book_input.clear()
        book_input.send_keys(book_toDiscuss)

    def choose_your_book(self):
        choose_element = self.wait.until(EC.element_to_be_clickable(self.choose_book))
        choose_element.click()

    def enter_the_topic(self):
        myjson = Handler()
        topic = myjson.config['topic']
        topic_input = self.wait.until(EC.visibility_of_element_located(self.enter_topic_title))
        topic_input.clear()
        topic_input.send_keys(topic)

    def click_windoww(self):
        click_small_window = self.wait.until(EC.element_to_be_clickable(self.click_window))
        click_small_window.click()

    def write_comment(self):
        myjson = Handler()
        comment = myjson.config['comment']
        commnet_element = self.wait.until(EC.visibility_of_element_located(self.comment_input))
        commnet_element.clear()
        commnet_element.send_keys(comment)

    def click_post_button(self):
        click_post_button = self.wait.until(EC.element_to_be_clickable(self.post_button))
        click_post_button.click()

    def validate_success_message(self):
        success_message_text = self.wait.until(
            EC.visibility_of_element_located(
                ((By.ID,"header_notice_container" )))).text

        return success_message_text

    def discuss_a_book_flow(self):
        self.press_discuss_button()
        self.press_start_topic()
        self.enter_book_name()
        self.choose_your_book()
        self.enter_the_topic()
        self.click_windoww()
        self.write_comment()
        self.click_post_button()
