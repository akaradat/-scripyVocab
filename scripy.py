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
	

def print_line(x=None):
	if x is None:
		print "-"*40
	else:
		print "-"*x

def print_con():
	x=raw_input("press enter to continue.")

def loading():
	global done
	done = False
	t = threading.Thread(target=animate)
	t.start()

def animate():
	global done
	done=False
	for c in itertools.cycle(['.  ', '.. ', '...', '   ']):
		if done:
			break
		sys.stdout.write('\rLOADING PLEASE WAIT' + c)
		sys.stdout.flush()
		time.sleep(0.3)
		
def degree(a,b):
	x=a*1.0/b
	if(x>=0.8):
		return "Excellent!"
	elif(x>=0.6):
		return "Good"
	elif(x>=0.4):
		return "Fair"
	else:
		return "Try harder"

def random_word():
	global vocab
	global word_vocab
	word_vocab=[]
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
	global trans_vocab1
	global trans_vocab2
	tmp=['','']
	ran=[0,1,2,3,4]
	random.shuffle(ran)
	score=0
	
	for i in ran:
		if(lan[0]!=''):
			tmp[0]= '[%s] %s'%(lan[0],trans_vocab1[i])
		if(lan[1]!=''):
			tmp[1]= '[%s] %s'%(lan[1],trans_vocab2[i])
		cls()
		print "--------Dictaion--------"
		print "Did you remember this?\n"
		print "%s %s\n"%(tmp[0],tmp[1])
		j=0
		while(j<3):
			x=raw_input("In english is: ")
			if(x.lower()==word_vocab[i]):
				score+=1
				print "----- Correct! -----\n"
				print_con()
				break
			else:
				print "----- Try again! -----\n"
			j+=1
		if(j==3):
			print_line()
			print "%s %s in english is %s"%(tmp[0],tmp[1],word_vocab[i])
			print_line()
			print_con()

	cls()
	print "--------Dictaion--------"
	print_line(24)
	print "%7d/%d %s"%(score,5,degree(score,5))
	print_line(24)
	print_con()
	return score


def learn_vocab():
	global word_vocab
	global lan
	global trans_vocab1
	global trans_vocab2
	global done
	total = 0
	score = 0
	
	x='y'
	while(x=='yes' or x=='y'):
		cls()
		print "--------Learn station--------\n"
		print "How much that you can remember?(# Exit)\n"
		x=raw_input("press enter to start")
		if(x=='#'):
			break
		cls()
		print "--------Learn station--------\n"
		print "How much that you can remember?(# Exit)\n"
		loading()
		random_word()
		get_translate()
		done=True
		cls()
		print "--------Learn station--------\n"
		print "How much that you can remember?(# Exit)"
		print_line()
		tmp=['','','']
		for i in range(5):
			tmp[0]='[%s] %s'%('en',word_vocab[i])
			if(lan[0]!=''):
				tmp[1]= '[%s] %s'%(lan[0],trans_vocab1[i])
			if(lan[1]!=''):
				tmp[2]= '[%s] %s'%(lan[1],trans_vocab2[i])
			print "%-15s%-15s\t%s"%(tmp[0],tmp[1],tmp[2])
		print_line()
		x=raw_input("press enter to continue")
		if(x=='#'):
			break
		total+=5
		score+=dictation()
		cls()
		print "--------Learn station-------3-\n"
		print "total: %d \tyour score: %d \t%s\n"%(total,score,degree(score,total))
		while x!= 'n' and x!= 'y':
			x=raw_input("Do you want to play again? (y/n) : ").lower()
		
def word_shuffle():
	global word_vocab
	total = 0
	score = 0
	x='y'
	while(x=='yes' or x=='y'):
		random_word()
		cls()
		print "--------Word shuffle-------\n"
		print_con()
		for i in word_vocab:
			cls()
			print "--------Word shuffle-------\n"
			total+=1
			tmp = ' '.join(random.sample(i,len(i)))
			print tmp
			y=''
			while(y!=i):
				y=raw_input("Input: ")
				if(y==i):
					print "----- Correct! -----\n"
					score+=1
					print_con()
				if(y=='#'):
					break
				print "----- Try again! -----\n"
		cls()
		x=''
		print "--------Word shuffle-------\n"
		print "total: %d \tyour score: %d \t%s\n"%(total,score,degree(score,total))
		while x!= 'n' and x!= 'y':
			x=raw_input("Do you want to play again? (y/n) : ").lower()
	






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
dictation()

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
