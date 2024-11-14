import selenium.webdriver as wd
from selenium.webdriver.chrome.service import Service

def scrape_url(url):

    print(f"Running chrome driver for url: {url}")

    ### get all contents of page using chrome driver
    options = wd.ChromeOptions()
    service = Service(executable_path='./driver/chromedriver.exe')
    driver = wd.Chrome(service=service, options=options)

    try:
        driver.get(url)
        print("Page loaded sucessfully")
        content = driver.page_source
        driver.quit()
        return content

    except Exception as e:
        print(e)
        driver.quit()
        return