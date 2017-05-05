#!/usr/bin/python

from stop_words import get_stop_words
from nltk.stem.porter import *

def inp():
	pun=0
	sum_weights=0
	count=0
	_input=raw_input("type sentence here")
	sent=_input.split(' ')
	sent = tokenizer(' '.join(sent))
	sent = removeStopWords(sent)
	sent = stem(sent)
	for words in sent:
		for word in sent and words not equal to word:
			try:
				sum_weights+=occurence[words][word]
			except KeyError:
				sum_weights+=occurence[word][words]
			finally:
				count=count+1
	sum_weights=sum_weights/count

	for words in sent:
		for word in sent and words not equal to word:
			try:
				val=occurence[words][word]
			except KeyError:
				val=occurence[word][words]
			finally:
				if val > sum_weights
				pun=1
	if pun:
		print "pun word"
if __name__ == '__main__':
	f = open('cooccurence.p', 'rb')   # 'rb' for reading binary file
	occurence = pickle.load(f)     
	f.close()
	inp()
	# mydict=list(mydict)