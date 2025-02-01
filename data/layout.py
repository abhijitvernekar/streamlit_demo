import streamlit as st 



st.title("Registration Form")



col1 , col2 = st.columns(2)

col1.text_input("First Name",value = "first name")
col2.text_input("Last Name",value = "last name")

email,mob = st.columns([3,1])

email.text_input("Email id")
mob.text_input("Mobile")


user,pw,pw2 = st.columns(3)

user.text_input("Username")

pw.text_input("Password", type = "password")
pw2.text_input("Retype Password", type ="password")

ck,bl,sub = st.columns(3)

ck.checkbox("I agree")
sub.button("Submit")