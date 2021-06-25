import platform
from selenium import webdriver


# ChromeOptions类的封装
class Options:
    def conf_options(self):
        if platform.system() == "Windows":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('start-maximized')
            self.options.add_experimental_option('useAutomationExtension', False)
            self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
            self.prefs = {}
            self.prefs['credentials_enable_service'] = False
            self.prefs['profile.password_manager_enabled'] = False
            self.options.add_experimental_option('prefs', self.prefs)
        elif platform.system() == "Linux":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('start-maximized')
            # root运行且无图形界面
            self.options.add_argument('--no-sandbox')
            self.options.add_argument('--disable-dev-shm-usage')
            self.options.add_argument('--headless')
            self.options.add_argument('blink-settings=imagesEnabled=false')
            self.options.add_argument('--disable-gpu')
        return self.options