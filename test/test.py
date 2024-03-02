import concurrent
import unittest
from infra.browser_wrapper import BrowserWrapper


class GridTest(unittest.TestCase):


    def setUp(self):
      self.browser=BrowserWrapper()
      self.cap_list = self.browser.get_caps()






