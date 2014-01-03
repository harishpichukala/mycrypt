import os
from cmd import Cmd
from shiftcipher import *	

class MyInterpreter(Cmd):
	
	""" My awesome Interpreter """

	prompt = "shift@harish "
	
	def cmdloop(self):
	
		print "Welcome to My Interpreter!"

		Cmd.cmdloop(self)
	

	def do_quit(self,line):
	
		"""usage: quit """
		print "the terminal is closing !!"
	
		return True
	
	def do_encrypt(self,line):
		"""Usage: encrypt filename key """
		s=line.split(' ')
		name=s[0]
		key=int(s[1])
		encrypt(name,key)
	def do_decrypt(self,line):
		"""Usage:decrypt filename key"""
		s=line.split(' ')
		name=s[0]
		key=int(s[1])
		decrypt(name,key)	
if __name__ == "__main__":
	MyInterpreter().cmdloop()
