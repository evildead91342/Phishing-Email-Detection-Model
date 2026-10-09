import streamlit as st
import pickle
import re
import virustotal_python
from pprint import pprint
from base64 import urlsafe_b64encode
import pandas as pd

model = ('Logistic Regression', 'Random Forest', 'XGBoost', 'Support Vector Machine', 'k-nearest neighbors',
         'Naive Bayes', 'Decision Tree', 'Multilayer perceptron', 'AdaBoost', 'Gradient Boosting')
st.subheader(
    'Software system for detecting malicious content in email data using an algorithm doc2vec')

text = st.text_area('Enter the contents of the Email:')
urls = re.findall(
    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

with open('model/model_dbow.pkl', 'rb') as f:
    model_dbow = pickle.load(f)


def predict(model, model_dbow, text):
    text = text.split(' ')
    vec = model_dbow.infer_vector(text)
    pred = model.predict([vec])
    return pred


select_model = st.selectbox('Select classifier', model)
result = ['The Email is harmless', 'The Email is malicious']

if select_model == 'Logistic Regression':
    with open('model/Logistic Regression.pkl', 'rb') as f:
        model_lr = pickle.load(f)
    pred = predict(model_lr, model_dbow, text)
elif select_model == 'Random Forest':
    with open('model/Random Forest.pkl', 'rb') as f:
        model_rf = pickle.load(f)
    pred = predict(model_rf, model_dbow, text)
elif select_model == 'XGBoost':
    with open('model/XGBoost.pkl', 'rb') as f:
        model_xgb = pickle.load(f)
    pred = predict(model_xgb, model_dbow, text)
    # st.write(pred)
elif select_model == 'Support Vector Machine':
    with open('model/SVM.pkl', 'rb') as f:
        model_svm = pickle.load(f)
    pred = predict(model_svm, model_dbow, text)
elif select_model == 'k-nearest neighbors':
    with open('model/KNN.pkl', 'rb') as f:
        model_knn = pickle.load(f)
    pred = predict(model_knn, model_dbow, text)
elif select_model == 'Naive Bayes':
    with open('model/Naive Bayes.pkl', 'rb') as f:
        model_nb = pickle.load(f)
    pred = predict(model_nb, model_dbow, text)
elif select_model == 'Decision Tree':
    with open('model/Decision Tree.pkl', 'rb') as f:
        model_dt = pickle.load(f)
    pred = predict(model_dt, model_dbow, text)
elif select_model == 'Multilayer perceptron':
    with open('model/Neural Network.pkl', 'rb') as f:
        model_nn = pickle.load(f)
    pred = predict(model_nn, model_dbow, text)
    # st.write(pred)
elif select_model == 'AdaBoost':
    with open('model/AdaBoost.pkl', 'rb') as f:
        model_ada = pickle.load(f)
    pred = predict(model_ada, model_dbow, text)
elif select_model == 'Gradient Boosting':
    with open('model/Gradient Boosting.pkl', 'rb') as f:
        model_gb = pickle.load(f)
    pred = predict(model_gb, model_dbow, text)
else:
    st.write('Invalid Input')
# st.write('Used classifier:',select_model)
# st.write('Text:',text)
st.write('**Classification prediction:**')
st.info(result[pred[0]])
