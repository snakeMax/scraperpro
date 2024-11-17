import selenium.webdriver as wd
from selenium.webdriver.chrome.service import Service
import os
from bs4 import BeautifulSoup

irrelevant_tags = ["script", "style", "select"]

def extract_content(html):
    soup = BeautifulSoup(html, "html.parser")
    bodyc = soup.body

    if bodyc:
        return str(bodyc)
    return ""
    
def clean_body(body):
    soup = BeautifulSoup(body, "html.parser")

    for irrelevant in soup(irrelevant_tags):
        irrelevant.extract()

    cleaned = soup.get_text(separator="\n")
    cleaned = "\n".join(line.strip() for line in cleaned.splitlines() if line.strip())
    return cleaned


def split_dom(content, max_length=6000):
    return [content[i:i+max_length] for i in range(0, len(content), max_length)]


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
        