from tools.demo import tools
from time import sleep
from data_page.user_manager_Element import usermanager_Element


class user_manager(tools):
    url = tools.url + "/club/personManage/info-staff"
    ue = usermanager_Element()

    def user_manager_search(self, name, typename, number):
        # self.get_()
        self.send_(self.ue.name, name)
        self.send_(self.ue.typename, typename)
        self.send_(self.ue.number, number)
        self.click_(self.ue.button)

    def user_manager_reload(self):
        self.click_(self.ue.reload)

    def user_manager_resign(self):
        self.click_(self.ue.resign)
        sleep(1)

    def add_user(self):
        self.click_(self.ue.aduser)
        sleep(1)

    def edit_user(self):
        self.get_()
        self.click_(self.ue.eduser)

    def user_resign(self):
        self.get_()
        self.click_(self.ue.res)
        sleep(1)

    def click_close(self):
        self.click_(self.ue.close_)

    def click_ok(self):
        self.user_resign()
        self.click_(self.ue.ok_)
        sleep(1)

    def add_person(self, names):
        self.send_(self.ue.name_input, self.faker_())
        self.click_(self.ue.wichman)
        self.send_(self.ue.phone_num, self.number())
        self.send_(self.ue.other_name, names)
        self.click_(self.ue.witch)
        sleep(1)
        self.Enter_()
        sleep(1)
        self.esc_()
        self.click_(self.ue.input_witch)
        self.click_(self.ue.witch_member)
        sleep(1)
        self.Enter_()
        sleep(1)
        self.esc_()
        self.click_(self.ue.enter_button)
