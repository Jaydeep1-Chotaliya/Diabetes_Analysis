import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route("/")
def Home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    float_features=[float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    prediction=model.predict(features)
    #prediction_output = "Negative" if prediction == 0 else "Positive"
    return render_template("index.html",prediction_text=prediction)

if __name__=="__main__":
    app.run(debug=True)