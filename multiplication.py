print("-" *50)
i=1
while i<11:
	number=1
	while number<10:
		s=i*number
		print("{:3d}*{}={}".format(i,number,s),end=" ")
		number=number+1
	print()
	i=i+1
print("-" *50)
