try:
    m=int(input("整数1:"))
    n=int(input("整数2:"))
    valus=m/n
    print("计算结果：{}".format(valus))
except ZeroDivisionError:
    print("被除数不能为0")
except ValueError:
    print("输入数字符")
else:
    print("这是一个正确的结果")
finally:
    print("正确错误都执行")


# try:
#     print("正常执行")
# except:
#     print("异常执行")
# else:
#     print("非异常执行")
# finally:
#     print("正常异常都执行")
