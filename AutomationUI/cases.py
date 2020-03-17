from AutomationUI.step import *
from AutomationUI.common import *
import unittest

class Cases(Step):
    #@classmethod
    def __init__(self):
        self.st = Step()
        self.st.log_write()  #日志录入
    def test1(self):  #正确登录
        res = self.st.login(username,password,v_code,home_page_text)
        self.st.assert_res("正确登录",resp_home_page,res)
    def test2(self):  #错误用户名登录
        res = self.st.login(username_err,password,v_code,username_err_text,1)
        self.st.assert_res("错误用户名登录",resp_username_err,res)
    def test3(self):  #用户名长度最少为6位
        res = self.st.login(username_err_5, password, v_code, username_err_text_5)
        self.st.assert_res("用户名长度最少为6位", resp_username_err_5, res)
    def test4(self):  #错误密码登录
        res = self.st.login(username, password_err, v_code, password_err_text,1)
        self.st.assert_res("错误密码登录", resp_password_err, res)
    def test5(self):  #密码少于6位登录
        res = self.st.login(username, password_err_5, v_code, password_err_text_5)
        self.st.assert_res("密码少于6位登录", resp_password_err_5, res)

if __name__ == '__main__':
    #unittest.main()
    ca = Cases()
    ca.test1()
    # ca.test2()
    # ca.test3()
    # ca.test4()
    # ca.test5()