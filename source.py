import pandas as pd 
import numpy as np

import matplotlib.pyplot as plt

from warnings import filterwarnings

filterwarnings(action = "ignore")


train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
print(train) 

train.head() 

train.shape
test.shape
train.isnull().sum()
test.isnull().sum()
train.describe()  



plt.figure(1)
train.loc[train['Survived'] == 1 ,"Pclass" ].value_counts().sort_index().plot.bar()
plt.title("Bar graph of people according tickte class who servived")

plt.figure(2) 
train.loc[train['Survived'] == 0 ,"Pclass"].value_counts().sort_index().plot.bar()  
plt.title("Bar graph of people according tickte class who didn't servived")




fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis("equal") 
l = ["c = cherbourg", "s = southampton" , "q =  queenstown" ]
s = [0.546464,0.23434 , 0.5354343]
ax.pie(s,labels = l,autopct = "%1.2f%%")




