"""
pages/01_home.py - Home & Theory Section
"""

import streamlit as st
from config import APP_TITLE, APP_ICON, APP_LAYOUT
from visualization import get_css_styling


def show_home():
    """Display home page with background and theory."""
    
    st.markdown(get_css_styling(), unsafe_allow_html=True)
    
    # ═══════════════════════════════════════════════════════════════
    # HERO SECTION
    # ═══════════════════════════════════════════════════════════════
    st.markdown("""
    <div class="hero">
      <div class="hero-badge">Statistical Analysis</div>
      <h1>ANOVA Analysis Tool</h1>
      <p>Compare means across three or more groups — instantly interpret variance, significance & insights.</p>
    </div>
    """, unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # SECTION 1 — THEORY
    # ═══════════════════════════════════════════════════════════════
    st.markdown('<p class="section-title">Fundamentals of ANOVA</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="theory-card">
          <h4>📐 The Concept</h4>
          <p>ANOVA (<em>Analysis of Variance</em>) tests whether the means of <strong>3+ groups</strong>
          differ significantly — all in one test, avoiding the inflated error rate of multiple t-tests.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="theory-card">
          <h4>📊 The F-Statistic</h4>
          <p>ANOVA compares <strong>between-group variance</strong> to <strong>within-group variance</strong>:</p>
          <p style="margin-top:0.6rem; font-size:1rem; text-align:center; font-weight:600; color:#303f9f">
            F = Var(between) / Var(within)
          </p>
          <p>A large F signals the groups differ more than chance alone would predict.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="theory-card">
          <h4>🔬 Hypotheses</h4>
          <p><strong>H₀ (Null):</strong> All group means are equal — μ₁ = μ₂ = … = μₖ</p>
          <br>
          <p><strong>H₁ (Alternative):</strong> At least one group mean differs from the rest.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top:1rem"></div>', unsafe_allow_html=True)

    st.markdown("""
    <p style="font-size:0.8rem;font-weight:600;color:#7986cb;letter-spacing:2px;margin-bottom:0.5rem">
    ASSUMPTIONS
    </p>
    <div class="pill-row">
      <span class="pill">✅ Independence of observations</span>
      <span class="pill">✅ Approximate normality per group</span>
      <span class="pill">✅ Homogeneity of variance</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # USE CASES
    # ═══════════════════════════════════════════════════════════════
    st.markdown('<p class="section-title">Real-World Applications</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="use-case-card">
          <h4>🔬 Research Studies</h4>
          <p>Compare treatment effectiveness across multiple groups in clinical trials, drug studies, or behavioral experiments.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="use-case-card">
          <h4>📈 Business Analytics</h4>
          <p>Analyze performance differences across regions, product lines, or marketing campaigns to optimize strategy.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="use-case-card">
          <h4>📈 Operations Research</h4>
          <p>Optimize manufacturing processes and quality control by comparing variance across different production methods.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div style="margin-top:3rem"></div>', unsafe_allow_html=True)
    
    # ═══════════════════════════════════════════════════════════════
    # FEATURES SECTION
    # ═══════════════════════════════════════════════════════════════
    st.markdown('<p class="section-title">Key Features</p>', unsafe_allow_html=True)
    
    # Create responsive feature cards
    features = [
        {
            "icon": "⚡",
            "title": "Fast Analysis",
            "description": "Run ANOVA analysis instantly with real-time results and interpretation"
        },
        {
            "icon": "📊",
            "title": "Multiple Visualizations",
            "description": "5 different chart types to understand your data from multiple angles"
        },
        {
            "icon": "📈",
            "title": "Detailed Reports",
            "description": "Export comprehensive PDF and text reports for documentation"
        },
        {
            "icon": "🔬",
            "title": "Statistical Tests",
            "description": "Levene's test, effect size calculation, and assumption checking included"
        },
        {
            "icon": "📚",
            "title": "Built-in Guide",
            "description": "Learn ANOVA concepts while analyzing with integrated educational content"
        },
        {
            "icon": "📱",
            "title": "Mobile Friendly",
            "description": "Fully responsive design that works seamlessly on all devices"
        }
    ]
    
    # Display features in responsive grid
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    
    for idx, feature in enumerate(features):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="theory-card" style="text-align: center; padding: 1.5rem; min-height: 240px; display: flex; flex-direction: column; justify-content: center;">
              <div style="font-size: clamp(2rem, 5vw, 3rem); margin-bottom: 0.8rem;">{feature['icon']}</div>
              <h4 style="text-align: center; margin-bottom: 0.8rem;">{feature['title']}</h4>
              <p style="text-align: center; flex-grow: 1; display: flex; align-items: center; justify-content: center;">{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('<div style="margin-top:2rem"></div>', unsafe_allow_html=True)
    st.divider()
    st.markdown("---")
    
    st.markdown("""
            <div style='text-align: center; color: #999; font-size: 0.85rem;'>
            <p>@2026 ANOVA Analysis Tool</p>
            </div>
            """, unsafe_allow_html=True)
