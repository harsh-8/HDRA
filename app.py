# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:16:04 2021

@author: Harsh
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    if output == 1:
        return render_template('index.html', prediction_text='There is a risk of developing CHD.')
    else:
        return render_template('index.html', prediction_text='No risk of developing CHD.')

if __name__ == "__main__":
    app.run(debug=True)