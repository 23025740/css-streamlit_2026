import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Undergrad Research | R. Tshivhase",
    page_icon="📚",
    layout="wide"
)


st.markdown("""
    <style>
    .main { background-color: #fdfdfd; }
    .stAlert { border-radius: 8px; }
    .stMetric { border: 1px solid #eeeeee; padding: 10px; border-radius: 5px; }
    h1, h2 { color: #1E3A8A; }
    </style>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Initialization (Default Student Data)
# --------------------------------------------------
if "education" not in st.session_state:
    st.session_state.education = [
        {"deg": "BSc in Computer Science & Mathematics (Current)", "sch": "Your University Name", "yr": "Expected 2025"}
    ]
if "projects" not in st.session_state:
    st.session_state.projects = [
        {"title": "Mobile Payment Barriers", "desc": "Analyzing why rural users prefer USSD over Apps."}
    ]

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
with st.sidebar:
    st.markdown("## 🇿🇦 Research Portfolio")
    st.image("https://img.icons8.com/fluency/96/000000/education.png", width=80)
    st.write("**Ritshidze Tshivhase**")
    st.caption("Undergraduate Researcher")
    st.divider()
    menu = st.radio("Sections", ["About Me", "Academic Journey", "STEM & Research", "Contact"])

# --------------------------------------------------
# 1. About Me
# --------------------------------------------------
if menu == "About Me":
    st.title("🎓 Computer Science Graduate")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Research Focus
        **"The Adoption and Impact of Mobile Payment Systems on Financial Inclusion in South Africa."**
        
        As an undergraduate student, I am exploring how technology can solve real-world problems. My research focuses 
        on the 'digital divide' in South Africa—specifically looking at how mobile payment systems can provide 
        financial dignity to the unbanked.
        """)
        
        st.info("💡 **Objective:** To identify the psychological and technical barriers preventing the adoption of digital wallets in local communities.")
    
    with col2:
        st.markdown("### Technical Skills")
        st.button("Python (Pandas/Streamlit)")
        st.button("Data Visualization")
        st.button("Statistical Analysis")

# --------------------------------------------------
# 2. Academic Journey
# --------------------------------------------------
elif menu == "Academic Journey":
    st.title("📚 Academic & Projects")
    
    tab1, tab2 = st.tabs(["University History", "Key Projects"])
    
    with tab1:
        st.subheader("Education")
        for edu in st.session_state.education:
            st.markdown(f"**{edu['deg']}**")
            st.caption(f"{edu['sch']} — {edu['yr']}")
            st.divider()
            
    with tab2:
        st.subheader("Research Projects")
        for p in st.session_state.projects:
            with st.expander(p['title']):
                st.write(p['desc'])

# --------------------------------------------------
# 3. STEM & Research (Visualizations)
# --------------------------------------------------
elif menu == "STEM & Research":
    st.title("📊 Research Insights")
    st.write("Current landscape of financial inclusion methods in South African Townships.")
    
    

    # Sample Data
    data = {
        "Method": ["Cash", "Mobile Banking", "Store Cards", "Digital Wallets"],
        "Usage %": [65, 40, 25, 15],
        "Perceived Security": [10, 8, 5, 4]
    }
    df = pd.DataFrame(data)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Usage Trends")
        st.bar_chart(df.set_index("Method")["Usage %"])
    
    with col2:
        st.subheader("The Trust Gap")
        st.line_chart(df.set_index("Method")["Perceived Security"])

    st.markdown("""
    ### Why this matters:
    While **Cash** is seen as high-security (because you can hold it), **Digital Wallets** face a trust barrier. 
    My research aims to bridge this gap through better UI/UX and financial literacy.
    """)

# --------------------------------------------------
# 4. Contact
# --------------------------------------------------
elif menu == "Contact":
    st.title("📬 Connect with me")
    st.write("I am always open to discussing research opportunities, internships, or data science projects.")
    
    st.markdown("""
    - **Email:** tshivhaserichie@gmail.com
    - **GitHub:** [github.com/yourusername](https://github.com)
    - **LinkedIn:** [linkedin.com/in/ritshidze-tshivhase](https://linkedin.com)
    """)
    
    if st.button("Download Research Abstract (PDF)"):
        st.write("Download link would go here!")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.caption("@2026 Tdhivhase Ritshidze Research")
