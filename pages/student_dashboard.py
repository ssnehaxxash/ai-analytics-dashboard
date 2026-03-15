import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Student Performance Analytics")

option = st.radio(
    "Choose Data Input Method",
    ["Upload CSV", "Enter Manually", "Use Sample Data"]
)

# ----------------------------
# Upload CSV
# ----------------------------

if option == "Upload CSV":

    uploaded_file = st.file_uploader("Upload student CSV", type=["csv"])

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Dataset Preview")
        st.dataframe(df)

        fig = px.bar(df, x="Student", y="Marks", color="Subject")
        st.plotly_chart(fig)


# ----------------------------
# Manual Entry (MULTIPLE ROWS)
# ----------------------------

elif option == "Enter Manually":

    st.subheader("Enter Student Data")

    if "student_data" not in st.session_state:
        st.session_state.student_data = []

    name = st.text_input("Student Name")
    subject = st.text_input("Subject")
    marks = st.number_input("Marks", 0, 100)

    if st.button("Add Student"):

        new_row = {
            "Student": name,
            "Subject": subject,
            "Marks": marks
        }

        st.session_state.student_data.append(new_row)

    if len(st.session_state.student_data) > 0:

        df = pd.DataFrame(st.session_state.student_data)

        st.subheader("Student Dataset")
        st.dataframe(df)

        fig = px.bar(df, x="Student", y="Marks", color="Subject")
        st.plotly_chart(fig)


# ----------------------------
# Sample Data
# ----------------------------

elif option == "Use Sample Data":

    data = {
        "Student": ["Rahul", "Ananya", "Priya", "Arjun"],
        "Subject": ["Math", "Physics", "CS", "Math"],
        "Marks": [88, 91, 95, 76]
    }

    df = pd.DataFrame(data)

    st.subheader("Sample Dataset")
    st.dataframe(df)

    fig = px.bar(df, x="Student", y="Marks", color="Subject")
    st.plotly_chart(fig)