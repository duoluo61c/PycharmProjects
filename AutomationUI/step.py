from AutomationUI.common import *
from AutomationUI.elements import *
from AutomationUI.data import *
class Step(Common):
    def __init__(self):
        self.co = Common()
    #断言
    def assert_res(self,case_number,expect,res):
        if expect == res:
            print("%s 用例通过 期望结果为：%s  实际结果为：%s"%(case_number,expect,res))
        else:
            print("%s 用例不通过 期望结果为：%s  实际结果为：%s"%(case_number,expect,res))

    def login(self,username1,password1,v_code1,resp_text,num=0): #num=0意思下方的条件判断=1时执行弹框的返回，0就正常的text返回
        self.co.get_element(username_input).send_keys(username1)
        self.co.get_element(password_input).send_keys(password1)
        self.co.get_element(v_code_input).send_keys(v_code1)
        self.co.get_element(yes_button).click()
        if num == 1:
            res_text1 = self.co.get_element(resp_text).get_attribute('textContent')  #弹框式的文字返回结果
            self.co.driver.quit()
            return res_text1
        else:
            res_text = self.co.get_element(resp_text).text  # 返回实际结果
            self.co.driver.quit()
            return res_text

# if __name__ == '__main__':
#     st = Step()
#     st.login()
