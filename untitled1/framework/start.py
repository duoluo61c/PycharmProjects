import case
import inspect

li=[]
def get_case():
    for i in case.__all__:     #通过模块名称寻找类
        _class=getattr(case,i) #反射  获取
        #print(_class)
        for name,value in inspect.getmembers(_class):  #返回函数名  返回一个包含对象的所有成员的(name, value)列表。
            #print(name)
            if not name.startswith("_"):    #不是以_开头的
                li.append(name)       #将方法名依次加入列表  #['case1', 'case10', 'case11', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', 'case8', 'case9']
    return li

if __name__ == '__main__':
    for j in range(len(get_case())):        #返回class
        thisclass=getattr(case,"textcase")  #实例化class
        obj=thisclass()                     #返回方法
        testmtd=getattr(obj,get_case()[j])
        testmtd()                           #执行方法