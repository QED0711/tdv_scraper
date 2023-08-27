
from classes.browser_interface import BrowserInterface

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'

def main():

    browser = BrowserInterface(
        option_args=[
            "no-sandbox", 
            "disable-dev-shm-usage", 
            "remote-debugging-port=9222", 
            "user-data-dir=/app/browser_data",
            "no-gpu" 
        ],
        load_script="console.log('HELLO WORLD FROM SELENIUM')"
        )

    try:
        # browser.open("https://www.tradingview.com/chart")
        browser.open("https://google.com")
        while True: # keep the process alive
            pass
    except KeyboardInterrupt:
        print("USER TERMINATION")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
