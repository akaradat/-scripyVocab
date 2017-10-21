#-*-coding: utf-8 -*-


ip1=''

while(ip1!='#')
	print "---------- Welcome to Scripy Vocab ----------"
	print "\t1.Learn vocabuary"
	print "\t2.Hangman Game"
	print "\t3.Word shuffle Game"
	print "\t4.Setting"
	print "\t# Exit"
	ip1=raw_input("Select: ")

	if (ip1=='1'):
		learn_vocab()
	elif (ip1='2'):
		hangman()
	elif (ip1='3'):
		word_shuffle()
	elif (ip1='4'):
		setting()
