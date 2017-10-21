#-*-coding: utf-8 -*-
import os,random,json,requests

vocab=open('vocabulary.txt').read().split()
word_vocab=[]
trans_vocab1=[]
trans_vocab2=[]

lan1='th'
lan2='fr'

def cls():
	if(os.name=='nt'):
		os.system('cls')
	else :
		os.system('clear')
		#print("\033[H\033[J")

def random_word():
	global vocab
	global word_vocab
	while len(word_vocab)<10:
		tmp=random.choice(vocab)
		if tmp not in word_vocab:
			word_vocab.append(tmp)

def get_translate():
	global trans_vocab1
	global trans_vocab2
	for i in range(5):
		url1='https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=%s&dt=t&q=%s'%(lan1,word_vocab[i])
		url2='https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=%s&dt=t&q=%s'%(lan2,word_vocab[i])

		trans_vocab1.append(json.loads(requests.get(url1).text)[0][0][0])
		trans_vocab2.append(json.loads(requests.get(url2).text)[0][0][0])



#def dictation():


def learn_vocab():
	global word_vocab
	random_word()
	x=''
	while(x!='#'):
		print "--------Learn station--------\n"
		print "How much that you can remember?(# Exit)"
		for i in range(5):
			print "[en] ",word_vocab[i]
		x=raw_input("press enter to continue")


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

#home()
random_word()
get_translate()
for i in word_vocab:
	print i
print "\n"
for i in trans_vocab1:
	print i
print "\n"
for i in trans_vocab2:
	print i