from tools.demo import tools
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from page.Login_page import login_page


class user_manager(tools):
    url = tools.url + "/club/personManage/info-staff"
    name = (By.XPATH,
            '//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[1]/form/div[2]/div[1]/div/div[2]/div/span/input')
    typename = (By.XPATH,
                '//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[1]/form/div[2]/div[2]/div/div[2]/div/span/input')
    number = (By.XPATH,
              '//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[1]/form/div[2]/div[3]/div/div[2]/div/span/input')
    button = (
    By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[1]/form/div[1]/div/button[1]')
    reload = (
    By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[2]/div/div/div/div[1]/form/div[1]/div/button[2]')
    resign = (By.XPATH, "//div[text()='已离职']")
    aduser = (By.XPATH, "// button[@class ='ant-btn ant-btn-primary ant-btn-sm']")
    eduser = (By.XPATH, "//a[text()='编辑'][1]")
    res = (By.XPATH, "//a[text()='离职'][1]")
    ok_ = (By.XPATH, '//span[text()="确 认"] /..')
    close_ = (By.XPATH, '//span[text()="取 消"] /..')

    def user_manager_search(self, name, typename, number):
        # self.get_()
        self.send_(self.name, name)
        self.send_(self.typename, typename)
        self.send_(self.number, number)
        self.click_(self.button)

    def user_manager_reload(self):
        self.click_(self.reload)

    def user_manager_resign(self):
        self.click_(self.resign)
        sleep(1)

    def add_user(self):
        self.click_(self.aduser)
        sleep(1)

    def edit_user(self):
        self.get_()
        self.click_(self.eduser)

    def user_resign(self):
        self.get_()
        self.click_(self.res)
        sleep(1)

    def click_close(self):
        self.click_(self.close_)

    def click_ok(self):
        self.user_resign()
        self.click_(self.ok_)
        sleep(1)
