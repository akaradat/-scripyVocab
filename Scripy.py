#-*-coding: utf-8 -*-
import os,random,json,requests,time,threading,itertools,sys

vocab=open('vocabulary.txt').read().split()
word_vocab=[]
trans_vocab1=[]
trans_vocab2=[]
done=False
lan=['th','fr']

def cls():
	if(os.name=='nt'):
		os.system('cls')
	else :
		os.system('clear')
		#print("\033[H\033[J")

def animate():
	global done
	for c in itertools.cycle(['|', '/', '-', '\\']):
		if done:
			break
		cls()
		print('\rloading ' + c)
		time.sleep(0.1)
		
		

def random_word():
	global vocab
	global word_vocab
	while len(word_vocab)<10:
		tmp=random.choice(vocab).lower()
		if tmp not in word_vocab:
			word_vocab.append(tmp)

def get_translate():
	global trans_vocab1
	global trans_vocab2
	global lan
	trans_vocab1=[]
	trans_vocab2=[]
	for i in range(5):
		url1='https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=%s&dt=t&q=%s'%(lan[0],word_vocab[i])
		url2='https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=%s&dt=t&q=%s'%(lan[1],word_vocab[i])
		trans_vocab1.append(json.loads(requests.get(url1).text)[0][0][0].lower())
		trans_vocab2.append(json.loads(requests.get(url2).text)[0][0][0].lower())

def dictation():
	global word_vocab

def loading():
	t = threading.Thread(target=animate)
	t.start()

def learn_vocab():
	global word_vocab
	global lan
	global trans_vocab1
	global trans_vocab2
	global done
	#cls()
	loading()
	#print "LOADING PLEASE WAIT..."
	random_word()
	get_translate()
	done=True
	x=''
	while(x!='#'):
		cls()
		print "--------Learn station--------\n"
		print "How much that you can remember?(# Exit)\n"
		tmp=['','','']
		for i in range(5):
			tmp[0]='[%s] %s'%('en',word_vocab[i])
			if(lan[0]!=''):
				tmp[1]= '[%s] %s'%(lan[0],trans_vocab1[i])
			if(lan[1]!=''):
				tmp[2]= '[%s] %s'%(lan[1],trans_vocab2[i])
			print "%-15s%-15s\t%s"%(tmp[0],tmp[1],tmp[2])
			#print "\n"
		x=raw_input("press enter to continue")


def setting():
	global lan
	x=''
	while(x!='#'):
		cls()
		print "--------Setting Language-------"
		print "First language: ",lan[0]
		print "Second language: ",lan[1]
		print "press 1 or 2 to setting language. # to exit."
		x=raw_input("Select: ")

		if x=='1':
			lan[0]=raw_input("Input first language: ")
		elif x=='2':
			lan[1]=raw_input("Input second language: ")
		
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

'''
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
	'''