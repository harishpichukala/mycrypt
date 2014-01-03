import random,math
def randomkey():
	keys="abcdefghijklmnopqrstuvwxyz \n"
	l=list(keys)
	range=28
	i=0
	k=[]
	while i<range:
		index=math.floor(random.random()*28)
		k.append(l[int(index)])
		i=i+1
	counta=[]
	for l1 in l:
		counta.append(k.count(l1))

	i=0
	j=0
	while j<28:
		if counta[j]==0:
			while i<28:
				if counta[i]>1:
					m=k.index(l[i])
					k[m]=l[j]
					counta[i]=counta[i]-1		
					counta[j]=counta[j]+1
					break
				i=i+1
		j=j+1
	cipher=''.join(k)
	return cipher


