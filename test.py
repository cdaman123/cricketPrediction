import pickle
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[0, 1, 1, 0, 0, 0]]))