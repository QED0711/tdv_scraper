import os

from typing import Union, List
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BrowserInterface:

    def __init__(self, driver=None, option_args=Union[List[str], None], js_snippets: Union[List[str], None]=None,):
        if driver is None:
            driver_options = Options()
            for arg in (option_args if option_args is not None else []):
                driver_options.add_argument(arg if arg.startswith("--") else f"--{arg}")
            # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=driver_options)
            self.driver = webdriver.Chrome(options=driver_options)
        else:
            self.driver = driver

        self.action = ActionChains(self.driver)

        self.symbol_selectors = {}

        if js_snippets is not None:
            for path in js_snippets:
                with open(path, "r") as js:
                    script = js.read()
                    self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})

    #####################
    ##### UTILITIES #####
    #####################

    def _click_element(self, element):
        self.action.move_to_element(element).click().perform()

    def _get_chart_data(self, key: Union[str, None]=None):
        data = self.driver.execute_script("return window._activeChart;")
        return data.get(key) if key is not None else data

    def open(self, url):
        self.driver.get(url)

    def reload(self):
        self.driver.refresh()

    def get_symbols(self,):
        # elements = self.driver.execute_script("""return document.querySelector("[class^='listContainer']").querySelectorAll("[class*='symbolNameText']")""")
        elements = self.driver.execute_script("""return document.querySelectorAll("[class*=symbolNameText]")""")
        for element in elements:
            self.symbol_selectors[element.get_attribute("innerText")] = element
        return self.symbol_selectors

    def change_symbol(self, symbol: str):
       element = self.symbol_selectors.get(symbol)
       if element is not None:
           self._click_element(element)