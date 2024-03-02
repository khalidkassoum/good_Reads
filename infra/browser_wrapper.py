
from infra.handle import Handler

from selenium import webdriver
import concurrent.futures

class BrowserWrapper:

    def get_caps(self):
        chrome_cap = webdriver.ChromeOptions()
        chrome_cap.capabilities['platformName'] = 'windows'
        fireFox_cap = webdriver.FirefoxOptions()
        fireFox_cap.capabilities['platformName'] = 'windows'
        edge_cap = webdriver.EdgeOptions()
        edge_cap.capabilities['platformName'] = 'windows'
        cap_list = [chrome_cap, fireFox_cap, edge_cap]
        return cap_list

    def get_grid(self):
        myjson = Handler()
        Grid = myjson.config['grid']
        return Grid
    def get_driver(self,option):
        myjson = Handler()
        hub_url = myjson.config['url_hub']
        myjson = Handler()
        url = myjson.config['url']
        driver = webdriver.Remote(command_executor=hub_url, options=option)
        driver.get(url)
        return driver



    def test_run_grid_serial(self,test_execute):
        caps=self.get_caps()
        for cap in caps:
            test_execute(cap)

    def test_run_grid_parallel(self,test_execute):
        #max_workers = len(caps)
        caps=self.get_caps()
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(caps)) as executor:
           futures= [executor.submit(test_execute,cap) for cap in caps]
           for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Test run encountered an exception: {e}")


