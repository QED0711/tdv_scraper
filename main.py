#!/usr/bin/python
import os, time, datetime, pdb
from classes.browser_interface import BrowserInterface
from classes.errors import WatchlistNotFoundError
from environment import HEADLESS_SELENIUM
DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
from keys import ntfy_url

def main():
    ##################################
    ##### SELENIUM BROWSER SETUP #####
    ##################################
    try:
        browser_options = [
                "--no-sandbox", 
                "--disable-dev-shm-usage", 
                "--remote-debugging-port=9222", 
                "--user-data-dir=/app/browser_data",
                "--ignore-certificate-errors",
                "--allow-insecure-localhost",
                "--no-gpu",
            ]

        if HEADLESS_SELENIUM:
            browser_options.append("--headless")

        browser = BrowserInterface(
            option_args=browser_options,
            js_snippets=["/app/javascript/socketListener.js"],
        )

        browser.open("https://www.tradingview.com/chart")
        time.sleep(7) # give some time for the page to load
        browser.screenshot(f"/app/screenshots/{str(datetime.date.today())}.png")
        watchlist_attempts = 0
    except Exception as e:
        os.system(f"""
            curl \
            -H "tdv scraper up" \
            -H "Priority: default" \
            -H "Tags: white_check_mark" \
            -d "tdv scraper status: healthy" \
            {ntfy_url}
        """)
    
    

    #########################
    ##### GET WATCHLIST #####
    #########################
    while True:
        browser.get_watchlist()
        if len(browser.watchlist_selectors) > 0:
            break
        watchlist_attempts += 1
        if watchlist_attempts > 10:
            raise WatchlistNotFoundError()
        time.sleep(5)

    ##########################
    ##### ITERATE CHARTS #####
    ##########################
    while True:
        browser.iterate_watchlist()
        time.sleep(30)


if __name__ == "__main__":
    main()
