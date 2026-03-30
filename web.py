import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

# Header
st.title("Manthan Moondra")
st.subheader("Data Science | Analytics | Problem Solving")

# Sidebar
menu = ["Home", "About", "Skills", "Projects", "Achievements", "Contact"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---------------- HOME ----------------
if choice == "Home":
    st.header("Welcome")
    st.write("""
    This portfolio presents my work, technical skills, and projects in the field of 
    data science and analytics.

    I focus on building practical solutions, analyzing data effectively, and 
    continuously improving my technical capabilities.
    """)

# ---------------- ABOUT ----------------
elif choice == "About":
    st.header("About Me")
    st.write("""
    I am an engineering student with strong interest in data science and analytics.
    I enjoy solving real-world problems using data-driven approaches.

    My focus is on developing practical skills through projects and understanding 
    concepts deeply to build efficient solutions.
    """)

# ---------------- SKILLS ----------------
elif choice == "Skills":
    st.header("Technical Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Programming")
        st.write("- Python")

        st.subheader("Data Analysis")
        st.write("- Pandas, NumPy")
        st.write("- Data Cleaning")

    with col2:
        st.subheader("Visualization")
        st.write("- Power BI")
        st.write("- Tableau")

        st.subheader("Machine Learning")
        st.write("- Regression")
        st.write("- Classification")

# ---------------- PROJECTS ----------------
elif choice == "Projects":
    st.header("Projects")

    st.subheader("Insurance Claim Prediction")
    st.write("""
    Built a machine learning model to predict insurance claim amounts using 
    real-world datasets. Applied preprocessing, feature engineering, and model evaluation.
    """)

    st.subheader("Data Dashboard")
    st.write("""
    Designed an interactive dashboard using Power BI to visualize business insights 
    and KPIs with filters and charts.
    """)

    st.subheader("ML Project Collection")
    st.write("""
    Developed multiple machine learning projects covering regression and classification problems.
    """)

# ---------------- ACHIEVEMENTS ----------------
elif choice == "Achievements":
    st.header("Achievements & Certifications")

    st.subheader("Certifications")

    col1, col2 = st.columns(2)

    with col1:
        st.image("powerbi.png", caption="Power BI certificate", use_container_width=True)

    with col2:
        st.image("SQL.png", caption="SQL Certificate", use_container_width=True)

    st.subheader("Achievements")
    st.write("""
    - Completed multiple data science projects  
    - Strong foundation in analytics and machine learning  
    - Hands-on experience with real datasets  
    """)

# ---------------- CONTACT ----------------
elif choice == "Contact":
    st.header("Contact")

    st.write("Email: manthanmoondra0@gmail.com.com")
    st.write("LinkedIn: linkedin.com/in/yourprofile")
    st.write("GitHub: github.com/yourusername")

# Footer
st.markdown("---")
st.markdown("© 2026 Manthan Moondra")