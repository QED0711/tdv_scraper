from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'

def main():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--user-data-dir=/home/user/app/browser_data')

    # chrome_options.add_argument('--display=:99')
    chrome_options.add_argument('--no-gpu')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        driver.get("https://www.tradingview.com/chart")
        while True:
            pass
    except Exception as e:
        print(str(e))
    finally:
        print("SUCCESS - CLOSING")
        # driver.quit()

if __name__ == "__main__":
    main()
