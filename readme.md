# AI Analytics Platform 📊

**Live Demo:** https://ai-analytics-dash.streamlit.app/

AI Analytics Platform is an interactive multi-user analytics dashboard designed for **student performance insights and global disaster intelligence**.
The platform allows users to securely log in, analyze data through interactive visualizations, and explore global disaster trends using modern data analytics tools.

---

## 🚀 Features

### 🔐 Authentication System

* Secure login and signup system
* Multi-user support
* Session-based authentication to protect dashboards

### 🎓 Student Performance Analytics

* Visualize student marks and academic trends
* Interactive charts for performance comparison
* Manual data entry or file upload

### 🌍 Disaster Intelligence Dashboard

* Global disaster visualization
* Interactive disaster map
* Disaster density heatmap
* Event tracking with location-based data

### 📊 Interactive Data Visualization

* Modern dashboards using interactive charts
* Real-time data updates
* Responsive layout for analytics exploration

---

## 🛠️ Tech Stack

**Frontend & Framework**

* Python
* Streamlit

**Data Visualization**

* Plotly

**Data Handling**

* Pandas

**APIs**

* USGS Earthquake API (for live disaster data)

**Deployment**

* Streamlit Community Cloud

---

## 📂 Project Structure

```
ai-analytics-dashboard
│
├── app.py                     # Main application entry point
├── pages/
│   ├── student_dashboard.py   # Student analytics module
│   └── disaster_dashboard.py  # Disaster intelligence module
│
├── users.json                 # User authentication storage
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/ssnehaxxash/ai-analytics-dashboard.git
```

Navigate to the project folder:

```
cd ai-analytics-dashboard
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

## 🌐 Deployment

The project is deployed on **Streamlit Community Cloud**.

Live application:
https://ai-analytics-dash.streamlit.app/

---

## 📈 Future Improvements

* AI-powered insights for student performance
* Disaster prediction analytics
* Real-time global disaster monitoring
* Advanced filtering and analytics dashboards
* Integration with additional disaster data APIs

---

## 👨‍💻 Author

Sneha

---

## ⭐ Acknowledgements

* Streamlit for rapid dashboard development
* Plotly for interactive visualizations
* USGS for providing open disaster data APIs
