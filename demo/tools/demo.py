from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class tools():
    url = "http://t-saas.lianduoduo.com/websaas/#"

    def __init__(self, driver):
        self.driver = driver

    def find_(self, *loc):
        return self.driver.find_element(*loc)

    def click_(self, loc):
        self.find_(*loc).click()

    def send_(self, loc, text):
        self.find_(*loc).send_keys(text)

    def get_(self):
        self.driver.get(self.url)

    def wait_(self):
        self.driver.implicitly_wait(10)

    def refresh_(self):
        self.driver.refresh()

    def Space_(self):
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()

    def Enter_(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def Back_Space_(self):
        ActionChains(self.driver).send_keys(Keys.BACK_SPACE)

    def double_mouse(self):
        ActionChains(self.driver).double_click().perform()

    def down_(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


class Chorme_option():
    def option(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('start-maximized')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        #root运行且无图形界面
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--headless')
        self.options.add_argument('blink-settings=imagesEnabled=false')
        self.options.add_argument('--disable-gpu')
        self.prefs = {}
        self.prefs['credentials_enable_service'] = False
        self.prefs['profile.password_manager_enabled'] = False
        self.options.add_experimental_option('prefs', self.prefs)
        return self.options
