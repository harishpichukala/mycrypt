from vingenere import *
from cmd import Cmd
class vingenere(Cmd):
	"""my vingenere cipher operations"""
	prompt="harish@vingenere"
	def cmdloop(self):
		print "welcome to harish interpreter"
		Cmd.cmdloop(self)
	def do_encrypt(self,line):
		"""Usage:encrypt [filename]"""
		l=line.split(' ')
		key=raw_input("enter key")
		k=key.split(' ')
		n=len(k)
		key=[]
		i=0
		while i<n:
			key.append(k[i])
			i=i+1
		encrypt(key,l[0])
	def do_decrypt(self,line):
		"""Usage:decrypt [filename"""
		l=line.split(' ')
		key=raw_input("enter key")
                k=key.split(' ')
                n=len(k)
                key=[]
                i=0
                while i<n:
                        key.append(k[i])
                        i=i+1
		decrypt(key,l[0])
	def do_quit(self,line):
		"""closes the terminal"""
		print "we are closing the terminal"
		return True
if __name__ == "__main__":
	vingenere().cmdloop()
