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
    name_input=(By.XPATH,'//input[@class="ant-input"]')
    wichman=(By.XPATH,'//span[@class="ant-radio"]//input')
    phone_num=(By.XPATH,'//input[@placeholder="请输入手机号"]')
    other_name = (By.XPATH, '//input[@placeholder="最多可输入10个字"]')
    witch=(By.XPATH,'//div[text()="请选择"]/../..')
    witch_member=(By.XPATH,'//label[@title="系统角色"]/../following-sibling::div/descendant::div[5]')
    enter_button=(By.XPATH,'//span[text()="提 交"]/..')
    input_witch=(By.XPATH,'//label[5]//input')
