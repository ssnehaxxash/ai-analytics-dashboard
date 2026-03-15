import streamlit as st
import json

st.set_page_config(page_title="AI Analytics Dashboard", layout="wide")

# -----------------------------
# Load users
# -----------------------------

def load_users():
    try:
        with open("users.json","r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open("users.json","w") as f:
        json.dump(users,f)

users = load_users()

# -----------------------------
# Session state
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# -----------------------------
# Login / Signup Page
# -----------------------------

if not st.session_state.logged_in:

    st.title("Student Analytics Portal")

    menu = st.radio(
        "Select Option",
        ["Login","Sign Up"]
    )

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # LOGIN
    if menu == "Login":

        if st.button("Login"):

            if username in users and users[username] == password:

                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()

            else:
                st.error("Invalid username or password")

    # SIGNUP
    if menu == "Sign Up":

        if st.button("Create Account"):

            if username in users:
                st.error("User already exists")

            else:
                users[username] = password
                save_users(users)
                st.success("Account created! Please login.")

# -----------------------------
# Main App
# -----------------------------

else:

    st.sidebar.success(f"Logged in as {st.session_state.username}")

    st.title("AI Analytics Dashboard")

    st.write("Welcome to your analytics portal.")

    col1,col2,col3 = st.columns(3)

    col1.metric("Modules",4)
    col2.metric("Dashboards",3)
    col3.metric("AI Tools",1)

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()