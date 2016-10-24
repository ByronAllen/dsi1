from imdbpie import Imdb
import pandas as pd

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

imdb = Imdb()
imdb = Imdb(anonymize=True)
top250 = imdb.top_250()
#print top250
top250_df = pd.DataFrame(data=top250)

top250_df.to_csv('./imdb_top250.csv')
