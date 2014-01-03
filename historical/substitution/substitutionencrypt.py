from cmd import Cmd
import os
from  substitute import  *
class Subcipher(Cmd):
	"""susbtitution cipher implementation"""
	prompt="harish@srkr"
	def cmdloop(self):
		Cmd.cmdloop(self)
	def do_encrypt(self,line):
		encrypt(generate(),line)
		input('')
	def do_decrypt(self,line):
		"""usage: decrypt keyfile cipherfile"""
		l=line.split(' ')
		s.decryptmsg(l[0],l[1])
		input(' ')
	def do_quit(self):
		print("terminaring")
if __name__ == "__main__" :
	Subcipher().cmdloop()
input(' ')
