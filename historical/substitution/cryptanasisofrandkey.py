from factorial import factorial
from randkey import randomkey
n=randomkey()
randslist=[]
i=factorial(26)
f=open('list.txt','w')
f.write("************")
f.write("$")
f.write(n)
f.write("$***********\n the keys are\n")
while i>0:
	j=randomkey()
	randslist.append(j)
	print(i)
	f.write(j)
	f.write('\n')
	if n in randslist:
		break
	
	i=i-1
f.close()
if n in randskey:
	m=randskey.count(n)
	print(m)
input(' ')
input(' ')