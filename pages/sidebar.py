import streamlit as st
import pandas as pd # pip install pandas
from matplotlib import pyplot as plt # pip install matplotlib
import time

plt.style.use("ggplot")

data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}

df = pd.DataFrame(data)

rad = st.sidebar.radio("Navigation",["Home","About Us"])

if rad == "Home":

    col = st.sidebar.multiselect("Select a column",df.columns[1:])

    fig,ax = plt.subplots()

    plt.plot(df['num'],df[col])
    st.pyplot(fig)

if rad == "About Us":
    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+5)
    st.balloons()

    st.write("Welcome to about us sections")
    st.success("Success")
    st.error("This is a error")
    st.warning("This is an warning")
    st.exception(RuntimeError("Exception"))
    st.info("info")