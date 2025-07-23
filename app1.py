import streamlit as st
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

st.sidebar.write("Type of Analysis")
selected_option=st.sidebar.radio("Select any option", options=("Line Graph","Bar Graph","Area Chart"))

data = pd.DataFrame(np.random.randn(50,2), columns=['Age','BMI'])
    
if selected_option == "Line Graph":
    st.write("Line Graph")
    st.line_chart(data)

elif selected_option == "Bar Graph":
    st.write("Bar Graph")
    st.bar_chart(data)

else:
    st.write("Area Chart")
    st.area_chart(data)