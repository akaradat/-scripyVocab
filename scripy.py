#-*-coding: utf-8 -*-
import os,random,json,requests,time,threading,itertools,sys,signal
from bs4 import BeautifulSoup 
#textname='vocabularyTest.txt'
#vocab=open(textname).read().split()

#url="http://www.manythings.org/vocabulary/lists/a/words.php?f=animals_1"
#page=requests.get(url)
#soup = BeautifulSoup(page.content,'html.parser')

count_learn=[0,0]
catalog_now="Animals"
catalog_amount=29
catalog_selected=3
slan=[]
llan=[]
vocab=[]
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
		print "-"*30
	else:
		print "-"*x

def print_con():
	x=raw_input("press enter to continue.")

def loading():
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

def getvocab(x):
	global vocab
	global catalog_now
	global done
	
	#find url of catalog
	vocab=[]
	page=requests.get("http://www.manythings.org/vocabulary/lists/a/")
	soup = BeautifulSoup(page.content,'html.parser')
	url="http://www.manythings.org/vocabulary/lists/a/"+soup.find_all('a')[x]['href']
	catalog_now=soup.find_all('a')[x].text
	#get vocab
	page=requests.get(url)
	soup = BeautifulSoup(page.content,'html.parser')
	for x in soup.find_all('li'):
		vocab.append(x.text.lower())


def get_translate():
	
	global trans_vocab1
	global trans_vocab2
	global lan
	global word_vocab
	trans_vocab1=[]
	trans_vocab2=[]

	for i in range(len(word_vocab)):
		url1='https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=%s&dt=t&q=%s'%(lan[0],word_vocab[i])
		url2='https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=%s&dt=t&q=%s'%(lan[1],word_vocab[i])
		trans_vocab1.append(json.loads(requests.get(url1).text)[0][0][0].lower())
		trans_vocab2.append(json.loads(requests.get(url2).text)[0][0][0].lower())
	
	

def random_word(n):
	global done
	global vocab
	global word_vocab
	word_vocab=[]
	loading()
	if len(vocab) < n:
			getvocab(catalog_selected)
	
	while True:
		tmp=random.choice(vocab).lower()
		if tmp not in word_vocab:
			word_vocab.append(tmp)
			if len(word_vocab) == n:
				break

	get_translate()
	done = True

def delword():
	global vocab
	global word_vocab
	for i in word_vocab:
		print i
		vocab.remove(i)



def print_word_translate():
	global word_vocab
	global trans_vocab1
	global trans_vocab2
	tmp=['','','']
	print_line()
	for i in range(len(word_vocab)):
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
		print ' Dictaion '.center(30,'-')
		print "Did you remember this?\n"
		print "%s %s\n"%(tmp[0],tmp[1])
		j=0
		while(j<3):
			x=raw_input("In english is: ")
			if(x.lower()==word_vocab[i]):
				score+=1
				print " Correct! ".center(30,'-'),'\n'
				print_con()
				break
			else:
				print " Try again! ".center(30,'-'),'\n'
			j+=1
		if(j==3):
			print_line()
			print "%s %s in english is %s"%(tmp[0],tmp[1],word_vocab[i])
			print_line()
			print_con()

	cls()
	print " Dictaion ".center(30,'-')
	print_line(30)
	print "%7d/%d %s"%(score,5,degree(score,5))
	print_line(30)
	print_con()
	count_learn[0]+=5
	count_learn[1]+=score
	return score


def learn_vocab():
	global word_vocab
	global lan
	global trans_vocab1
	global trans_vocab2
	total = 0
	score = 0
	
	x='y'
	while(x=='yes' or x=='y'):
		cls()
		print " Learn station ".center(30,'-'),'\n'
		print "How much that you can remember?\n"
		x=raw_input("press enter to start")
		cls()
		print " Learn station ".center(30,'-'),'\n'
		print "How much that you can remember?"
		random_word(5)
		
		cls()
		print " Learn station ".center(30,'-'),'\n'
		print "How much that you can remember?"
		
		print_word_translate()
		x=raw_input("press enter to continue")
		total+=5
		score+=dictation()
		cls()
		print " Learn station ".center(30,'-'),'\n'
		print "total: %d \tyour score: %d \t%s\n"%(total,score,degree(score,total))
		while x!= 'n' and x!= 'y':
			x=raw_input("Do you want to play again? (y/n) : ").lower()
		
		delword()
		
