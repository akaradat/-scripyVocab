#-*-coding: utf-8 -*-
import os,random

vocab=open('vocabulary.txt').read().split()
word_vocab=[]
lan1='th'
lan2='ja'

def cls():
	if(os.name=='nt'):
		os.system('cls')
	else :
		print("\033[H\033[J")

def random_word():
	global vocab
	global word_vocab
	while len(word_vocab)<10:
		tmp=random.choice(vocab)
		if tmp not in word_vocab:
			word_vocab.append(tmp)


def learn_vocab():
	global word_vocab
	print "--------Learn station--------\n"
	print "How much that you can remember?(# Exit)"
	for i in range(5):
		print "[en] ",word_vocab[i]



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
		
def home():
	x=''
	while(x!='#'):
		cls()
		print "---------- Welcome to Scripy Vocab ----------"
		print "\t1.Learn vocabuary"
		print "\t2.Hangman Game"
		print "\t3.Word shuffle Game"
		print "\t4.Setting"
		print "\t# Exit"
		x=raw_input("Select: ")

		if (x=='1'):
			learn_vocab()
		elif (x=='2'):
			hangman()
		elif (x=='3'):
			word_shuffle()
		elif (x=='4'):
			setting()

	print "Good bye!"		

home()