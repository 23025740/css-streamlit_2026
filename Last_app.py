import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Researcher Portfolio | R. Tshivhase",
    page_icon="🔬",
    layout="wide"
)

# Professional Styling
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #f0f2f6; border-radius: 4px 4px 0px 0px; gap: 1px; }
    .stTabs [aria-selected="true"] { background-color: #1E3A8A; color: white; }
    .researcher-card { background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 5px solid #1E3A8A; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Data & Projects
# --------------------------------------------------
projects = [
    {
        "title": "📱 Adoption Barriers in Rural Limpopo",
        "description": "A quantitative study investigating why USSD-based banking remains more prevalent than app-based mobile wallets in low-connectivity areas.",
        "outcome": "Identified 'Data Cost' and 'Network Latency' as the primary deterrents for 70% of surveyed participants."
    },
    {
        "title": "🔒 Trust & Security Perception in Digital Payments",
        "description": "Evaluating the psychological gap between physical cash security and digital encryption among elderly populations in South African townships.",
        "outcome": "Developed a set of UI/UX recommendations for fintech developers to increase visual trust cues."
    },
    {
        "title": "📉 Comparative Analysis: SARB Vision 2025 vs. Reality",
        "description": "A policy-focused project tracking the progress of South African Reserve Bank's financial inclusion goals through public data.",
        "outcome": "Found a 15% lag in digital payment penetration compared to initial 2020 projections due to informal economy reliance."
    }
]

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:
    st.title("Navigation")
    menu = st.radio("Select Section", ["Researcher Profile", "Portfolio", "STEM DATA EXPLORER", "Contact"])
    st.divider()
    st.caption("Current Year: 2026")

# --------------------------------------------------
# 1. Researcher Profile
# --------------------------------------------------
if menu == "Researcher Profile":
    st.header("🔬 Researcher Profile")
    
    with st.container():
        st.markdown("""
        <div class="researcher-card">
            <h3>Ritshidze Tshivhase</h3>
            <p><strong>Primary Research Area:</strong> Financial Inclusion & Digital Payment Ecosystems</p>
            <p><strong>Affiliation:</strong> Undergraduate Scholar | Data Science & AI</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Research Summary")
        st.write("""
        My research focuses on the intersection of technology and socio-economic development. 
        I investigate the mechanics of **Mobile Payment Systems** and their efficacy in 
        reducing financial exclusion in South Africa. By analyzing user behavior and 
        systemic barriers, I aim to contribute to a more inclusive digital economy.
        """)
    
    with col2:
        st.subheader("Core Competencies")
        st.write("- **Methodology:** Quantitative Surveys, Comparative Policy Analysis")
        st.write("- **Technical:** Data Cleaning (Pandas), Visualization (Streamlit, Matplotlib)")
        st.write("- **Context:** Emerging Markets, Fintech Adoption, SARB Regulations")

# --------------------------------------------------
# 2. Research Portfolio (Multiple Projects)
# --------------------------------------------------
elif menu == "Research Portfolio":
    st.header("📂 Research Portfolio")
    st.write("Current and completed academic projects focusing on the South African fintech landscape.")
    
    for p in projects:
        with st.expander(p["title"], expanded=True):
            st.markdown(f"**Objective:** {p['description']}")
            st.markdown(f"✅ **Key Outcome:** {p['outcome']}")
            st.button("View Abstract", key=p["title"])

# --------------------------------------------------
# 3. Data Insights
# --------------------------------------------------
elif menu == "Data Insights":
    st.header("📊 STEM Explorer: Market Dynamics")
    
    # Diagram of the mobile payment ecosystem
    
    
    st.write("### Demographic Split of Payment Methods")
    
    # Sample Data for undergraduate level research
    data = {
        "Age Group": ["18-25", "26-40", "41-60", "60+"],
        "Banking App (%)": [85, 60, 30, 10],
        "Cash Only (%)": [5, 20, 50, 85],
        "USSD/Mobile Wallet (%)": [10, 20, 20, 5]
    }
    df = pd.DataFrame(data)
    
    st.line_chart(df.set_index("Age Group"))
    
    st.info("""
    **Observation:** There is a significant 'Age Cliff' in digital adoption. 
    Research suggests that mobile payment systems must simplify the UI to capture the 41-60 demographic.
    """)

# --------------------------------------------------
# 4. Contact
# --------------------------------------------------
elif menu == "Contact":
    st.header("📬 Contact Information")
    st.markdown("""
    For academic collaboration, data sharing, or research inquiries:
    
    - **Email:** tshivhaserichie@gmail.com
    - **Institutional Email:** [Your University Email]
    - **ResearchGate:** [Link to Profile]
    """)
