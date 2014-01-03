from hill import *
from cmd import Cmd
class hill(Cmd):
	prompt="harish@hill"
	def cmdloop(self):
		print "welcome to harish interpreter"
		Cmd.cmdloop(self)
	def do_encrypt(self,line):
		line=line.split(' ')
		key=raw_input("enter key")
		key=list(key)
		l=len(key)
		i=0
		keys=read_keys()
		i=0
		while i<l:
			key[i]=keys.index(key[i])
			i+=1
		encrypt(key,line[0])
		
	def do_decrypt(self,line):
		line=line.split(' ')
		key=raw_input("enter key")
		key=list(key)
		l=len(key)
		i=0
		keys=read_keys()
		i=0
		while i<l:
			key[i]=keys.index(key[i])
			i+=1
		decrypt(key,line[0])
	def do_quit(self,line):
		print "it is terminating"
		return True

if __name__=="__main__":
	hill().cmdloop()

