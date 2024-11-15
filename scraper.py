import selenium.webdriver as wd
from selenium.webdriver.chrome.service import Service
import os

def scrape_url(url):

    print(f"Running chrome driver for url: {url}")
    print(os.getcwd())
    driver_path = os.path.join(os.getcwd(), "driver", "chromedriver-win64", "chromedriver.exe")
    print(driver_path)

    if not os.path.exists(driver_path):
        print(f"Error: Driver executable not found at {driver_path}")
        return

    ### get all contents of page using chrome driver
    options = wd.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    service = Service(executable_path=driver_path)
    driver = wd.Chrome(service=service, options=options)

    try:
        driver.get(url)
        print("Page loaded sucessfully")
        content = driver.page_source
        driver.quit()
        return content

    finally:
        driver.quit()
        