import pymysql

con = pymysql.connect("localhost","root","123456")
cur = con.cursor()  #建立游标
sql1 = "use test"
sql2 = "select * from stu order by RAND() limit 5 "
cur.execute(sql1)
cur.execute(sql2)
con.commit()
con.close()
