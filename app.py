import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv("data/Salary_Data.csv")
x = np.array(data["YearsExperience"]).reshape(-1,1)

lr = LinearRegression()
lr.fit(x,np.array(data["Salary"]))

st.title("Salary Predictor")

nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])

if nav=="Home":
    st.image("data/sal.jpg", width = 1000)

    if st.checkbox("Show Table"):
        st.table(data)

    graph = st.selectbox("What type of graph?",["Non-Interactive","Interactive"])
    

    years = st.slider("Number of Years", min_value= 0,max_value = 16,step = 1, value = 5)
    data = data.loc[data["YearsExperience"]>=years]
    if graph == "Non-Interactive":
        fig,x = plt.subplots(figsize = (10,5))
        
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.tight_layout()
        st.pyplot(fig)

    if graph == "Interactive":
        
        layout =go.Layout(
            xaxis = dict(range=[0,14]),
            yaxis = dict(range =[0,210000])
        )
        fig = go.Figure(data=go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode='markers'),layout = layout)
        st.plotly_chart(fig)
    


if nav == "Prediction":
    st.header("Know Your Salary")
    val = st.number_input("Enter Your Exp",0.00,20.00,step = 0.25)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your predicted salary is {round(pred)}")



if nav == "Contribute":
    st.header("Enter your Years of Experience and salary")
    exp,sal = st.columns(2)
    experience = exp.number_input("Enter Your Exp", 0.00,20.00,step = 0.25)
    salary = sal.number_input("Salary",0.00,1000000.00,step = 500.00)

    btn = st.button("Submit")

    if btn:
        to_add = {"YearsExperience": [experience],"Salary": [salary]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("data//Salary_Data.csv", mode = 'a', header = False,index = False)
        st.success("Submitted")
    

