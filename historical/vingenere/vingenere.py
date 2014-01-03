from errors import *
from  fileoperation import *
def encrypt(key,msg):
	message=read_data(msg)
	message=list(message)
	keys=read_keys()
	n=len(key)
	if message[0]=='$':
		encrypt_error()
		return
	m2=len(message)
	i=0
	e=[]
	m=28
	j=0
	while i<m2:
		e.append(keys[(keys.index(message[i])+int(key[j]))%m])
		j=j+1
		i=i+1
		if j==n:
			j=0
	data=''.join(e)
	fileoperation(msg,data,1)

def decrypt(key,msg):
	message=list(read_data(msg))
	keys=read_keys()
	n=len(key)
        if message[0]!='$':
                decrypt_error()
                return
        
	m2=len(message)
        i=1
        d=[]
        m=28
        j=0
        while i<m2:
                d.append(keys[(keys.index(message[i])-int(key[j]))%m])
                j=j+1
                i=i+1
		if j==n:
			j=0
	data=''.join(d)
	fileoperation(msg,data,0)	
