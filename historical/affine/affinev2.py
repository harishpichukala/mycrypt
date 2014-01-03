from affine import *
from cmd import Cmd
class affine(Cmd):
	"""my affine  cipher operations"""
	prompt="harish@affine"
	def cmdloop(self):
		print "welcome to harish interpreter"
		Cmd.cmdloop(self)
	def do_encrypt(self,line):
		"""Usage:encrypt [filename]"""
		l=line.split(' ')
		key=raw_input("enter key")
		k=key.split(' ')
		
		encrypt(int(k[0]),int(k[1]),l[0])
	def do_decrypt(self,line):
		"""Usage:decrypt [filename"""
		l=line.split(' ')
		key=raw_input("enter key")
                k=key.split(' ')
           	decrypt(int(k[0]),int(k[1]),l[0])
	def do_quit(self,line):
		"""closes the terminal"""
		print "we are closing the terminal"
		return True
if __name__ == "__main__":
	affine().cmdloop()
