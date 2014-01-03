from cmd import Cmd
from substitute import *
class Subcipher(Cmd):
	"""my substitution cipher interpreter"""
	prompt="harish@srkr$"
	def cmdloop(self):
		print "welcome to  harish  interpreter"
		Cmd.cmdloop(self)
	def do_encrypt(self,line):
		"""usage:encrypt filename"""
		g=generate()
		encrypt(g,line)
	def do_decrypt(self,line):
		"""usage:decrypt filename"""
		decrypt("key.txt",line)
	def do_quit(self,line):
		"""usage:quit"""
		print "we are closing the terminal"
		return True	

	
if __name__ == "__main__":
	Subcipher().cmdloop()
