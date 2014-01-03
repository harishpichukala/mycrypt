def cal_inverse(k):
	t=k[0]
	k[0]=k[3]
	k[3]=t
	k[1]=-k[1]
	k[2]=-k[2]
	i=0
	m=26
	while i<=3:
		k[i]=k[i]%m
		i=i+1
	i=0
	return k

def cal_mul(x,t):
	y=[0,0]
	m1=26
	y[0]=((x[0]*t[0])+(x[1]*t[2]))
	m=y[0]
	y[1]=((x[0]*t[1])+(x[1]*t[3]))
	n=y[1]
	#if ((m==26)or(m==27)or(n==26)or(n==27)):
	#	y[0],y[1]=m,n
	#else:
	y[0]%=m1
	y[1]%=m1
	return y
	
def inverse_exists(k):
	if k[0]*k[3]-k[1]*k[2]==0:
		return 0
	else:
		return 1

