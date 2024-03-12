import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import unittest
from logic.follow_review import AddFriendPage
from logic.login import LoginPage
from test import GridTest



class gridtest_add_friend(GridTest):


  def test_add_friend(self,cap):
    self.driver = self.browser.get_driver(cap)
    self.Mylogin = LoginPage(self.driver)
    self.Mylogin.login()
    self.add_new_friend = AddFriendPage(self.driver)
    self.add_new_friend.follow_friend_flow()
    assert "following reviews" in (self.add_new_friend.validate_success_message())

  def test_run_MyTest(self):

        self.grid = self.browser.get_grid()
        if self.grid:
            self.browser.test_run_grid_parallel(self.test_add_friend)
        else:
            self.browser.test_run_grid_serial(self.test_add_friend)
