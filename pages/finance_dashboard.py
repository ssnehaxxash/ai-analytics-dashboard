import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Personal Finance Dashboard")

st.write("Upload your transaction CSV file.")

uploaded_file = st.file_uploader("Upload Transactions CSV")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Transactions")
    st.dataframe(df)

    category_sum = df.groupby("Category")["Amount"].sum()

    fig = px.pie(
        values=category_sum.values,
        names=category_sum.index,
        title="Expense Distribution"
    )

    st.plotly_chart(fig)