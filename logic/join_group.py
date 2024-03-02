import time
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage

class joinGroupPage(BasePage):

     community_button = (By.PARTIAL_LINK_TEXT,'Community')
     groups_button=(By.PARTIAL_LINK_TEXT,'Groups')
     selectt_group=(By.PARTIAL_LINK_TEXT,'Booktok')

     join_group_button=(By.PARTIAL_LINK_TEXT,'Join')
     notification_only_button=(By.ID,"user_subscription_frequency_n")
     edit_membership_button=(By.PARTIAL_LINK_TEXT,'Edit Membership')
     leave_group_button=(By.PARTIAL_LINK_TEXT,'Leave this group')
     leave_group_button2=(By.XPATH, "//button[@type='submit']")
          # selected_group_button=(By.PARTIAL_LINK_TEXT,'Librarians Group')
          # second_group=(By.PARTIAL_LINK_TEXT,'Read With Jenna')
          # third_group=(By.PARTIAL_LINK_TEXT,'Shared Shelf')


     def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


     def press_community_button(self):
        COMMUNITY_BUTTON = self.wait.until(EC.element_to_be_clickable(self.community_button))
        COMMUNITY_BUTTON.click()


     def press_groups_button(self):
        groups_BUTTON = self.wait.until(EC.element_to_be_clickable(self.groups_button))
        groups_BUTTON.click()

     def press_select_group(self):
         select_button=self.wait.until(EC.element_to_be_clickable(self.selectt_group))
         select_button.click()

     def join_group(self):
      JOIN_GROUP = self.wait.until(EC.element_to_be_clickable(self.join_group_button))
      JOIN_GROUP.click()

     def select_notification(self):
        SELECT_NOTIFICATION_BUT= self.wait.until(EC.element_to_be_clickable(self.notification_only_button))
        SELECT_NOTIFICATION_BUT.click()


     def leave_group(self):

          EDIT_MEMBERSHIP=self.wait.until((EC.element_to_be_clickable(self.edit_membership_button)))
          EDIT_MEMBERSHIP.click()
          LEAVE_GROUP=self.wait.until((EC.element_to_be_clickable(self.leave_group_button)))
          LEAVE_GROUP.click()
          LEAVE_GROUP2=self.wait.until((EC.element_to_be_clickable(self.leave_group_button2)))
          LEAVE_GROUP2.click()


     def join_the_group(self):
        self.join_group()
        self.select_notification()
        self.join_group()



     def join_OR_LEAVE_group_flow(self):


        self.press_community_button()
        self.press_groups_button()
        self.press_select_group()
        flag=self.wait.until(EC.presence_of_element_located(self.selectt_group))
        if flag:
            self.join_the_group()
        else :
         self.leave_group()



