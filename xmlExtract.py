import xml.etree.ElementTree as ET
import pickle
import sys
from nltk.stem.porter import *
stemmer = PorterStemmer()
reload(sys)
sys.setdefaultencoding('utf-8')
from nltk.corpus import stopwords


tree = ET.parse('subtask1-heterographic-test.xml')
root = tree.getroot()
sentences = []
words = {}
stop = set(stopwords.words('english'))
scrap = ['"', "'", ":" , ",", "?", "!", "/", "_", ".", "-"]
wordset = set()


def extractXml():
	for sentence in root:
		line = ""
		for word in sentence:
			word = (word.text).lower()
			if((word not in stop) and (word[0] not in scrap)):
				#print word
				word=stemmer.stem(word).encode('utf-8')
				wordset.add(word)
			#line += word.text + " "
		#sentences.append(line)


def saveData():
	f = open('mainWords.p','w')
	pickle.dump(wordset, f)
	f.close()
	
                

# print mydict

extractXml()
saveData()
f = open('mainWords.p', 'rb')   # 'rb' for reading binary file
mydict = pickle.load(f)     
f.close()
mydict=list(mydict)
# print mydict












