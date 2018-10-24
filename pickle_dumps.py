import pandas as pd
import os
dir_path="C:\\Users\\Krishna\\Desktop\\Projects\\BechdelPlusPlus\\New_Bechdel"
movie_character_df = pd.read_csv(dir_path+'\mcm_csv.csv')

movie_conversations_df=pd.read_csv(dir_path+'\mc_csv.csv')
movie_lines_df=pd.read_csv(dir_path+'\ml_csv.csv')
# result_df=pd.DataFrame(columns=('movie','ch1','ch2'  """,'gender1','gender2'""", 'dialog'))
count=0
list_of_utterances=[]
# for i in range(len(movie_conversations_df)):
#     j=movie_conversations_df.List_of_Utterance[i]
# #     print type(j)
# #     j=j.replace('[',"")
# #     j=j.replace(']',"")
# #     j=j.replace("'","")
# #     j=j.split(", ")
#     list_of_utterances.append(j)
# movie_conversations_df['List_of_Utterance']=list_of_utterances
total_list=[]
print movie_conversations_df.head()
for i in range(1000):#len(movie_conversations_df) 5000 dialogs initially
    temp=movie_conversations_df.List_of_Utterance[i]
    temp=movie_conversations_df.List_of_Utterance[i]
    temp=temp.replace('[',"")
    temp=temp.replace(']',"")
    temp=temp.replace("'","")
    temp=temp.split(", ")
    for j in range(len(temp)):
        total_list.append([movie_conversations_df.Movie_Number[i],movie_conversations_df.Character_Id1[i],
         movie_conversations_df.Character_Id2[i],
         movie_character_df['Gender'][movie_character_df['Character_Id']==movie_conversations_df.Character_Id1[i]].values
         ,movie_character_df['Gender'][movie_character_df['Character_Id']==movie_conversations_df.Character_Id2[i]].values,
         temp[j],
         movie_lines_df['Dialogue'][movie_lines_df['Line_Id']==temp[j]].values])
        count=count+1
        # print count
result_df=pd.DataFrame(total_list,columns=('movie','ch1','ch2','gender1','gender2','line_id', 'dialog'))
for i in range(len(result_df)):
	for j in result_df.gender1[i]:
		result_df.gender1[i]=j.upper()
	for j in result_df.gender2[i]:
		result_df.gender2[i]=j.upper()
print count
import pickle
pickle_output=open('result_df.pickle','wb')
pickle.dump(result_df,pickle_output)

pickle_output.close()

