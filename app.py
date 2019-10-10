from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def p():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    s = [0,0,0,0,0,0]
    name = [int(x) for x in request.form.values()]
    if name[0] == 1:
        s[0] = 1
    elif name[0] == 2:
        s[1] = 1
    if name[1] == 1:
        s[2] = 1
    elif name[1] == 2:
        s[3] = 1
    if name[2] == 1:
        s[4] = 1
    if name[3] == 1:
        s[5]  =1
    model = pickle.load(open('model.pkl','rb'))
    N = model.predict([s])
    S = "Probability for Playing is : "+str(round(N[0]*100,2))+"%"
    if N[0]<.5:
        T = "Not Good for Playing."
    else:
        T = "Good for Playing"
    return render_template('index.html',result1 = S, result2 = T )

if __name__ == "__main__":
    app.run(debug=False)