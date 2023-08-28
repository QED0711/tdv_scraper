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
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=driver_options)
        else:
            self.driver = driver

        self.action = ActionChains(self.driver)

        if js_snippets is not None:
            for path in js_snippets:
                with open(path, "r") as js:
                    script = js.read()
                    self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})

    def open(self, url):
        self.driver.get(url)

    def get_symbols(self,):
        self.symbol_elements = self.driver.execute_script("""return document.querySelector("[class^='listContainer']").querySelectorAll("div[draggable=true]")""")

        print(self.symbol_elements)
        # TODO: write utility functions to "click" and element (move mouse to and click)
        # once we have the symbols, parse out the symbol name and store in dict in this format {sym_name: element}