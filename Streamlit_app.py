import numpy as np
import streamlit as st
import matplotlib.pylab as plt

st.title("Simulation[tm]")
st.write("Here is our super important simulation")

x = st.slider('Slope', min_value=0.01, max_value=0.10, step=0.01)
y = st.slider('Noise', min_value=0.01, max_value=0.10, step=0.01)

st.write(f"x={x} y={y}")
values = np.cumprod(1 + np.random.normal(x, y, (100, 10)), axis=0)

for i in range(values.shape[1]):
    plt.plot(values[:, i])

st.pyplot()