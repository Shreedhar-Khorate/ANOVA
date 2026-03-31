"""
pages/02_analysis.py - Configuration & Data Input Section
"""

import streamlit as st
import numpy as np
from config import (
    DEFAULT_ALPHA, MIN_ALPHA, MAX_ALPHA, ALPHA_STEP,
    MIN_GROUPS, MAX_GROUPS, DEFAULT_GROUPS,
)
from utils import parse_input, run_anova
from data.sample_datasets import get_dataset_names, load_sample_dataset


def show_analysis():
    """Display analysis configuration and input section."""
    
    # ═══════════════════════════════════════════════════════════════
    # SETTINGS + INPUT
    # ═══════════════════════════════════════════════════════════════
    st.markdown('<p class="section-title">Analysis Configuration</p>', unsafe_allow_html=True)

    # Create responsive settings section
    settings_cols = st.columns([1, 1])
    with settings_cols[0]:
        alpha = st.slider("Significance level (α)", MIN_ALPHA, MAX_ALPHA, DEFAULT_ALPHA, ALPHA_STEP,
                          help="Threshold for rejecting H₀. Common choice: 0.05")
    with settings_cols[1]:
        num_groups = st.slider("Number of groups", MIN_GROUPS, MAX_GROUPS, DEFAULT_GROUPS,
                               help="How many groups you want to compare")
    
    sample_choice = st.selectbox(
        "Load sample dataset",
        ["— Choose a sample —"] + get_dataset_names(),
        help="Auto-fills the group inputs below"
    )

    # Load sample into session state
    if sample_choice != "— Choose a sample —":
        sample = load_sample_dataset(sample_choice)
        sample_keys = list(sample.keys())
        for i in range(min(len(sample_keys), num_groups)):
            st.session_state[f"gn_{i}"] = sample_keys[i]
            st.session_state[f"gd_{i}"] = ", ".join(str(v) for v in sample[sample_keys[i]])

    st.markdown('<div style="margin-top:1rem"></div>', unsafe_allow_html=True)

    # Collect group data from user input
    group_data = {}
    all_valid = True

    cols = st.columns(min(num_groups, 3))
    for i in range(num_groups):
        with cols[i % 3]:
            with st.container(border=True):
                default_name = st.session_state.get(f"gn_{i}", f"Group {i + 1}")
                default_data = st.session_state.get(f"gd_{i}", "")

                name = st.text_input(f"Group {i + 1} name", value=default_name, key=f"gn_{i}")
                raw = st.text_area("Values (comma-separated)", value=default_data,
                                   key=f"gd_{i}", height=80,
                                   placeholder="e.g. 85, 90, 78, 92")

                parsed = parse_input(raw)
                if raw.strip() and parsed is None:
                    st.error("⚠️ Need ≥ 2 valid numbers.")
                    all_valid = False
                elif parsed:
                    group_data[name] = parsed
                    arr = np.array(parsed)
                    st.caption(f"n = {len(parsed)} · mean = {arr.mean():.2f} · std = {arr.std(ddof=1):.2f}")

    st.markdown('<div style="margin-top:1.5rem"></div>', unsafe_allow_html=True)

    btn_col, reset_col = st.columns([5, 1])
    with btn_col:
        run_clicked = st.button("🚀 Run ANOVA Analysis", type="primary", use_container_width=True)
    with reset_col:
        if st.button("🔄 Reset", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    # Run ANOVA if button clicked
    if run_clicked:
        if len(group_data) < 2:
            st.error("Please provide valid data for at least 2 groups.")
        elif not all_valid:
            st.error("Please fix invalid inputs before running.")
        else:
            f_stat, p_value = run_anova(*group_data.values())
            
            # Extract data for visualizations and reporting
            group_names = list(group_data.keys())
            group_means = [np.mean(np.array(v)) for v in group_data.values()]
            group_stds = [np.std(np.array(v), ddof=1) for v in group_data.values()]
            
            st.session_state["anova_results"] = {
                "group_data": group_data,
                "f_stat": f_stat,
                "p_value": p_value,
                "alpha": alpha,
                "group_names": group_names,
                "group_means": group_means,
                "group_stds": group_stds,
            }
            st.success("✅ Analysis complete. Results are ready for review.")
            
            # Display quick summary
            st.markdown('<div style="margin-top:1.5rem"></div>', unsafe_allow_html=True)
            st.markdown('<p class="section-title">Analysis Summary</p>', unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("F-Statistic", f"{f_stat:.4f}")
            with col2:
                st.metric("P-Value", f"{p_value:.6f}")
            with col3:
                significance = "Not Significant" if p_value >= alpha else "Significant"
                st.metric("Result", significance)
            
            
    
    # Footer always displayed (moved outside if run_clicked block)
    st.divider()
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #999; font-size: 0.85rem;'>
    <p>@2026 ANOVA Analysis Tool</p>
    </div>
    """, unsafe_allow_html=True)
