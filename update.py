import os
import requests
import zipfile

def get_chrome_version():
    import winreg
    reg_key = r"SOFTWARE\Google\Chrome\BLBeacon"
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key) as key:
            version, _ = winreg.QueryValueEx(key, "version")
            return version
    except OSError:
        return None

def download_chrome_driver(version):
    url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip"
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open("chromedriver.zip", "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
            zip_ref.extractall("driver")
        os.remove("chromedriver.zip")
    else:
        print("Failed to download Chrome driver")

def main():
    chrome_version = get_chrome_version()
    if chrome_version:
        driver_path = os.path.join("driver", "chromedriver.exe")
        if not os.path.exists(driver_path):
            download_chrome_driver(chrome_version)
        else:
            print("Chrome driver already exists")
    else:
        print("Failed to detect Chrome version")

if __name__ == "__main__":
    main()