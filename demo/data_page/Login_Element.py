from selenium.webdriver.common.by import By
class Login_Element():
    user = (By.XPATH, "//*[@id='username']")
    pwd = (By.XPATH, "//*[@id='password']")
    club=(By.XPATH,"//p[text()='线测环境总部']")
    button = (By.XPATH, '//*[@id="formLogin"]/div[2]/div/div/span/button')