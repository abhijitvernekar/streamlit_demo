import streamlit as st

st.title("Widgets")

btn = st.button("Subscribe")

if btn:
    st.write("Thank you for subscribing")



name = st.text_input("Name")

st.write(name)

address = st.text_area("Enter the address")

st.write(address)

st.date_input("Enter a date")
st.time_input("Enter a time")

if st.checkbox("You accept T&C", value = False):
    st.write("Thank you")

s1 = st.radio("Colors",['r','g','b'], index=1)

s2 = st.selectbox("Colors",['r','g','b'], index=1)

s3 = st.multiselect("Colors",['r','g','b'])

st.write(s1,s2,s3)

st.slider("age",min_value = 18,max_value = 60,value = 30,step=2)

st.number_input("Number",min_value = 18,max_value = 60,value = 30,step=2)

st.file_uploader("upload a file")