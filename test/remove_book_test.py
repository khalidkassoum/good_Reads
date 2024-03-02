import unittest
from logic.login import LoginPage
from logic.remove_book_logic import RemoveBookgPage
from test import GridTest

class gridtest_removebook(GridTest):

    def test_remove_book(self,cap):
        self.driver = self.browser.get_driver(cap)
        self.Mylogin = LoginPage(self.driver)
        self.Mylogin.login()
        self.remove_book = RemoveBookgPage(self.driver)
        self.remove_book.all_flow()
        assert "Removed book from shelves" in (self.remove_book.validate_success_message().title())


    def test_run_MyTest(self):

        self.grid = self.browser.get_grid()
        if self.grid:
            self.browser.test_run_grid_parallel(self.test_remove_book)
        else:
            self.browser.test_run_grid_serial(self.test_remove_book)