def hangman():
	global word_vocab
	global vocab
	x='y'
	while(x=='yes' or x=='y'):
		signal.signal(signal.SIGALRM, interrupted)
		cls()
		print " Hangman ".center(30,'-'),'\n'
		print "We hint all vowel in the word.\nJust guess other character.\n"

		while True:
			x=raw_input("Number of player(1/2) : ").lower()
			if x== '1' or x== '2':
				break

		x=int(x)
		
		random_word(5)
		score=[0,0]
		usedtime=[0,0]
		for n in range(x):
			tmp = []
			count=[]
			p=[]
			for i in range(5):
				tmp.append(list('_'*len(word_vocab[i])))
				count.append(0)
				p.append(0)
			for i in range(5):
				for j in range(len(word_vocab[i])):
					z=word_vocab[i][j]
					if(z=='a' or z=='e' or z=='i' or z=='o' or z=='u'):
						tmp[i][j]=word_vocab[i][j]
			cls()
			print " Hangman ".center(30,'-'),'\n'
			z=raw_input("Player%d are you ready?\n(press enter to start)"%(n+1))
			usedtime[n]=time.time()

			try:
				signal.alarm(60)
				for i in itertools.cycle(range(5)):
					if(0 not in p):
						break
					elif(p[i]==1):
						continue
					while(count[i]<5):
						cls()
						print " Hangman ".center(30,'-'),'\n'
						print "Score: %d Word#: %d (# to skip.)\n"%(p.count(1),i+1)
						print "lift left: ",5-count[i]
						print ' '.join(tmp[i])
						guess=raw_input("guess: ")
						if guess == '#':
							break
						for k in range(len(guess)):
							check=0
							for j in range(len(word_vocab[i])):
								if(guess[k] == word_vocab[i][j]):
									tmp[i][j]=word_vocab[i][j]
									check=1
							if(check==0):
								count[i]+=1
						if(''.join(tmp[i])==word_vocab[i]):
							p[i]=1
							print '\n'," Correct! ".center(30,'-')
							print 'Answer is',word_vocab[i],'\n'
							print_con()
							break
						if(count[i]>=5):
							p[i]=-1
							print '\n',' Wrong! '.center(30,'-')
							print 'Answer is',word_vocab[i],'\n'
							print_con()

				signal.alarm(0)
				usedtime[n]=int(time.time()-usedtime[n])
			except:
				print '\n\n'," Time out! ".center(30,'-')
				print_con()
				usedtime[n]='timeout'


			score[n]=p.count(1)
			cls()
			print " Hangman ".center(30,'-'),'\n'
			print "Score %d/5 %s Used time: %s"%(score[n],degree(score[n],5),str(usedtime[n]))
			print_word_translate()
			print ''
			print_con()
		
		cls()
		print " Hangman ".center(30,'-'),'\n'
		if(x==1):
			print ""
		elif(score[0]>score[1]):
			print "The winner is player 1\n"
		elif(score[1]>score[0]):
			print "The winner is player 2\n"
		elif(usedtime[0]==usedtime[1]):
			print "Draw!"
		elif(usedtime[0]<usedtime[1]):
			print "The winner is player 1\n"
		else:
			print "The winner is player 2\n"
		count_learn[0]+=5
		count_learn[1]+=score[0]

		while True:
			x=raw_input("Do you want to play again? (y/n) : ").lower()
			if x== 'n' or x== 'y':
				break
		delword()



def word_shuffle():
	global word_vocab
	global vocab
	x='y'

	while(x=='y'):
		signal.signal(signal.SIGALRM, interrupted)
		cls()
		print " Word shuffle ".center(30,'-'),'\n'
		x=0
		print "Sort the shuffle letter."
		print "Time limit 60 sec and # to skip.\n"
		while not (x=='1' or x=='2'):
			x=raw_input("Number of player(1/2) : ")
		x=int(x)
		random_word(5)
		tmp=['']*5
		for i in range(5):
			tmp[i] = ' '.join(random.sample(word_vocab[i],len(word_vocab[i])))
			while(tmp[i].replace(' ','')==word_vocab[i]):
				tmp[i] = ' '.join(random.sample(word_vocab[i],len(word_vocab[i])))

		check=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
		usedtime=[0]*x
		total = 5
		for j in range(x):
			cls()
			print " Word shuffle ".center(30,'-'),'\n'
			z=raw_input("Player%d are you ready?\n(press enter to start)"%(j+1))
			usedtime[j]=time.time()

			try:
				signal.alarm(60)
				for i in itertools.cycle(range(5)):
					if sum(check[j]) == 5:
						break
					elif check[j][i]==1:
						continue
					cls()
					print " Word shuffle ".center(30,'-'),'\n'
					print "Player %d turn, press # to skip.\n"%(j+1)
					print tmp[i].center(27,'-')
					y=''
					while(y!=word_vocab[i]):
						y=raw_input("Input: ")
						if(y==word_vocab[i]):
							print " Correct! ".center(30,'-'),'\n'
							check[j][i]=1
							print_con()
						if(y=='#'):
							break
						print " Try again! ".center(30,'-'),'\n'
				signal.alarm(0)
				usedtime[j]=int(time.time()-usedtime[j])
			except:
				print '\n\n'," Time out! ".center(30,'-')
				print_con()
				usedtime[j]='timeout'
			cls()
			print " Word shuffle ".center(30,'-'),'\n'
			print "player %d score: %d/%d \t%s\nUsed time : %s\n"%(j+1,sum(check[j]),5,degree(sum(check[j]),total),str(usedtime[j]))
			print_word_translate()
			print "\n"
			print_con()
		cls()
		print " Word shuffle ".center(30,'-'),'\n'
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

		count_learn[0]+=5
		count_learn[1]+=sum(check[0])
		
		
		while x!= 'n' and x!= 'y':
			x=raw_input("Do you want to play again? (y/n) : ").lower()

		delword()

