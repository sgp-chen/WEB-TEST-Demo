from selenium.webdriver.common.by import By
class Login_Element():
    user = (By.XPATH, "//*[@id='username']")
    pwd = (By.XPATH, "//*[@id='password']")
    button = (By.XPATH, '//*[@id="formLogin"]/div[2]/div/div/span/button')