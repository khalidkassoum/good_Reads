import os
import unittest
from logic.ask_author import AskPage
from logic.login import LoginPage
from test import GridTest

class gridtest_ask_author(GridTest):
  def test_ask_author(self,cap):
    self.driver = self.browser.get_driver(cap)
    self.Mylogin = LoginPage(self.driver)
    self.Mylogin.login()
    self.new_ask = AskPage(self.driver)
    self.new_ask.ask_author_flow()
    assert "Your question has been submitted! We’ll notify you if the author answers." in (self.new_ask.validate_success_message())

  def test_run_MyTest(self):

    self.grid=self.browser.get_grid()
    if self.grid:
        self.browser.test_run_grid_parallel(self.test_ask_author)
    else:
        self.browser.test_run_grid_serial(self.test_ask_author)

