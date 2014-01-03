import os
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

def read_data(file):
	f1=open(file,'r')
	string=f1.read()
	f1.close()
	return string
def read_keys():
	keys="abcdefghijklmnopqrstuvwxyz \n"
	return list(keys)
