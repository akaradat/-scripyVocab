#-*-coding: utf-8 -*-

from googletrans import Translator
import random

#list of vocabulary
word =['แมว','หมา','นก','ปลา','ผึ้ง','หมี','อูฐ','นกอินทรี','ช้าง','จิงโจ้',
'สิงโต','เพนกวิน','ฉลาม','เสือ','ค้างคาว','กระต่าย','เต่า','หมู','แพะ','แกะ',
'ม้า','มังกร','กวาง','ควาย','จิราฟ','ลิง','งู','แมงป่อง','แมงมุม','ไส้เดือน',
'กบ','คางคก','ผีเสื้อ','แมลงสาบ','แมลงปอ','แมลงวัน','หนอน','มด','แพนด้า','เหยี่ยว']


ts = Translator()

#score counter
total=0
correct=0
wrong=0
x=''
print '----------Hello welcome to Dictation Game---------\nInput the word in english to get point.(To exit in put \'exit\')\nSTART'

#repeat until input exit
while (x!='exit'):
        #random word
	i = random.randrange(len(word))
	print word[i]
	x=raw_input()

	#translate word to english
	y= ts.translate(word[i]).text.lower()

	#compare between word and input
	if y == x.lower():
		print '-----Correct-----'
		correct+=1
	else :
		print '----- ',word[i],' = ',y,' -----'
		wrong+=1
	total+=1

#end game
print '--------------------------\nTotal:{0} Correct:{1} Wrong:{2}'.format(total-1,correct,wrong-1)
