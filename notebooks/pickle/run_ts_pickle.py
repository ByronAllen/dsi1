
#!usr/bin/env python

import sklearn.linear_model
import pandas as pd
import pickle
import matplotlib.pyplot as plt

input_df = pd.read_csv('test_x_df.csv')

ts = pickle.loads(open('ts.pickle').read())

print ts.predict(input_df)
results = ts.predict(input_df)

print len(input_df)
print len(results)

plt.scatter(input_df,results)
plt.show()


