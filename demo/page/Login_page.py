from tools.demo import tools
from selenium.webdriver.common.by import By
from time import sleep
class login_page(tools):
    url = tools.url+"/user/login"
    user = (By.XPATH, "//*[@id='username']")
    pwd = (By.XPATH, "//*[@id='password']")
    button=(By.XPATH,'//*[@id="formLogin"]/div[2]/div/div/span/button')
    def login_(self,username,passwd):
        self.get_()
        self.send_(self.user,username)
        self.send_(self.pwd,passwd)
        self.click_(self.button)
        sleep(2)
        self.refresh_()
# if __name__ == '__main__':
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     lp=login_page(driver)
#     user="13999999999"
#     pwd="123456a"
#     lp.login_(user,pwd)



