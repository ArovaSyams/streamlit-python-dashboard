import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ====== WRITE ======
st.write(
    """
    # My First App
    Hello calon praktisi masa depan
    """
)

st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

# ====== TEXT ======

# markdown()
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

# title()
st.title("Belajar Analysis Data")

# header()
st.header("Pengembangan Dashboard")

# subheader()
st.subheader("Pengembangan Dashboard")

# caption()
st.caption("Copiright (c) 2023")

# code()
code = """
    def hello()
        print("Hello World")
"""
st.code(code, language="python")

# text()
st.text("Hallo Calon Praktisi Data")

# latex() : to show matematics expression
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

# ====== DATA DISPLAY ======

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

# dataframe()
st.dataframe(data=df, width=500, height=150)

# table()
st.table(data=df)

# metric()
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

# json()
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

# ====== CHART =======

x = np.random.normal(15, 5, 250)

# pyplot()
fig, ax = plt.subplots(figsize=(10,5))
ax.hist(x=x, bins=15)
st.pyplot(fig)

