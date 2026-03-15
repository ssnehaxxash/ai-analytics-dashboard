import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Student Performance Analytics")

# Choose input method
option = st.radio(
    "Choose Data Input Method",
    ["Upload CSV", "Enter Manually", "Use Sample Data"]
)

# -------------------------
# Upload CSV
# -------------------------

if option == "Upload CSV":

    uploaded_file = st.file_uploader("Upload student CSV", type=["csv"])

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Dataset Preview")
        st.dataframe(df)

        fig = px.bar(df, x="Student", y="Marks", color="Subject")

        st.plotly_chart(fig)


# -------------------------
# Manual Entry
# -------------------------

elif option == "Enter Manually":

    st.subheader("Enter Student Data")

    name = st.text_input("Student Name")
    subject = st.text_input("Subject")
    marks = st.number_input("Marks", 0, 100)

    if st.button("Add Data"):

        data = {
            "Student": [name],
            "Subject": [subject],
            "Marks": [marks]
        }

        df = pd.DataFrame(data)

        st.success("Data Added")

        st.dataframe(df)

        fig = px.bar(df, x="Student", y="Marks", color="Subject")

        st.plotly_chart(fig)


# -------------------------
# Sample Dataset
# -------------------------

elif option == "Use Sample Data":

    data = {
        "Student": ["Alice", "Bob", "Charlie", "David"],
        "Subject": ["Math", "Science", "Math", "Science"],
        "Marks": [85, 90, 78, 88]
    }

    df = pd.DataFrame(data)

    st.subheader("Sample Dataset")

    st.dataframe(df)

    fig = px.bar(df, x="Student", y="Marks", color="Subject")

    st.plotly_chart(fig)