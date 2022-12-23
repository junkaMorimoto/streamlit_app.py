#importing required libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#creating a sample array
a = np.random.normal(1, 1, size=50)

#specifying the figure to plot 
fig, x = plt.subplots()
x.hist(a, bins=10)

#plotting the figure
st.pyplot(fig)