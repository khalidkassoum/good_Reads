import os
import unittest

from logic.login import LoginPage
from logic.manage_notification import ManageNotificationPage
from test import GridTest


class gridtest_manage_notification(GridTest):

  def test_manage_notifications(self, cap):
    self.driver = self.browser.get_driver(cap)
    self.Mylogin = LoginPage(self.driver)
    self.Mylogin.login()
    self.manage_nots = ManageNotificationPage(self.driver)
    self.manage_nots.manage_notification_flow()
    assert "https://www.goodreads.com/notifications" in self.driver.current_url



  def test_run_MyTest(self):

    self.grid=self.browser.get_grid()
    if self.grid:
        self.browser.test_run_grid_parallel(self.test_manage_notifications)
    else:
       self.browser.test_run_grid_serial(self.test_manage_notifications)

