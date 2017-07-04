import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
f=open("testing")
raw=f.read()
ak=[]
ak=nltk.sent_tokenize(raw)
flag=0
training_data=open("training")
train=training_data.read()
train=train.split("\n")
global_answer="false"
for v3 in ak:
	word_tokens=[]
	word_tokens=nltk.word_tokenize(v3)
	filtered_sentence=[]
	for w in word_tokens:
		
    		if w not in stop_words:
        		filtered_sentence.append(w)
	
	answer="false"
	ak1=[]
	for w1 in train:
		ak1=nltk.word_tokenize(w1)
		filtered_sentence2=[]
		for w in ak1:
		
    			if w not in stop_words:
        			filtered_sentence2.append(w)
		cnt=0
		for w in filtered_sentence:
			for w2 in filtered_sentence2:
				#print w,w2
				if w.lower()==w2.lower():
					cnt+=1
		#print cnt
		#print len(ak1)/2
		if cnt>=(len(ak1)/2) and cnt>0:
			answer="true"
		if answer=="true":
			global_answer="true"
print global_answer
