n=int(input())
sum=0
temp=n
while temp>0:
	a=temp%10
	sum=sum+a**3
	temp//=10
if n==sum:
	print("yes")
else:
	print("no")
 