import pandas as pd
import os
import pickle
pickle_in=open('pos_tags_utterances.pickle','rb')
list1=pickle.load(pickle_in)
pos_tags=list1[0]
utterances=list1[1]
# for i,j in utterances.items():
# 	print i,'---',j

keys=utterances.keys()
values=pos_tags
print len(keys),len(values)
pos_dict={}
for i in range(len(keys)):
	pos_dict[keys[i]]=pos_tags[i]


import re

noun_pattern=re.compile("[N][N]*")
verb_pattern=re.compile("[V][B]*")
adjective_pattern=re.compile("[J][J]*")

noun_count_dict={}
verb_count_dict={}
adj_count_dict={}
for i in pos_dict.keys():
	noun_count=0
	adj_count=0
	verb_count=0
	for words in pos_dict[i]:

		 if (noun_pattern.match(words[1])):
		 	noun_count=noun_count+1
		 elif(verb_pattern.match(words[1])):
		 	verb_count=verb_count+1
		 elif(adjective_pattern.match(words[1])):
		 	adj_count=adj_count+1
	noun_count_dict[i]=noun_count
	verb_count_dict[i]=verb_count
	adj_count_dict[i]=adj_count	 			

# for i in pos_dict.keys():
# 	print pos_dict[i],'---', noun_count_dict[i], verb_count_dict[i]

pickle_out=open('nn_vb_jj_pos_dicts.pickle','wb')
pickle.dump([pos_dict,noun_count_dict,verb_count_dict,adj_count_dict],pickle_out)
pickle_out.close()
