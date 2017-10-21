#-*-coding: utf-8 -*-
import os



ip1=''
lan1='th'
lan2='ja'

def cls():
	if(os.name=='nt'):
		os.system('cls')
	else :
		print("\033[H\033[J")

def setting():
	global lan1
	global lan2
	x=''
	while(x!='#'):
		cls()
		print "--------Setting Language-------"
		print "First language: ",lan1
		print "Second language: ",lan2
		print "press 1 or 2 to setting language. # to exit."
		x=raw_input("Select: ")

		if x=='1':
			lan1=raw_input("Input first language: ")
		elif x=='2':
			lan2=raw_input("Input second language: ")
		

while(ip1!='#'):
	cls()
	print "---------- Welcome to Scripy Vocab ----------"
	print "\t1.Learn vocabuary"
	print "\t2.Hangman Game"
	print "\t3.Word shuffle Game"
	print "\t4.Setting"
	print "\t# Exit"
	ip1=raw_input("Select: ")

	if (ip1=='1'):
		learn_vocab()
	elif (ip1=='2'):
		hangman()
	elif (ip1=='3'):
		word_shuffle()
	elif (ip1=='4'):
		setting()

print "Good bye!"


