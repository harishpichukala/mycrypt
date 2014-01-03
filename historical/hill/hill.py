from inverse import *
from fileoperation import *
from errors import *
def encrypt(key,readmsg):
	y=[]
	keys=read_keys()
	msg=read_data(readmsg)	
	k=len(msg)
	i=0
	if msg[0] is '$':
		encrypt_error()
		return
	if k%2 is not 0:
		msg+=(' ')
	while i<k:
		x=list(msg[0:2])
		#print x
		x[0]=keys.index(x[0])
		x[1]=keys.index(x[1])
		#print x
		y+=cal_mul(x,key)
		if inverse_exists(key)==0:
				unpossible()
				return
		msg=msg[2:]
		i=i+2
	#print y
	j=0
	l=[]
	
	while j<len(y):
		l+=keys[int(y[j])]
		j+=1
	#print l
	data=''.join(l)
	fileoperation(readmsg,data,1)
	
		
#k=[11,8,3,7]
#encrypt(k,"hello.txt")

def decrypt(key,msgfile):
	msg=read_data(msgfile)
	keys=read_keys()
	if msg[0] is '$':
		msg=list(msg[1:])
		#print msg
		k1=len(msg)
		i=0
		z=[]
		t=cal_inverse(key)
		while i<k1:
			y=list(msg[0:2])
			y[0]=keys.index(y[0])
			y[1]=keys.index(y[1])
			z+=cal_mul(y,t)
			msg=msg[2:]
			i+=2
		j=0
		l=[]
		while j<len(z):
			l+=keys[int(z[j])]
			j+=1
		l=''.join(l)
		fileoperation(msgfile,l,0)
	else:
		decrypt_error()
		return
#decrypt(k,"hello.txt")
