N=10
sum=0
count=0
print("输入10个数值")
while count<N:
	a=float(input("输入："))
	sum=sum+a
	count=count+1
avg=sum/N
print("数值{},平均值{}".format(N,avg))
print("平均值取2位小数{:.2f}".format(avg))
