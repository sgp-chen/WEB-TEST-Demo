from selenium.webdriver.common.by import By
class usermanager_Element():
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