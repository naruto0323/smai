
# import xml.etree.ElementTree as ET
import xml.sax, textProccesor, timeit, re
import pickle
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from nltk.corpus import stopwords

wikiIndex = {}
class WikiHandler(xml.sax.ContentHandler):
	def build(self, title, id, bodyText, infobox, categories, links):
		print bodyText
		print id
		# print "jksdfcbsjkdfb"
		# for word in bodyText:
		# 	if word not in wikiIndex.keys():
		# 		wikiIndex[word] = {}
		# 	if id not in wikiIndex[word].keys():
		# 		wikiIndex[word][id] = ""
		# 	if ('b' not in wikiIndex[word][id]):
		# 		wikiIndex[word][id] += 'b' + str(bodyText.count(word))


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
	# print "ajsdbasjkdb"
	myParse('/home/ram/Desktop/pun/smai/ire-wiki-search/wiki-search-small.xml')