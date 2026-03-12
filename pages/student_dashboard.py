import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Student Performance Analytics")

uploaded_file = st.file_uploader("Upload student marks CSV")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    st.subheader("Average Marks")

    averages = df[["Math","Physics","CS"]].mean()

    fig = px.bar(
        x=averages.index,
        y=averages.values,
        labels={"x":"Subject","y":"Average Marks"},
        title="Average Marks Per Subject"
    )

    st.plotly_chart(fig)

    st.subheader("Student Comparison")

    fig2 = px.bar(
        df,
        x="Student",
        y=["Math","Physics","CS"],
        barmode="group"
    )

    st.plotly_chart(fig2)