import os
import re


class ChromeVersion:

    def __init__(self) -> None:
        pass
        

    def extract_version_registry(self, output):
        try:
            google_version = ''
            for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
                if letter != '\n':
                    google_version += letter
                else:
                    break
            return(google_version.strip())
        except TypeError:
            return

    def extract_version_folder(self):
        # Check if the Chrome folder exists in the x32 or x64 Program Files folders.
        for i in range(2):
            path = 'C:\\Program Files' + (' (x86)' if i else '') +'\\Google\\Chrome\\Application'
            if os.path.isdir(path):
                paths = [f.path for f in os.scandir(path) if f.is_dir()]
                for path in paths:
                    filename = os.path.basename(path)
                    pattern = '\d+\.\d+\.\d+\.\d+'
                    match = re.search(pattern, filename)
                    if match and match.group():
                        # Found a Chrome version.
                        return match.group(0)

        return None

    def get_chrome_version(self):

    
        version = None
        install_path = None

        try:
            # Try registry key.
            stream = os.popen('reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome"')
            output = stream.read()
            version = self.extract_version_registry(output)
        except Exception as ex:
            # Try folder path.
            print(ex)
            version = self.extract_version_folder()
            

        version = os.popen(f"{install_path} --version").read().strip('Google Chrome ').strip() if install_path else version

        return version
    