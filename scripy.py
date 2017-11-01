#-*-coding: utf-8 -*-
import os,random,json,requests,time,threading,itertools,sys,signal

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

def interrupted(signum, frame):
	raise Exception()

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
	print "\n"
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
	

def print_word_translate():
	global word_vocab
	global trans_vocab1
	global trans_vocab2
	tmp=['','','']
	print_line()
	for i in range(5):
		tmp[0]='[%s] %s'%('en',word_vocab[i])
		if(lan[0]!=''):
			tmp[1]= '[%s] %s'%(lan[0],trans_vocab1[i])
		if(lan[1]!=''):
			tmp[2]= '[%s] %s'%(lan[1],trans_vocab2[i])
		print "%-15s%-15s\t%s"%(tmp[0],tmp[1],tmp[2])
	print_line()

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
		print "How much that you can remember?(# Exit)"
		loading()
		random_word()
		get_translate()
		done=True
		cls()
		print "--------Learn station--------\n"
		print "How much that you can remember?(# Exit)"
		
		'''
		tmp=['','','']
		for i in range(5):
			tmp[0]='[%s] %s'%('en',word_vocab[i])
			if(lan[0]!=''):
				tmp[1]= '[%s] %s'%(lan[0],trans_vocab1[i])
			if(lan[1]!=''):
				tmp[2]= '[%s] %s'%(lan[1],trans_vocab2[i])
			print "%-15s%-15s\t%s"%(tmp[0],tmp[1],tmp[2])
		'''
		print_word_translate()
		x=raw_input("press enter to continue")
		if(x=='#'):
			break
		total+=5
		score+=dictation()
		cls()
		print "--------Learn station--------\n"
		print "total: %d \tyour score: %d \t%s\n"%(total,score,degree(score,total))
		while x!= 'n' and x!= 'y':
			x=raw_input("Do you want to play again? (y/n) : ").lower()
		
def word_shuffle():
	global word_vocab
	global done
	x='y'

	while(x=='y'):
		signal.signal(signal.SIGALRM, interrupted)
		
		cls()
		print "--------Word shuffle-------\n"
		x=0
		print "Sort the shuffle letter to word."
		print "Time limit 60 sec and # to skip.\n"
		while not (x=='1' or x=='2'):
			x=raw_input("Number of player(1/2) : ")
		x=int(x)
		loading()
		random_word()
		get_translate()
		done=True
		tmp=['']*10
		for i in range(10):
			tmp[i] = ' '.join(random.sample(word_vocab[i],len(word_vocab[i])))
			while(tmp[i].replace(' ','')==word_vocab[i]):
				tmp[i] = ' '.join(random.sample(word_vocab[i],len(word_vocab[i])))

		check=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
		usedtime=[0]*x
		total =10
		for j in range(x):
			cls()
			print "--------Word shuffle-------\n"
			z=raw_input("Player%d are you ready?\n(press enter to start)"%(j+1))
			usedtime[j]=time.time()

			try:
				signal.alarm(30)
				for i in itertools.cycle(range(10)):
					if sum(check[j]) == 10:
						break
					elif check[j][i]==1:
						continue
					cls()
					print "--------Word shuffle-------\n"
					print "Player %d turn, press # to skip.\n"%(j+1)
					#print "------ %s ------\n"%tmp[i]
					print tmp[i].center(27,'-')
					y=''
					while(y!=word_vocab[i]):
						y=raw_input("Input: ")
						if(y==word_vocab[i]):
							print "----- Correct! -----\n"
							check[j][i]=1
							print_con()
						if(y=='#'):
							break
						print "----- Try again! -----\n"
				signal.alarm(0)
				usedtime[j]=int(time.time()-usedtime[j])
			except:
				print "\n\n----------- Time out! ------------"
				print_con()
				usedtime[j]='timeout'
			cls()
			print "--------Word shuffle-------\n"
			print "player %d score: %d/10 \t%s\nUsed time : %s\n"%(j+1,sum(check[j]),degree(sum(check[j]),total),str(usedtime[j]))
			print_word_translate()
			print "\n"
			print_con()
		cls()
		print "--------Word shuffle-------\n"
		if(x==1):
			print ""
		elif(sum(check[0])>sum(check[1])):
			print "The winner is player 1\n"
		elif(sum(check[1])>sum(check[0])):
			print "The winner is player 2\n"
		elif(usedtime[0]==usedtime[1]):
			print "Draw!"
		elif(usedtime[0]<usedtime[1]):
			print "The winner is player 1\n"
		else:
			print "The winner is player 2\n"

		
		
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
