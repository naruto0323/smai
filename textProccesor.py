#!/usr/bin/python
import re
from stop_words import get_stop_words
from nltk.stem.porter import *
from xmlExtract import *
counts={}
def tokenizer(text):                                                
	tokens = re.findall("\d+|\w+",text)
  	tokens = [token.encode('utf-8') for token in tokens]
  	return tokens

def removeStopWords(words):
	stopWords = get_stop_words('en')
	stopWords = [word.encode('utf-8') for word in stopWords]
	nonStopWords = [word for word in words if word not in stopWords]
	return nonStopWords

def stem(words):
	stemmer = PorterStemmer()
	_digits = re.compile('\d')
	stemmedWords = [stemmer.stem(word).encode('utf-8')for word in words if not bool(_digits.search(word))]
	return stemmedWords

def findExternalLinks(data):
	allLinks = []
	lines = data.split("==external links==")
	if (len(lines) > 1):
		links = lines[1]
		links = links.split('\n')
		for i in xrange(len(links)):
			link = links[i]
			if ("*[" in link or "* [" in link):
				link = link.split('[')
				link = link[1].split(' ')
				link = link[0]
				if "http" in link:
					allLinks.append(link)

	allLinks = tokenizer(' '.join(allLinks))
  	allLinks = removeStopWords(allLinks)
  	allLinks = stem(allLinks)
	return allLinks

def findElements(data):
	allCategories = []
	bodyText = []
	infobox = []
	bodyInPlay = True
	i = 0
	data=data.lower()
	lines = data.split('.')
	while i < len(lines):
		line = lines[i]
		if ("[[category:" in line):
			categories = line.split(':')
			# if len(categories) < 2:
			# 	print categories
			categories = categories[1]
			categories = categories.split(']]')
			categories = categories[0].strip().split(' ')
			# for cat in categories:
			# 	category = cat.strip()
			# 	if cat[-1] == '|':
			# 		category = category[:-1]
			# 	allCategories.append(category)
			# pass
		elif "{{infobox" in line:
			flag = 0
			tmp = lines[i].split('{{infobox')[1:]
			infobox.extend(tmp)
			while i < len(lines):
				if '{{' in lines[i]:
					count = lines[i].count('{{')
					flag += count
				if '}}' in lines[i]:
					count = lines[i].count('}}')
					flag -= count
				if flag <= 0:
					break
				# infobox.append(lines[i])
				i += 1
		elif bodyInPlay:
			if '[[category' in line or '==external links==' in line:
				bodyInPlay = 0
			else:
				sent=line.split(' ')
				sent = tokenizer(' '.join(sent))
				sent = removeStopWords(sent)
				# print sent
				# if len(sent) > 35:
					# sent=sent[:35]
				sent = stem(sent)
				for word in sent :
					if len(word)>1 and word in mydict:
						try:
							counts[word]+=1
						except KeyError:
							counts[word]=1
					else:
						sent.remove(word)
				bodyText.append(sent)
		i += 1

	# Tokenisation
	# allCategories = tokenizer(' '.join(allCategories))
  	# infobox = tokenizer(' '.join(infobox))
  	# bodyText = tokenizer(' '.join(bodyText))

  	# Stop Word Removal
  	# allCategories = removeStopWords(allCategories)
  	# infobox = removeStopWords(infobox)
  	# bodyText = removeStopWords(bodyText)
  
  	# Stemming
  	# allCategories = stem(allCategories)
  	# infobox = stem(infobox)
  	# for sentence in body text
  	# bodyText = stem(bodyText)


	return allCategories, infobox, bodyText

def process(text):
    text = text.lower()
    links = findExternalLinks(text)
    categories, infobox, bodyText = findElements(text)
    return links, categories, infobox, bodyText






