import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# LOGIN PAGE
if not st.session_state.logged_in:

    st.title("🔐 AI Analytics Dashboard Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials")


# MAIN DASHBOARD
else:

    st.title("📊 AI Analytics Dashboard Suite")

    st.write("Welcome! Select a module from the sidebar.")

    # Dashboard metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Modules", 4)
    col2.metric("Dashboards", 3)
    col3.metric("AI Tools", 1)

    st.divider()

    st.subheader("Available Modules")

    st.write("""
    • **Student Performance Analytics**  
    • **AI Resume Analyzer**  
    • **Personal Finance Dashboard**  
    • **Disaster Monitoring Dashboard**
    """)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()