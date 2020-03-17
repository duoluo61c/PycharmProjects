def Mothod(a):
    sum = 0
    for i in range(0,a+1):
        sum = sum + i
    return sum
if __name__ == '__main__':
    res = Mothod(100)
    print(res)