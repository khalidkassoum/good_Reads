import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
from infra.handle import Handler


class RemoveBookgPage(BasePage):

    SEARCH_WINDOW = (By.NAME, 'q')
    book_title_element = (By.XPATH, "//span[@itemprop='name' and contains(text(), 'Chain of Gold (The Last Hours, #1)')]")
    want_to_read_button2=(By.CSS_SELECTOR,".Button.Button--secondary.Button--medium.Button--block")
    remove_from_my_shelf_button =(By.XPATH, "//span[contains(text(), 'Remove from my shelf')]")
    remove_button=(By.XPATH,"//button[@class='Button Button--primary Button--small Button--block' and .//span[text()='Remove']]")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_book(self):
     myjson = Handler()
     book = myjson.config['bookToRead']
     search_window = self.wait.until(EC.visibility_of_element_located(self.SEARCH_WINDOW))
     search_window.clear()
     search_window.send_keys(book)
     search_window.send_keys(Keys.RETURN)
     time.sleep(5)


    def select_book(self):
        book_title_elment= self.wait.until(EC.element_to_be_clickable(self.book_title_element))
        book_title_elment.click()



    def remove_from_wanted(self):
        wanted_to_read_2=self.wait.until(EC.element_to_be_clickable(self.want_to_read_button2))
        wanted_to_read_2.click()
        remove_from_my_list=self.wait.until(EC.element_to_be_clickable(self.remove_from_my_shelf_button))
        remove_from_my_list.click()
        remove_element=self.wait.until(EC.element_to_be_clickable(self.remove_button))
        remove_element.click()

    def validate_success_message(self):
        success_message_text = self.wait.until(
            EC.visibility_of_element_located((By.XPATH,"//div[text()='Removed book from shelves']"))
        ).text



        return success_message_text

    def all_flow(self):
        self.search_book()
        self.select_book()
        self.remove_from_wanted()



