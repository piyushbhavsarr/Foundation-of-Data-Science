import pandas as pd

from sklearn import Preprocessing

#label encoding

data=pd.read_csv("data.csv")
df=pd.DataFrame(data)
'''label_enc=Preprocessing.LabelEncoder()
df=label_enc.fit_transform(df['Purchased'])
print(df)'''

#one hot encoding
enc=Preprocessing.OneHotEncoder()
enc_df=pd.DataFrame(enc.fit_transform(df[['Country']])).toarray()


