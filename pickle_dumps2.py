import pandas as pd
import pickle
import os
import nltk
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
dir_path="C:\\Users\\Krishna\\Desktop\\Projects\\BechdelPlusPlus\\New_Bechdel"
movie_character_df = pd.read_csv(dir_path+'\mcm_csv.csv')

movie_conversations_df=pd.read_csv(dir_path+'\mc_csv.csv')
movie_lines_df=pd.read_csv(dir_path+'\ml_csv.csv')
list_of_utterances={}
trans_table = ''.join( [chr(i) for i in range(128)] + ['?'] * 128 )
# line_id_mapping={}
for i in range(3500):#len(movie_lines_df)
	# 
	# if movie_lines_df.Line_Id[i] not in list_of_utterances.keys():
	# 	list_of_utterances[movie_lines_df.Line_Id[i]]=[]
	try:
		list_of_utterances[movie_lines_df.Line_Id[i]]=(nltk.word_tokenize(str(movie_lines_df.Dialogue[i])))
		# tokenizer.tokenize(movie_lines_df.Dialogue[i])
	except:
		list_of_utterances[movie_lines_df.Line_Id[i]]=(nltk.word_tokenize(str(movie_lines_df.Dialogue[i]).translate(trans_table)))
# for i in range(len(movie_lines_df)):
# 	# print movie_lines_df.Dialogue[i]
# 	tokens=nltk.word_tokenize(str(movie_lines_df.Dialogue[i]))
# 	list_of_utterances.append(tokens)
# print list_of_utterances	
pos_tags=[]
pos_tags=nltk.pos_tag_sents(list_of_utterances.values())

pickle_out=open('pos_tags_utterances.pickle','wb')
pickle.dump([pos_tags,list_of_utterances],pickle_out)
pickle_out.close	