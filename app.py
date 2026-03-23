import streamlit as st

# Page config
st.set_page_config(page_title="Manthan Portfolio", layout="wide")

# Custom CSS (UI upgrade)
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
            color: white;
        }
        h1, h2, h3 {
            color: #00C9A7;
        }
        .card {
            padding: 20px;
            border-radius: 10px;
            background-color: #1c1f26;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
menu = ["Home", "About", "Skills", "Projects", "Achievements", "Contact"]
choice = st.sidebar.radio("Navigation", menu)

# ---------------- HOME ----------------
if choice == "Home":
    col1, col2 = st.columns([2,1])

    with col1:
        st.title("👋 Hello, I'm Manthan Moondra")
        st.subheader("Future IFS Officer | Data Science Enthusiast")

        st.write("""
        I am a focused and disciplined engineering student working towards becoming an IFS officer.
        Alongside UPSC preparation, I am building strong technical expertise in Data Science and Cloud.
        
        My goal is to combine analytical thinking with global diplomacy to create real-world impact.
        """)

        st.markdown("### 🚀 Vision")
        st.write("""
        To represent India on the global stage with intelligence, clarity and strategic thinking.
        """)

    with col2:
        st.image("https://via.placeholder.com/200", caption="Profile")

# ---------------- ABOUT ----------------
elif choice == "About":
    st.header("About Me")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
    I am currently pursuing engineering while preparing for UPSC 2029 with PSIR as my optional subject.
    
    I follow a structured and disciplined approach towards both academics and skill development.
    I believe in consistency, clarity of thought and long-term vision.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🎯 Current Focus")
    st.write("""
    - UPSC Preparation (NCERT + Core Subjects)
    - Data Science & Machine Learning Projects
    - Cloud Computing Fundamentals
    - Personality & Communication Development
    """)

# ---------------- SKILLS ----------------
elif choice == "Skills":
    st.header("My Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💻 Technical Skills")
        st.write("Python")
        st.progress(85)

        st.write("Machine Learning")
        st.progress(75)

        st.write("Data Analysis")
        st.progress(80)

        st.write("Streamlit")
        st.progress(70)

    with col2:
        st.subheader("🧠 Core Skills")
        st.write("Critical Thinking")
        st.progress(90)

        st.write("Leadership")
        st.progress(85)

        st.write("Public Speaking")
        st.progress(80)

        st.write("Discipline")
        st.progress(95)

# ---------------- PROJECTS ----------------
elif choice == "Projects":
    st.header("Projects")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Salary Prediction App")
    st.write("""
    - Built using Machine Learning regression models  
    - Predicts salary based on multiple features  
    - Focused on data preprocessing and model optimization  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📈 Restaurant Rating Predictor")
    st.write("""
    - Developed a regression-based ML model  
    - Performed feature selection and scaling  
    - Evaluated model accuracy using metrics  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📉 Data Analysis Projects")
    st.write("""
    - Worked on multiple datasets  
    - Performed visualization and insights extraction  
    - Used Pandas, Matplotlib and NumPy  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ACHIEVEMENTS ----------------
elif choice == "Achievements":
    st.header("Achievements")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
    ✔ Completed Data Science Course with 90% score  
    ✔ Built 10+ Data Science & ML Projects  
    ✔ Active member of International Relations Club  
    ✔ Participated in technical and personality development activities  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONTACT ----------------
elif choice == "Contact":
    st.header("Contact Me")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("📧 Email: manthanmoondra0@gmail.com")
    st.write("🔗 LinkedIn: https://linkedin.com")
    st.write("💻 GitHub: https://github.com")
    st.markdown('</div>', unsafe_allow_html=True)