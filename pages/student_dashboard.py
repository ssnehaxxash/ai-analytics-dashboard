import streamlit as st

# Protect page from unauthorized access
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login to access this page.")
    st.stop()
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📊 Student Performance Analytics")

username = st.session_state.get("username")

user_file = f"user_data/{username}.csv"

option = st.radio(
    "Choose Data Input Method",
    ["Upload CSV", "Enter Manually"]
)

# -------------------------
# Upload CSV
# -------------------------

if option == "Upload CSV":

    uploaded_file = st.file_uploader("Upload student CSV", type=["csv"])

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        df.to_csv(user_file, index=False)

        st.success("File uploaded to your account")

# -------------------------
# Manual Entry
# -------------------------

elif option == "Enter Manually":

    st.subheader("Add Student")

    name = st.text_input("Student Name")
    subject = st.text_input("Subject")
    marks = st.number_input("Marks", 0, 100)

    if st.button("Add Student"):

        new_row = {
            "Student": name,
            "Subject": subject,
            "Marks": marks
        }

        if os.path.exists(user_file):

            df = pd.read_csv(user_file)

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        else:

            df = pd.DataFrame([new_row])

        df.to_csv(user_file, index=False)

        st.success("Student added")

# -------------------------
# Display Data
# -------------------------

if os.path.exists(user_file):

    df = pd.read_csv(user_file)

    st.subheader("Your Dataset")

    st.dataframe(df)

    fig = px.bar(df, x="Student", y="Marks", color="Subject")

    st.plotly_chart(fig)