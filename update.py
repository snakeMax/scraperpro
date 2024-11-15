import os
import requests
import zipfile
from chromeV import ChromeVersion

### Program will get chrome version, then download the appropriate chrome driver
### Delete the chrome driver in the driver folder if its not up to date

def download_chrome_driver(version):
    url = f"https://storage.googleapis.com/chrome-for-testing-public/{version}/win64/chromedriver-win64.zip"
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        print("Downloading Chrome driver...")
        with open("chromedriver-win64.zip", "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

        driver_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "driver")
        with zipfile.ZipFile("chromedriver-win64.zip", "r") as zip_ref:
            zip_ref.extractall(driver_folder)
        print("Chrome driver downloaded successfully")
        os.remove("chromedriver-win64.zip")
    else:
        print("Failed to download Chrome driver")

def main():
    chromeversion = ChromeVersion()
    chromeversion.get_chrome_version()
    chrome_version = chromeversion.get_chrome_version()
    if chrome_version:
        print(f"Chrome version: {chrome_version}")
        driver_path = os.path.join("chromedriver-win64", "chromedriver.exe")
        if not os.path.exists(driver_path):
            download_chrome_driver(chrome_version)
        else:
            print("Chrome driver already exists")
    else:
        print("Failed to detect Chrome version")

if __name__ == "__main__":
    main()