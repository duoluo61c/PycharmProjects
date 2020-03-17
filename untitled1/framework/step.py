from common import *
import data
import elements
from selenium import webdriver
import random

class setp1():
    def __init__(self):
        self.driver = Base()

    #def log(self):        #登录过程
        self.driver.GetElement(elements.username_input).send_keys(data.username)
        self.driver.GetElement(elements.password_input).send_keys(data.password)
        self.driver.GetElement(elements.ver_input).send_keys(data.ver)
        self.driver.GetElement(elements.submit_button).click()

    def huoqu_title(self):   #获取当前页面title
        title=self.driver.driver.title
        self.title=title
        return title

    def duanyan(self,case_name,shiji,qiwang):    #断言  传参 （用例名称 实际结果 期望）
        self.driver.duanyan(case_name,shiji,qiwang)

    def logout(self):               #点击注销按钮
        self.driver.GetElement(elements.logout_button).click()

    def input_customerphone(self,number):        #验证会员管理手机输入框输入框
        self.driver.GetElement(elements.vip_button).click()    #点击会员管理按钮
        self.driver.GetElement(elements.customerphone_input).send_keys(number)  #会员管理中手机号码输入框输入
        self.driver.GetElement(elements.addcustomer_button).click() #点击会员查询中新增按钮
        sql = "select customerphone from customer where customerphone='%s'" % (number)
        source = self.driver.mysql(sql)
        sql1 = "delete from customer where customerphone='%s'" % (number)
        self.driver.mysql(sql1)
        return len(source)

    def sex_select(self):  #验证会员管理模块小孩性别下拉框
        self.driver.GetElement(elements.vip_button).click()          #点击会员管理按钮
        self.driver.GetElement(elements.customerphone_input).send_keys(123)  # 会员管理中手机号码输入框输入
        self.driver.select(elements.childsex_select,data.select_sex) #传入数据，选择下拉框
        self.driver.GetElement(elements.addcustomer_button).click() #点击会员查询中新增按钮
        sql = "select childsex from customer where customerphone='%s'" % (123)
        source = self.driver.mysql(sql)
        sql1 = "delete from customer where customerphone='%s'" % (123)
        self.driver.mysql(sql1)
        return source[0][0]

    def input_vipname(self):     #验证会员管理模块会员昵称输入框
        self.driver.GetElement(elements.vip_button).click()          #点击会员管理按钮
        self.driver.GetElement(elements.customerphone_input).send_keys(123)  # 会员管理中手机号码输入框输入
        vipname_default=self.driver.GetElement(elements.vip_name).get_attribute("value")  #获取会员昵称的默认值
        self.driver.GetElement(elements.vip_name).clear()   #清空
        self.driver.GetElement(elements.vip_name).send_keys(data.vip_name[0])    #输入数据
        self.driver.GetElement(elements.addcustomer_button).click()  # 点击会员查询中新增按钮
        sql = "select customername from customer where customerphone='%s'" % (123)
        source = self.driver.mysql(sql)
        sql1 = "delete from customer where customerphone='%s'" % (123)
        self.driver.mysql(sql1)
        source=[vipname_default,source[0][0]]   #返回会员昵称的默认值和查询数据库结果
        return source

    def search_button(self):  #验证直接点击查询按钮
        self.driver.GetElement(elements.vip_button).click()          #点击会员管理按钮
        self.driver.GetElement(elements.searchCustomer_button).click()  #点击会员查询中查询按钮
        count_xianshi = self.driver.GetElement(elements.xianshi_table).find_elements_by_tag_name("tr")#获取显示的信息条数
        count_xianshi=len(count_xianshi)-1    #显示在页面的数据条数
        sql = "select count(*) from customer"
        count_shujuku=self.driver.mysql(sql)     #数据库的页面条数
        source=[count_xianshi,count_shujuku[0][0]]
        return source

    def alter_click(self):  #没修改时修改按钮验证
        self.driver.GetElement(elements.vip_button).click()          #点击会员管理按钮
        source=self.driver.driver.find_element(elements.alter_button[0],elements.alter_button[1]).is_enabled()
        if source==False:         #查看修改按钮是否可用
            return 0
        else:
            return 1
    def searchphone_button(self):   #根据手机号码查询信息
        sql="select customerphone from customer"
        source=self.driver.mysql(sql)
        num=random.randint(0,len(source)-1)  #生成随机数作为下标
        self.driver.GetElement(elements.vip_button).click()  # 点击会员管理按钮
        self.driver.GetElement(elements.customerphone_input).send_keys(source[num][0])#会员管理中手机号码输入框输入数据库已存在的任意手机号码
        self.driver.GetElement(elements.searchCustomer_button).click()  #点击查询按钮
        text=self.driver.GetElement(elements.chaxun_source).text
        if text==source[num][0]:
            return 0
        else:
            return 1


    def searchcustomer_click(self):  #点击会员查询中查询按钮
        self.driver.GetElement(elements.searchCustomer_button).click()

    def myasql_phone(self,num):      #查询手机号码
        sql="select customerphone from customer where customerphone='%s'"%(num)
        source=self.driver.mysql(sql)
        return source

    def clear_vip(self,phone):    #删除手机号码
        sql1="delete from customer where customerphone='%s'"%(phone)
        self.driver.mysql(sql1)



