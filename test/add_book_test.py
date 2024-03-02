import unittest
from logic.login import LoginPage
from logic.search_logic import SearchgPage
from test import GridTest
class gridtest_search(GridTest):

    def test_search(self,cap):
        self.driver = self.browser.get_driver(cap)
        self.Mylogin = LoginPage(self.driver)
        self.Mylogin.login()
        self.search_pagee = SearchgPage(self.driver)
        self.search_pagee.all_flow()
        assert "Shelved as wanted to read" in (self.search_pagee.validate_success_message().title())


    def test_run_MyTest(self):

        self.grid = self.browser.get_grid()
        if self.grid:
            self.browser.test_run_grid_parallel(self.test_search)
        else:
            self.browser.test_run_grid_serial(self.test_search)


