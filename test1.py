import pandas as pd
import os
import pickle
pickle_in=open('nn_vb_jj_pos_dicts.pickle','rb')
list1=pickle.load(pickle_in)
pos_dict=list1[0]
noun_count_dict=list1[1]
verb_count_dict=list1[2]
adj_count_dict=list1[3]
word_count_dict=list1[4]

pickle_in2=open('result_df.pickle','rb')
result_df=pickle.load(pickle_in2)

print result_df.describe()

for i in range(len(result_df)):
	for j in result_df.gender1[i]:
		result_df.gender1[i]=j.upper()
	for j in result_df.gender2[i]:
		result_df.gender2[i]=j.upper()

print result_df.describe()
pickle_output=open('result_df.pickle','wb')
pickle.dump(result_df,pickle_output)

pickle_output.close()