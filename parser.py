#!/usr/bin/python
import xml.sax, textProccesor, timeit, re
import sys
from xmlExtract import *
wikiIndex = {}
co_occurence_matrix={}
class WikiHandler(xml.sax.ContentHandler):
	def build(self, title, id, bodyText, infobox, categories, links):
		# for word in bodyText:
		# 	if word not in wikiIndex.keys():
		# 		wikiIndex[word] = {}
		# 	if id not in wikiIndex[word].keys():
		# 		wikiIndex[word][id] = ""
		# 	if ('b' not in wikiIndex[word][id]):
		# 		wikiIndex[word][id] += 'b' + str(bodyText.count(word))
		# 	print id
		# print bodyText
		count=0
		for sen in bodyText:
			for word in sen:
				for words in sen:
					try:
						co_occurence_matrix[word][words]+=1
					except KeyError:
						try:
							co_occurence_matrix[words][word]+=1
						except KeyError:
							
							if word in co_occurence_matrix:
								co_occurence_matrix[word][words]=1
							else:
								co_occurence_matrix[word]={}
								co_occurence_matrix[word][words]=1
						else:
							if word in co_occurence_matrix:
								co_occurence_matrix[words][word]=1
							else:
								co_occurence_matrix[words]={}
								co_occurence_matrix[words][word]=1
			# 	if count < len(bodyText)-1:
			# 		try:
			# 			co_occurence_matrix[word][words]+=1
			# 		except KeyError:
			# 			if word in co_occurence_matrix:
			# 				co_occurence_matrix[word][words]=1
			# 			else:
			# 				co_occurence_matrix[word]={}
			# 				co_occurence_matrix[word][words]=1
			# count=count+1	
		f = open('cooccurence.p','w')
		pickle.dump(co_occurence_matrix, f)
		f.close()
		# print co_occurence_matrix


	def __init__(self):
		self.CurrentData = ""
		self.title = ""
		self.id = ""
		self.text = ""
		self.infobox = []
		self.categories = []
		self.links = []
		self.bodyText = []
		self.idFlag = 0

	# Called when an element starts
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "page":
			# print "\n***** Page *****"
			self.idFlag = 0
		elif tag == "text":
			self.text = ""

	# Called when an elements ends
	def endElement(self, tag):
		if self.CurrentData == "title":
			pass
			# print "Title:", self.title.encode('utf-8')
		elif self.CurrentData == "id":
			if self.idFlag == 0:
				pass
				# print "ID:", self.id.encode('utf-8')
			self.idFlag = 1
		elif self.CurrentData == "text":
			self.links, self.categories, self.infobox, self.bodyText = textProccesor.process(self.text)
			self.build(self.title, self.id.encode('utf-8'), self.bodyText, self.infobox, self.categories, self.links)
			# print self.links
			# print self.categories
			# print self.infobox
			# print self.bodyText
		self.CurrentData = ""

	# Called when a character between tags is read
	def characters(self, content):
		if self.CurrentData == "title":
			self.title = content
			self.title = re.findall("\d+|\w+",self.title)
			self.title = [token.encode('utf-8') for token in self.title]
		elif self.CurrentData == "id":
			if self.idFlag  == 0:
				self.id = content
		elif self.CurrentData == "text":
			self.text += content

def myParse(corpus):
	parser = xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	myHandler = WikiHandler()
	parser.setContentHandler(myHandler)
	parser.parse(corpus)

if __name__ == '__main__':
	start = timeit.default_timer()
	myParse('/home/ram/Desktop/pun/smai/ire-wiki-search/wiki-search-small.xml')
	f = open('a.txt', 'w' )
	f.write(repr(wikiIndex))
	f.close()
	stop = timeit.default_timer()
	# print stop - start
