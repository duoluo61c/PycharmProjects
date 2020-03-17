from selenium import webdriver
import pymysql,time,logging,os
from selenium.common.exceptions import *
class Common():
    #初始化，每次都打开网址
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.drizzle-hit.com/#/login")
        self.picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        self.save = r"D:\下载\UIimage"

    def get_element(self,element):
        try:
            e_type=element[0]
            e_value=element[1]
            e_res = self.driver.find_element(e_type,e_value)
        except NoSuchElementException:
            print("%s元素未找到"%(e_value))
            self.saveImage()
            self.driver.quit()
        except TimeoutException:
            print("%s元素查找超时"%(e_value))
            self.saveImage()
            self.driver.quit()
        else:
            if e_res.is_enabled()==False:
                print("%s元素不可用"%(e_value))
                self.saveImage()
                self.driver.quit()
            else:
                return e_res

    #SQL操作
    def sql_chang(self,databases='test',sql1=None):
        con = pymysql.connect("localhost","root","123456")
        cur = con.cursor()
        sql = "use %s"%(databases)
        cur.execute(sql)
        cur.execute(sql1)
        con.commit()
        con.close()
    def sql_select(self,databases='test',num=0, sql1=None):
        con = pymysql.connect("localhost",'root','123456')
        cur = con.cursor()
        sql = "use %s"%(databases)
        cur.execute(sql)
        cur.execute(sql1)
        if num == 0 :
            res =  cur.fetchall()
            print("查询全部数据成功")
        else:
            res =  cur.fetchmany(num)
            print("查询"+str(num)+"条数据成功")
        con.commit()
        con.close()
        return res

    # 日志
    def log_write(self):
        # logging.basicConfig(filename="%s"%(self.picture_time),filemode="w",level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')
        # handler=logging.FileHandler("log.txt")
        logger = logging.getLogger(__name__)
        logger.setLevel(level=logging.DEBUG)  # Log等级总开关
        handler = logging.FileHandler("log.txt")  # 创建一个handler，用于写入日志文件
        handler.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.info("this is a logger info message")
        logger.debug("this is a logger debug message")
        logger.warning("this is a logger warning message")
        logger.info("Finish")

    #截图
    def saveImage(self): #保存到D:\下载\UIimage 下
        if not os.path.exists(self.save):
            os.mkdir(self.save)
        self.driver.save_screenshot(self.save + self.picture_time + ".png")


# if __name__ == '__main__':
    # co = Common()
    # # sql = "insert into stu1 values('哈哈',9,20,'男')"
    # # co.sql_chang(databases='test',sql1=sql)
    # sql1 = "select * from stu1 where sid = 9"
    # res = co.sql_select(databases='test',num=2,sql1=sql1)
    # print(res)
