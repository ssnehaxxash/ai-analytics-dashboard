import streamlit as st

st.set_page_config(page_title="AI Analytics Dashboard", layout="wide")

# simple login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# login page
if not st.session_state.logged_in:

    st.title("AI Analytics Dashboard Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials")

# main app
else:

    st.title("AI Analytics Dashboard Suite")

    st.write("Select a module from the sidebar.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()