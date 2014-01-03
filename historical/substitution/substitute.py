from randkey import randomkey
import os
def encrypt(key,msg):
		write_key(key)
		keys="abcdefghijklmnopqrstuvwxyz \n"
		keys=list(keys)
		r=list(key)
		e=[]
		m=open(msg,'r')
		s=m.read()
		m.close()
		k=len(s)
		i=0
		while i<k:
			if s[i]=='$':
				print("you are performing encryption on the already encrypted file")
				return	
			e.append(r[keys.index(s[i])])
			i=i+1	
		data=''.join(e)
		fileoperation(msg,data,1)

def fileoperation(f,d,e):
		f1=open('temp.txt','w')
		if e==1:	
			f1.write('$')
		f1.write(d)
		f1.close()
		os.remove(f)
		os.rename('temp.txt',f)
		if e==1:
			print "you have successfully encrypted the file"
		elif e==0:
			print "you have successfully decrypted the file" 
def decrypt(key,cipher):
		f=open(key,'r')
		r=f.read()
		f.close()
		keys="abcdefghijklmnopqrstuvwxyz \n"
		keys=list(keys)
		r=list(r)
		#print(r)
		f2=open(cipher,'r')
		c=f2.read()
		#print(c)
		c=c[1:]
		#print(c)
		f2.close()
		k=len(c)
		i=0
		d=[]
		while i<k:
			d.append(keys[r.index(c[i])])
			i=i+1
		data=''.join(d)
		fileoperation(cipher,data,0)

def generate():
		k=randomkey()
		return k
def write_key(k2):
		f=open("key.txt",'w')
		f.write(k2)
		f.close()