def getlan():
	global slan
	global llan
	global done
	
	if not slan:
		loading()
		inurl="https://cloud.google.com/translate/docs/languages"
		inpage=requests.get(inurl)
		insoup = BeautifulSoup(inpage.content,'html.parser')
		slan.append('')
		llan.append('')
		for i in range(len(insoup.find_all('tbody')[0])/2):
			j=insoup.find_all('tbody')[0].find_all('tr')[i].find_all('td')
			llan.append(j[0].text)
			slan.append(j[1].text)
		done=True

def showlan():
	global slan
	global llan
	print '\n'," Available language ".center(30,'-'),'\n'
	for i in range(len(slan)-1):
		print "\t%s : %s"%(slan[i+1].split()[0],llan[i+1])


def settinglan():
	global lan
	x=''
	
	getlan()
	while(x!='#'):
		cls()
		print " Setting Language ".center(30,'-')
		print "\t[1].First language: ",lan[0]
		print "\t[2].Second language: ",lan[1]
		print "\t[3].Show language available"
		print "\t #  Back"
		x=raw_input("Select: ")

		if x=='1':
			y=raw_input("Input first language: ")
			if(y in slan):
				lan[0]=y
			else:
				print "Unavailable language!\n"
				print_con()

		elif x=='2':
			y=raw_input("Input second language: ")
			if(y in slan):
				lan[1]=y
			else:
				print "Unavailable language!\n"
				print_con()
		elif x=='3':
			showlan()
			print_con()

		

def showvocablist():
	page=requests.get("http://www.manythings.org/vocabulary/lists/a/")
	soup = BeautifulSoup(page.content,'html.parser') 
	i=1
	print '\n'," vocab catalog ".center(30,'-'),'\n'
	for x in soup.find_all('li'):
		print "[%d] %s"%(i,x.text)
		i=i+1
	catalog_amount=i-1
		
def settingvocab():
	x=''
	while(x!='#'):
		cls()
		print " Setting vocab ".center(30,'-')
		showvocablist()
		print_line()
		print "\nCatalog now: %s"%(catalog_now)
		x=raw_input("Select (# to back): ")
		if(x.isdigit()):
			if(int(x)>=1 and int(x)<=catalog_amount):
				catalog_select=int(x)
				getvocab(catalog_select)
				break


def setting():
	global lan
	x=''
	while(x!='#'):
		cls()
		print " Setting ".center(30,'-')
		print "\t[1].language [%s,%s]"%(lan[0],lan[1])
		print "\t[2].vocab catalog [%s]"%(catalog_now)
		print "\t #  Back"
		x=raw_input("Select: ")
		if x=='1':
			settinglan()
		elif x=='2':
			settingvocab()

def home():
	x=''
	while(x!='#'):
		cls()
		print " Welcome to Scripy Vocab ".center(50,'-')
		print "\t[1].Learn vocabuary"
		print "\t[2].Hangman Game"
		print "\t[3].Word shuffle Game"
		print "\t[4].Setting"
		print "\t #  Exit"
		x=raw_input("Select: ")

		if (x=='1'):
			learn_vocab()
		elif (x=='2'):
			hangman()
		elif (x=='3'):
			word_shuffle()
		elif (x=='4'):
			setting()
	cls()

	print "\n\n\n\n\n\n",' Total vocab: %d You learned: %d '.center(50,"=")%(count_learn[0],count_learn[1]),'\n',' Good bye! '.center(50,"="),"\n\n\n\n\n\n\n\n"		

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
