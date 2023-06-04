import pandas as pd 
import numpy as np 
import sklearn.preprocessing as preprocessing
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

from sklearn.preprocessing import OneHotEncoder
labelEnc = preprocessing.LabelEncoder()
new_data = labelEnc.fit_transform(data)
onehotEnc = preprocessing.OneHotEncoder()
onehotEnc.fit(new_data.reshape(-1, 1))
data = onehotEnc.transform(new_data.reshape(-1, 1))
# y = OneHotEncoder().fit_transform(data).toarray()
print(data.toarray())

