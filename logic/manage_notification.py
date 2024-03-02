from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage
class ManageNotificationPage(BasePage):

    notifications_button=(By.XPATH,"//span[contains(@class, 'headerPersonalNav__icon--notifications')]")
    view_all_notifications=(By.XPATH,"//div[@class='siteHeader__dropdownHeading']/h3")
    manage_my_notifications=(By.LINK_TEXT,"manage my notifications")
    load_more_button=(By.PARTIAL_LINK_TEXT,'Load More')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)



    def click_notifications(self):
        notification_element = self.wait.until(EC.element_to_be_clickable(self.notifications_button))
        notification_element.click()

    def click_view_allnotifications(self):
        view_button = self.wait.until(EC.element_to_be_clickable(self.view_all_notifications))
        view_button.click()




    def click_load_More(self):
        loadmore_button= self.wait.until(EC.element_to_be_clickable(self.load_more_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", loadmore_button)
        loadmore_button.click()


    def manage_notification_flow(self):
        self.click_notifications()
        self.click_view_allnotifications()
        self.click_load_More()
