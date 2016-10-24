from imdbpie import Imdb
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
imdb = Imdb()
imdb = Imdb(anonymize=True)
import json

reviews_df = pd.read_csv('./list_of_tconst.csv')
reviews_df.drop(labels='0',axis=1, inplace=True)
reviews_df.columns = ['tconst']
pure_list_of_tconst = list(reviews_df.tconst)

list_of_reviews=[]

#print i.text
#print i.username
#print i.date
#print i.rating
#print i.summary
#print i.status
#print i.user_location
#print i.user_score
#print i.user_score_count
#print 

for x in pure_list_of_tconst:        
	reviews = imdb.get_title_reviews(x, max_results=5)
	sub_list=''
	for rev in reviews:
		sub_list + reviews[0].text
	list_of_reviews.append(reviews[0].text)

print
print list_of_reviews

reviews_df['reviews'] = list_of_reviews
print reviews_df

reviews_df.to_csv('./reviews_df.csv')
