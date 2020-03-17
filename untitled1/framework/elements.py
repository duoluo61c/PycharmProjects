
username_input=["id","username"]     #查找登录输入框
password_input=["id","password"]     #查找密码输入框
ver_input=["id","verifycode"]        #查找验证码输入框
submit_button=["xpath","/html/body/div[4]/div/form/div[6]/button"] #查找登录按钮
logout_button=["xpath","/html/body/div[2]/div/div[2]/ul[2]/li[2]/a"] #查找注销按钮



#会员管理模块
vip_button=["xpath","/html/body/div[2]/div/div[2]/ul[1]/li[5]/a"] #查找会员管理按钮
customerphone_input=["id","customerphone"]  #获取手机号输入框
addcustomer_button=["xpath","/html/body/div[4]/div[1]/form[2]/div[2]/button[1]"] #查找会员管理中新增按钮按钮
searchCustomer_button=["xpath","/html/body/div[4]/div[1]/form[2]/div[2]/button[3]"] #会员管理中的查询按钮
childsex_select=["id","childsex"]   #会员管理中小孩性别下拉框
vip_name=["id","customername"]   #会员昵称
xianshi_table=["xpath","/html/body/div[4]/div[2]/table"]   #查询时的显示框
alter_button=["id","editBtn"]    #大修改按钮
chaxun_source=["xpath","/html/body/div[4]/div[2]/table/tbody/tr/td[2]"]  #显示信息的第一条的电话号码