import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import roc_curve, auc

data=pd.read_csv("D:/Projects/Sem 3/final.csv")

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.20,random_state=0)

from sklearn.linear_model import LogisticRegression as RR
model=RR()
model.fit(x_train,y_train)

a=model.predict(np.array([[5,7.4,0.66,0,1.8,0.075,13,40,0.9978,3.51,0.56,9.4,5
]]))

if a==0:
    print("Color of Your wine is Red")
else:
    print("Color of Your wine is white")