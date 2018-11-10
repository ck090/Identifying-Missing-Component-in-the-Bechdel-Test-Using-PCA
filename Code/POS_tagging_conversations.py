import pandas as pd
import os
import nltk

code_dir=os.path.dirname(os.path.realpath(__file__))
data_dir=os.path.dirname(code_dir)+'\Data'
movie_lines_df=pd.read_csv(data_dir+'\ml_csv.csv')

movie_line_pos={}
for i in range(len(movie_lines_df)):
	# print movie_lines_df.Line_Id[i],':', movie_lines_df.Dialogue[i]
	tokens=nltk.tokenize.word_tokenize(movie_lines_df.Dialogue[i])
	# movie_line_pos{'line_id':movie_lines_df.Line_Id[i],pos_tags:[]}
	# print 'tokens:',tokens

	pos_tags=nltk.pos_tag(tokens)

	# print 'pos_tags:', pos_tags
	# adjectives=[]
	# verbs=[]
	# nouns=[]

	# for j in pos_tags:
	# 	if j[1]=='':
	# # 		print j 
	movie_line_pos[movie_lines_df.Line_Id[i]]=pos_tags
print movie_line_pos