

__all__=["textcase"]   #声明可以被调用

from step import *
import elements
import data
import common


class textcase():
    def __init__(self):
        self.ob=setp1()
        self.ob.driver.log()     #日志

    def case1(self):   #使用正确的用户名密码登录
        source=self.ob.huoqu_title()
        self.ob.duanyan(data.case_text,data.qiwang,source)

    def case2(self):  #手机号码输入11位正整数
        source=self.ob.input_customerphone(data.number0[0])
        self.ob.duanyan(data.number0[2],data.number0[1],source)

    def case3(self):  #手机号码输入12位正整数
        source=self.ob.input_customerphone(data.number1[0])
        self.ob.duanyan(data.number1[2],data.number1[1],source)

    def case4(self):  #手机号码输入10位正整数
        source=self.ob.input_customerphone(data.number2[0])
        self.ob.duanyan(data.number2[2],data.number2[1],source)

    def case5(self):  #手机号码输入11位字母
        source=self.ob.input_customerphone(data.number3[0])
        self.ob.duanyan(data.number3[2],data.number3[1],source)

    def case6(self):  #手机号码输入11位特殊字符
        source=self.ob.input_customerphone(data.number4[0])
        self.ob.duanyan(data.number4[2],data.number4[1],source)

    def case7(self):  #手机号码输入为空
        source=self.ob.input_customerphone(data.number5[0])
        self.ob.duanyan(data.number5[2],data.number5[1],source)

    def case8(self):  #手机号码输入已存在手机号码
        source=self.ob.input_customerphone(data.number6[0])
        self.ob.duanyan(data.number6[2],data.number6[1],source)

    def case9(self):  #选择小孩性别为女
        source=self.ob.sex_select()
        self.ob.duanyan(data.select_sex[3],data.select_sex[2],source)

    def case10(self):   # 会员管理，会员名称默认值验证
        source=self.ob.input_vipname()
        self.ob.duanyan(data.vip_name_defaule[1],data.vip_name_defaule[0],source[0])

    def case11(self):   #会员管理，会员名称输入“西门吹雪”
        source = self.ob.input_vipname()
        self.ob.duanyan(data.vip_name[1], data.vip_name[0], source[1])

    def case12(self):   #验证不填数据单机查询按钮
        source=self.ob.search_button()
        self.ob.duanyan(data.serach_button,source[1],source[0])

    def case13(self):  #验证无修改时修改按钮是否处于置灰状态
        source=self.ob.alter_click()
        self.ob.duanyan(data.alter_defaule[1],data.alter_defaule[0],source)

    def case14(self):   #验证根据手机号码查询信息
        source=self.ob.searchphone_button()
        self.ob.duanyan(data.search_input_phone[1],data.search_input_phone[0],source)


if __name__ == '__main__':
    aa=textcase()
    aa.case13()


