import pymysql

def SqlChange(ip="localhost",username="root",password="123456",databases="test",sql1=None):
    con = pymysql.connect(ip,username,password)
    cur = con.cursor()
    sql = "use %s"%(databases)
    cur.execute(sql)
    res = cur.execute(sql1)
    con.commit()
    if res==0:
        print("操作失败")
    else:
        print("操作成功")
    con.close()

def SqlSelect(ip="localhost",username="root",password="123456",databases="test",num = 0,sql1=None):
    con = pymysql.connect(ip,username,password)
    cur = con.cursor()
    sql = "use %s"%(databases)
    cur.execute(sql)
    cur.execute(sql1)
    if num==0:
        res = cur.fetchall()
        print("查询全部内容成功")
    else:
        res = cur.fetchmany(num)
        print("批量"+str(num)+"条内容成功")
    con.commit()
    con.close()
    return res  #将查询结果返回给调用者

if __name__ == '__main__':
    # sql = "update stu set S_ID=1 where S_ID=3"
    # SqlChange(sql1=sql)
    sql1 = "select * from stu where S_ID=1"
    res = SqlSelect(num=2,sql1=sql1)
    print(res)

