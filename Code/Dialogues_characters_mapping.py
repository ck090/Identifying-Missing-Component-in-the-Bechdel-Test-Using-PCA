import pandas as pd
import os
code_dir=os.path.dirname(os.path.realpath(__file__))
data_dir=os.path.dirname(code_dir)+'\Data'
movie_character_df = pd.read_csv(data_dir+'\mcm_csv.csv')

movie_conversations_df=pd.read_csv(data_dir+'\mc_csv.csv')
# print movie_conversations_df.head(10)

conversations={}
to_type={}
for i in range(len(movie_character_df)):

	conversations[movie_character_df.Character_Id[i]]={"movie_numner":movie_character_df.Movie_Number[i],"dialogs":{}}#,"dialog_numbers_list":[]}}
	conversations[movie_conversations_df.Character_Id1[i]]["dialogs"][movie_conversations_df.Character_Id2[i]]=[]

temp_list=[]
# for i in conversations:
# 	print i ,":",conversations[i]
for i in range(len(movie_conversations_df)):
	try:
		j=movie_conversations_df.List_of_Utterance[i]
		j=j.replace('[',"")
		j=j.replace(']',"")
		j=j.replace("'","")
		j=j.split(", ")
		# print "---" ,movie_conversations_df.List_of_Utterance[i] 

		conversations[movie_conversations_df.Character_Id1[i]]["dialogs"][movie_conversations_df.Character_Id2[i]].append(j)
	except:
		continue
	# conversations[movie_conversations_df.Character_Id1[i]]["dialogs"]["to"][movie_conversations_df.Character_Id2[i]]["dialog_numbers_list"].append(movie_conversations_df.List_of_Utterance[i])
	


for i in conversations:
	print i ,":",conversations[i]
	