from typing import Union, List
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BrowserInterface:

    def __init__(self, driver=None, option_args=Union[List, None], load_script: Union[str, None]=None):
        if driver is None:
            driver_options = Options()
            for arg in (option_args if option_args is not None else []):
                driver_options.add_argument(arg if arg.startswith("--") else f"--{arg}")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=driver_options)
        else:
            self.driver = driver

        self.action = ActionChains(self.driver)

        if load_script is not None:
            self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": load_script})

    def open(self, url):
        self.driver.get(url)