"""
pages/about.py - About & Documentation Section
"""

import streamlit as st


def show_about():
    """Display about page with documentation."""
    
    st.markdown('<p class="section-label">Documentation</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">ANOVA Analysis Tool Reference</p>', unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # PROJECT OVERVIEW
    # ═══════════════════════════════════════════════════════════════
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 📊 Project Overview
        
        **ANOVA Analysis Tool** is a modern web application built with Streamlit 
        for performing **One-Way Analysis of Variance (ANOVA)** statistical tests.
        
        This tool enables researchers, data analysts, and students to:
        - Compare means across multiple groups efficiently
        - Generate comprehensive statistical reports
        - Visualize data distributions interactively
        - Export results in multiple formats (PDF, TXT)
        - Learn ANOVA concepts with built-in theory
        """)
    
    with col2:
        st.markdown("""
        ### 📋 Quick Facts
        
        - **Framework:** Streamlit
        - **Language:** Python 3.8+
        - **License:** Open Source
        - **Version:** 1.0.0
        - **Status:** Production Ready
        """)

    st.divider()

    # ═══════════════════════════════════════════════════════════════
    # TECHNICAL DETAILS
    # ═══════════════════════════════════════════════════════════════
    st.markdown("### 🔧 Technical Architecture")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### Core Libraries
        - **NumPy** - Numerical computing
        - **SciPy** - Statistical functions
        - **Matplotlib** - Data visualization
        - **Seaborn** - Statistical plots
        """)
    
    with col2:
        st.markdown("""
        #### Project Structure
        - `config/` - Configuration constants
        - `utils/` - Statistical utilities
        - `visualization/` - Chart generation
        - `data/` - Sample datasets
        - `pages/` - UI sections
        - `components/` - Reusable components
        """)
    
    with col3:
        st.markdown("""
        #### Features
        - Modular architecture
        - Advanced navbar navigation
        - Real-time visualization
        - PDF report generation
        - Responsive design
        - Error handling
        """)

    st.divider()

    # ═══════════════════════════════════════════════════════════════
    # ANOVA METHODOLOGY
    # ═══════════════════════════════════════════════════════════════
    st.markdown("### 📚 ANOVA Methodology")
    
    with st.expander("**Null Hypothesis (H₀)**", expanded=True):
        st.markdown("""
        All group means are equal:
        
        **H₀: μ₁ = μ₂ = ... = μₖ**
        
        This is the default assumption - we assume no real difference between groups
        until statistical evidence proves otherwise.
        """)
    
    with st.expander("**Alternative Hypothesis (H₁)**"):
        st.markdown("""
        At least one group mean differs:
        
        **H₁: ¬(μ₁ = μ₂ = ... = μₖ)**
        
        At least one group has a different mean. This is what we're testing for.
        """)
    
    with st.expander("**F-Statistic Calculation**"):
        st.markdown("""
        The F-statistic is the ratio of variances:
        
        **F = MS_between / MS_within**
        
        Where:
        - **MS_between** = Mean square between groups (between-group variance)
        - **MS_within** = Mean square within groups (within-group variance)
        
        **Interpretation:**
        - Large F → Groups differ significantly
        - Small F → Groups are similar
        """)
    
    with st.expander("**P-Value Interpretation**"):
        st.markdown("""
        The p-value represents the probability of observing your data if H₀ is true.
        
        - **p < α (0.05):** Reject H₀ → Significant difference exists
        - **p ≥ α (0.05):** Fail to reject H₀ → No significant difference
        
        **Example:** p = 0.02 means there's only a 2% chance of this data 
        if groups actually have equal means.
        """)
    
    with st.expander("**Assumptions**"):
        st.markdown("""
        ANOVA has three key assumptions:
        
        1. **Independence:** Observations are independent within and between groups
        2. **Normality:** Data in each group is approximately normally distributed
        3. **Homogeneity of Variance:** Groups have roughly equal variances
        
        **Tools used:**
        - Levene's Test → Checks assumption #3
        - Shapiro-Wilk → Checks assumption #2 (optional)
        - Q-Q plots → Visual normality check
        """)

    st.divider()

    # ═══════════════════════════════════════════════════════════════
    # HOW TO USE
    # ═══════════════════════════════════════════════════════════════
    st.markdown("### 🚀 How to Use This Tool")
    
    st.markdown("""
    #### Step 1: Home (📚 Home & Theory)
    - Learn ANOVA fundamentals
    - Understand hypotheses and assumptions
    - Explore use cases in different domains
    
    #### Step 2: Analysis (📊 Analysis)
    - Configure significance level (α)
    - Select number of groups (2-6)
    - Enter data for each group (comma-separated)
    - Or load a pre-built sample dataset
    - Click "Run ANOVA Analysis"
    
    #### Step 3: Results (📈 Results)
    - Review key metrics (F-statistic, p-value)
    - Visualize distributions with 5 chart types
    - Check assumption tests (Levene's)
    - Review effect size (Eta-squared)
    - Export results as PDF or TXT
    """)

    st.divider()

    # ═══════════════════════════════════════════════════════════════
    # FAQ
    # ═══════════════════════════════════════════════════════════════
    st.markdown("### ❓ Frequently Asked Questions")
    
    with st.expander("**What's the difference between t-test and ANOVA?**"):
        st.markdown("""
        - **t-test:** Compares means of 2 groups only
        - **ANOVA:** Compares means of 3 or more groups
        
        ANOVA avoids the "multiple comparisons problem" - inflated error rate 
        when doing many t-tests.
        """)
    
    with st.expander("**How many groups can I compare?**"):
        st.markdown("""
        This tool supports 2-6 groups. Theoretically, ANOVA can handle any number,
        but practical analysis typically uses 2-10 groups.
        """)
    
    with st.expander("**What sample size do I need?**"):
        st.markdown("""
        General guidelines:
        - **Minimum:** 2-3 observations per group
        - **Recommended:** 10-30+ observations per group
        - **Larger samples** increase statistical power
        
        Use the sample size calculator tool for specific requirements.
        """)
    
    with st.expander("**Can I use ANOVA for non-normal data?**"):
        st.markdown("""
        ANOVA is **robust** to moderate violations of normality, especially 
        with larger sample sizes (n > 30).
        
        For severely non-normal data:
        - Use Kruskal-Wallis test (non-parametric alternative)
        - Transform data (log, square root, etc.)
        - Use Welch's ANOVA (robust variant)
        """)

    st.divider()

    # ═══════════════════════════════════════════════════════════════
    # CONTACT & CREDITS
    # ═══════════════════════════════════════════════════════════════
    st.markdown("### 📞 Contact & Support")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 👥 Development Team
        **Engineering Mathematics-4**  
        Project Group 12  
        
        Modular architecture with  
        clean code principles
        """)
    
    with col2:
        st.markdown("""
        #### 📚 Learning Resources
        - [ANOVA on Wikipedia](https://en.wikipedia.org/wiki/Analysis_of_variance)
        - [Statistics textbooks](https://www.statsoft.com/textbook)
        - [SciPy Documentation](https://docs.scipy.org/)
        """)
    
    with col3:
        st.markdown("""
        #### 🔗 Technologies
        - Streamlit
        - NumPy & SciPy
        - Matplotlib & Seaborn
        - ReportLab
        """)

    st.divider()
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #999; font-size: 0.85rem;'>
    <p>@2026 ANOVA Analysis Tool</p>

    </div>
    """, unsafe_allow_html=True)
