import streamlit as st
import json

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------

st.set_page_config(
    page_title="AI Analytics Platform",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------
# Custom UI Styling
# ------------------------------------------------

st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#1f2937,#111827);
color:white;
}

/* Sidebar */
[data-testid="stSidebar"]{
background:#0f172a;
}

/* Metric cards */
[data-testid="stMetric"]{
background: rgba(255,255,255,0.05);
padding:15px;
border-radius:15px;
border:1px solid rgba(255,255,255,0.1);
}

/* Buttons */
.stButton>button{
background:linear-gradient(45deg,#6366f1,#3b82f6);
color:white;
border:none;
border-radius:10px;
padding:8px 20px;
}

.stButton>button:hover{
background:linear-gradient(45deg,#7c3aed,#2563eb);
}

/* Info cards */
.card{
padding:20px;
border-radius:15px;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# User Storage
# ------------------------------------------------

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

# ------------------------------------------------
# Session State
# ------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ------------------------------------------------
# AUTHENTICATION PAGE
# ------------------------------------------------

if not st.session_state.logged_in:

    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {display:none;}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <h1 style='text-align:center;font-size:48px'>
    🚀 AI Analytics Platform
    </h1>

    <p style='text-align:center;font-size:20px;color:#9ca3af'>
    Interactive dashboards for student analytics and global disaster intelligence
    </p>
    """, unsafe_allow_html=True)

    menu = st.radio("Select Option", ["Login", "Sign Up"])

    username = st.text_input("Username")

    if menu == "Login":

        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if username in users and users[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()

            else:
                st.error("Invalid username or password")

    elif menu == "Sign Up":

        password = st.text_input("Create Password", type="password")

        if st.button("Create Account"):

            if username in users:
                st.error("User already exists")

            else:
                users[username] = password
                save_users(users)
                st.success("Account created! Please login.")

# ------------------------------------------------
# MAIN DASHBOARD
# ------------------------------------------------

else:

    # Sidebar
    st.sidebar.title("AI Analytics Platform")
    st.sidebar.success(f"Logged in as {st.session_state.username}")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Navigation")
    st.sidebar.write("Use the sidebar to access dashboards.")
    st.sidebar.markdown("---")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.sidebar.caption("Built using Streamlit")

    # ------------------------------------------------
    # Dashboard UI
    # ------------------------------------------------

    st.markdown("""
    <h1 style='text-align:center;font-size:48px'>
    📊 AI Analytics Platform
    </h1>

    <p style='text-align:center;font-size:20px;color:#9ca3af'>
    Intelligent data dashboards for students and global analytics
    </p>
    """, unsafe_allow_html=True)

    st.divider()

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📦 Modules", "4")
    col2.metric("📊 Dashboards", "3")
    col3.metric("🤖 AI Tools", "1")
    col4.metric("👥 Users", "Multi-user")

    st.divider()

    # Modules
    st.subheader("Platform Modules")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card" style="background:linear-gradient(135deg,#6366f1,#3b82f6)">
        <h3>🎓 Student Performance Analytics</h3>
        <p>Track marks, analyze performance trends and visualize academic insights.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card" style="background:linear-gradient(135deg,#ef4444,#f97316)">
        <h3>🌍 Disaster Intelligence Dashboard</h3>
        <p>Monitor global disasters with analytics and interactive maps.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.success("Use the sidebar to open analytics dashboards.")