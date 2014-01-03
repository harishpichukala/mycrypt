import sys,os
from shiftcipher import decrypt
f=open('display.sh','w')
f.write("cat ")
f.write("temps.txt")
f.close()
f=open('initial.sh','w')
f.write('cat<')
f.write(sys.argv[1])
f.write('>temps.txt')
f.close()
k=0
while k<=27:
	os.system('sh initial.sh')
	decrypt("temps.txt",k)
	print "decryption when key=",k
	os.system('sh display.sh')
	print \
	"""---------------------------------------
	-----------------------------------------
	---------------------------------------"""
	os.remove('temps.txt')
	k=k+1
