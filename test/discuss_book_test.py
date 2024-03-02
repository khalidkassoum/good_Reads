import unittest
from logic.discuss_book import DiscussBookPage
from logic.login import LoginPage
from test import GridTest
class gridtest_discuss_book(GridTest):

  def test_discuus_book(self,cap):
    self.driver = self.browser.get_driver(cap)
    self.Mylogin = LoginPage(self.driver)
    self.Mylogin.login()
    self.discuss_my_book = DiscussBookPage(self.driver)
    self.discuss_my_book.discuss_a_book_flow()
    assert "Your topic was posted." in (self.discuss_my_book.validate_success_message())



  def test_run_MyTest(self):

    self.grid=self.browser.get_grid()
    if self.grid:
        self.browser.test_run_grid_parallel(self.test_discuus_book)
    else:
        self.browser.test_run_grid_serial(self.test_discuus_book)
