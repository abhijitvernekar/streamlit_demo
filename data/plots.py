import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.DataFrame(
    np.random.randn(100,3),
    columns = ['a','b','c']
)

city = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})

st.dataframe(data)
st.line_chart(data, width = 500,height = 500)

st.area_chart(data)

st.bar_chart(data)

fig,ax = plt.subplots()
plt.scatter(data['a'],data['b'])
plt.title("Scatter")
st.pyplot(fig)

st.map(city)
st.image("data//lavasa.jpg")

st.video("https://www.youtube.com/watch?v=jq0lKFb-P8k&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5&index=4")