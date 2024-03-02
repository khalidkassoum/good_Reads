import unittest
from logic.join_group import joinGroupPage
from logic.login import LoginPage
from test import GridTest
class gridtest_join_group(GridTest):

    def test_join_group(self,cap):
        self.driver = self.browser.get_driver(cap)
        self.Mylogin = LoginPage(self.driver)
        self.Mylogin.login()
        self.join_groupp = joinGroupPage(self.driver)
        self.counter += 1
        self.join_groupp.join_OR_LEAVE_group_flow()

    def test_run_MyTest(self):

        self.grid = self.browser.get_grid()
        if self.grid:
            self.browser.test_run_grid_parallel(self.test_join_group)
        else:
            self.browser.test_run_grid_serial(self.test_join_group)
