import streamlit as st
import requests


st.title('MY BEAUTIFUL AND UNDERSTANDABLE MINI-PROJECT')

st.write('''We predict the kind of iris it is depending on its
         petal and sepal characteristics''')


sepal_length=st.slider('What is the sepal length?',0,4,1)
sepal_width=st.slider('What is the sepal width?',0,4,1)

petal_length=st.slider('What is the petal length?',0,4,1)
petal_width=st.slider('What is the petal width?',0,4,1)

if(st.button('Predict')):
    url='https://my-api-app-474059628314.europe-west1.run.app/predict'
    params = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width,
    }
    response=requests.get(url, params).json()

    st.write(f"the prediction is that it belongs to the class {response['prediction']}")
else:
    st.write('Choose the variables values')
