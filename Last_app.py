# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 04:52:23 2026

@author: tshiv
"""

import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Research Portfolio | Ritshidze Tshivhase",
    page_icon="🇿🇦",
    layout="wide"
)

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Initialization
# --------------------------------------------------
if "education" not in st.session_state:
    st.session_state.education = [{"deg": "Data Science Specialization", "sch": "University of South Africa", "yr": "2023"}]
if "experience" not in st.session_state:
    st.session_state.experience = [{"role": "Researcher", "org": "Fintech Lab", "dur": "2022 - Present"}]

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/test-account.png", width=100)
    st.title("Ritshidze Tshivhase")
    st.info("📍 South Africa | Data Science & AI")
    st.divider()
    menu = st.radio(
        "Navigation",
        ["Home & Profile", "Academic & Professional", "Research Deep-Dive", "Contact"],
        index=0
    )

# --------------------------------------------------
# 1. Home & Profile
# --------------------------------------------------
if menu == "Home & Profile":
    st.title("👤 Researcher Profile")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("The Research Mission")
        st.markdown(f"""
        > **Topic:** The Adoption and Impact of Mobile Payment Systems on Financial Inclusion in South Africa.
        
        My work explores the intersection of **Fintech and Socio-economics**, specifically focusing on how 
        digital wallets can bridge the gap for the unbanked populations in South African townships and rural areas.
        """)
        
        with st.expander("Read Bio"):
            st.write("Specializing in how digital wallets bridge the gap for the unbanked in SA. "
                     "Leveraging data science to predict adoption barriers and policy impact.")

    with col2:
        st.markdown("### Quick Stats")
        st.metric(label="Current Focus", value="Mobile Payments")
        st.metric(label="Region", value="South Africa (Gauteng/Limpopo)")

    st.divider()
    st.subheader("🔬 Research Interests")
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    row1_col1.info("**Fintech Acceptance**\n\nShifting from cash-heavy habits to digital.")
    row1_col2.info("**Last-Mile Delivery**\n\nReaching rural communities effectively.")
    row1_col3.info("**Policy Impact**\n\nEvaluating SARB's Vision 2025.")

# --------------------------------------------------
# 2. Academic & Professional
# --------------------------------------------------
elif menu == "Academic & Professional":
    tab1, tab2 = st.tabs(["🎓 Education", "💼 Experience"])

    with tab1:
        st.header("Education")
        with st.expander("➕ Add New Record"):
            with st.form("edu_form"):
                deg = st.text_input("Degree")
                sch = st.text_input("University")
                yr = st.text_input("Year")
                if st.form_submit_button("Save"):
                    st.session_state.education.append({"deg": deg, "sch": sch, "yr": yr})
        
        for edu in reversed(st.session_state.education):
            st.markdown(f"#### {edu['deg']}")
            st.caption(f"{edu['sch']} | {edu['yr']}")
            st.divider()

    with tab2:
        st.header("Professional Timeline")
        with st.expander("➕ Add New Experience"):
            with st.form("exp_form"):
                role = st.text_input("Role")
                org = st.text_input("Organization")
                dur = st.text_input("Duration")
                if st.form_submit_button("Save"):
                    st.session_state.experience.append({"role": role, "org": org, "dur": dur})

        for exp in reversed(st.session_state.experience):
            st.markdown(f"#### {exp['role']}")
            st.markdown(f"**{exp['org']}** — *{exp['dur']}*")
            st.divider()

# --------------------------------------------------
# 3. Research Deep-Dive (STEM Explorer)
# --------------------------------------------------
elif menu == "Research Deep-Dive":
    st.title("📊 Financial Inclusion Data Explorer")
    st.write("This section visualizes the current landscape of payment methods in South Africa.")

    # 
    
    data = {
        "Method": ["Banking App", "Mobile Wallet", "USSD Payments", "Cash"],
        "Adoption Rate (%)": [45, 30, 15, 60],
        "Trust Score (1-10)": [8, 6, 7, 10]
    }
    df = pd.DataFrame(data)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.write("### Payment Method Adoption")
        st.bar_chart(df.set_index("Method")["Adoption Rate (%)"], color="#2E86C1")

    with col2:
        st.write("### Raw Data")
        st.dataframe(df, use_container_width=True)
        
    st.warning("⚠️ **Insight:** While digital adoption is rising, **Cash** remains the primary method due to trust and immediate liquidity.")

# --------------------------------------------------
# 4. Contact
# --------------------------------------------------
elif menu == "Contact":
    st.title("📬 Get In Touch")
    
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        st.write("Feel free to reach out for collaborations or data inquiries.")
        st.write("📧 **Email:** tshivhaserichie@gmail.com")
        st.write("🔗 **LinkedIn:** [linkedin.com/in/ritshidze-tshivhase](#)")
    
    with contact_col2:
        with st.form("contact"):
            name = st.text_input("Name")
            msg = st.text_area("Message")
            if st.form_submit_button("Send Message"):
                st.success("Message sent successfully (Simulation)")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.caption("© 2024 Ritshidze Tshivhase Portfolio")