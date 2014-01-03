from errors import *
from fileoperation import *
from Euclideaninverse import *
def encrypt(a,b,msgfile):
	s=read_data(msgfile)
	keys=read_keys()
	#print keys
	m=26
	j=0
	e=[]
	k2=len(s)
	if s[0]=='$':
		encrypt_error()
		return
	try:
		while j<k2:
			k=((a*keys.index(s[j]))+b)%m
			e.append(keys[k])
			j=j+1
		data=''.join(e)
		fileoperation(msgfile,data,1)
	except IndexError:
		print("error occured while performing operation")
def decrypt(a,b,msgfile):
	s=read_data(msgfile)
	bit=s[0]
	if bit!='$': 
		decrypt_error()
		return
	s=s[1:]
	k2=len(s)
	keys=read_keys()
	m=26
	j=0
	p=[]
	inv=compute_inverse(a,m)
	while j<k2:
		index=(inv*(keys.index(s[j])-b))%m
		p.append(keys[index])
		j=j+1
	data=''.join(p)
	fileoperation(msgfile,data,0)	

