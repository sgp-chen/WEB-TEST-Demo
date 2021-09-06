from tools.demo import tools
from time import sleep
from data_page.Login_Element import Login_Element


class login_page(tools):
    url = tools.url + "/user/login"
    le = Login_Element()


    def login(self, username, passwd):
        self.get_()
        self.send_(self.le.user, username)
        self.send_(self.le.pwd, passwd)
        self.click_(self.le.button)
        self.click_(self.le.club)
        sleep(1)
        self.refresh_()
# if __name__ == '__main__':
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     lp=login_page(driver)
#     user="13999999999"
#     pwd="123456a"
#     lp.login_(user,pwd)
