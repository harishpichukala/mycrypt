from cmd import Cmd
from substitute import *
import sys
try:
	if sys.argv[1]=="encrypt":
		g=generate()
		encrypt(g,sys.argv[2])
	elif sys.argv[1]=="decrypt":	
		decrypt("key.txt",sys.argv[2])
except IndexError:
	print \
	"""USAGE:programname [encrypt/decrypt] [filename]"""
	
