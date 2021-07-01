F=float(input("请输入华氏度："))
if F<32:
	print("请输入大于32的数值")
else:
	C=float((F-32)/1.8)
	print("输入华氏度{}，转换成摄氏度{}".format(F,C))
	print("取2位小数摄氏度{:2f}".format(C))
