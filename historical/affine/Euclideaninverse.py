#algorithm for extended Euclidean algorithm
#ax=1(mod M)
def compute_inverse(a,m):
	i=1
	while i<=m:
		p=(a*i)%m
		if p==1:
			return i
			break
		i=i+1
 
