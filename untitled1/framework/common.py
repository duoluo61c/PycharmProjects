import pymysql,time,os,logging,os.path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium import webdriver
from selenium.webdriver.support.select import Select



class Base():
    #打开浏览器，输入网址
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:8080/WoniuSales-20171128-V1.3-bin/")
        self.dire="C:\\Users\\Administrator\\Desktop\\picture\\"
        self.picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    #数据库操作
    def mysql(self,sql,num=0,database="milor"):
        con = pymysql.connect("localhost", "root", "123456")
        cur = con.cursor()
        sql0 = "use " + database
        cur.execute(sql0)
        cur.execute(sql)
        if num == 0:
            source = cur.fetchall()
        else:
            source = cur.fetchmany(num)
        con.commit()
        con.close()
        return source  # 将查询的结果放回给调用者

    #截图   保存到桌面C:\\Users\\Administrator\\Desktop\\picture  下
    def SaveImage(self):
        if not os.path.exists(self.dire):
            os.mkdir(self.dire)
        self.driver.save_screenshot(self.dire+self.picture_time+".png")

    #元素查找器
    def GetElement(self,ele0):
        driver=self.driver
        try:
            ele_type=ele0[0]
            value=ele0[1]
            ele=driver.find_element(ele_type,value)
        except NoSuchElementException:
            print("%s元素没有找到"%(value))
            self.SaveImage()
            self.driver.quit
        except TimeoutException:
            print("%s元素查找超时" % (value))
            self.SaveImage()
            self.driver.quit
        else:
            states=ele.is_enabled()
            if states==False:
                print("%s元素不可用" % (value))
                self.SaveImage()
                self.driver.quit
            else:
                return ele
    #断言对比
    def duanyan(self,c,a,b):
        if a==b:
            print("%s 用例通过，期望为:%s,实际结果为:%s"%(c,a,b))
            self.driver.quit()
        else:
            self.SaveImage()
            self.driver.quit()
            print("%s 用例不通过，期望为:%s,实际结果为:%s"%(c,a,b))

    #下拉框选择器
    def select(self,ele1,select_name):
        ele_type=ele1[0]
        ele_value=ele1[1]
        element=self.driver.find_element(ele_type,ele_value)
        select_type=select_name[0]
        select_value=select_name[1]
        if select_type=="index":
            Select(element).select_by_index(select_value)
        elif select_type=="value":
            Select(element).select_by_value(select_value)
        elif select_type=="name":
            Select(element).deselect_by_visible_text(select_value)
        else:
            print("无‘%s’下拉框选择类型"%(select_value))

    def log(self):
        # logging.basicConfig(filename="%s"%(self.picture_time),filemode="w",level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')
        # handler=logging.FileHandler("log.txt")
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.DEBUG)  # Log等级总开关
        handler = logging.FileHandler("log.txt") #创建一个handler，用于写入日志文件
        handler.setLevel(logging.DEBUG) # 输出到file的log等级的开关
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        logger.info("this is a logger info message")
        logger.debug("this is a logger debug message")
        logger.warning("this is a logger warning message")
        logger.info("Finish")








