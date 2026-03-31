# 📊 ANOVA One-Way Analysis Tool

## Engineering Mathematics-4 (EM-4) Project

A comprehensive, interactive Streamlit application for performing One-Way ANOVA (Analysis of Variance) analysis with professional visualizations, statistical testing, and detailed reporting capabilities.

---

## 👥 Project Team

**Group:** 12  
**Topic:** ANOVA One-Way Test

### Team Members

| Role             | Name              | Roll Number |
| ---------------- | ----------------- | ----------- |
| **Group Leader** | Adarsh Rasal      | 25101B2002  |
| **Member**       | Sujal Patil       | 25101B2001  |
| **Member**       | Vibhas Kadam      | 25101B2003  |
| **Member**       | Vedant Sakapl     | 25101B2004  |
| **Member**       | Bhushan Avhad     | 25101B2006  |
| **Member**       | Shreedhar Khorate | 25101B2007  |

---

## 📋 Overview

This project implements a complete One-Way ANOVA analysis tool that allows users to:

- Compare means across 3+ groups simultaneously
- Perform statistical hypothesis testing
- Validate ANOVA assumptions (Levene's test for homogeneity of variance)
- Calculate effect sizes and interpret results
- Generate comprehensive visualizations
- Export detailed reports in PDF and TXT formats

### Key Features

✅ **Interactive Data Input**

- Manual data entry for multiple groups
- Pre-loaded sample datasets for quick testing
- Real-time data validation

✅ **Statistical Analysis**

- One-Way ANOVA F-test
- Levene's Test for homogeneity of variance
- Effect size calculation (Eta-squared η²)
- Comprehensive descriptive statistics

✅ **Rich Visualizations**

- Box plots for distribution comparison
- Bar charts with error bars
- Kernel Density Estimation (KDE) curves
- Overlaid histograms
- Violin plots
- Summary statistics heatmaps
- Range, IQR & Median plots

✅ **Report Generation**

- **PDF Reports:** Full comprehensive reports with tables and visualizations
- **TXT Reports:** Detailed text summaries with all statistical values
- **HTML Support:** Exportable HTML reports with styled formatting

✅ **Professional UI**

- Modern, responsive design
- Gradient backgrounds and smooth animations
- Mobile-friendly layout
- Custom CSS styling with Poppins and Space Grotesk fonts

---

## 🚀 Getting Started

### Requirements

- Python 3.8+
- Streamlit
- NumPy
- SciPy
- Matplotlib
- Seaborn
- ReportLab (for PDF generation)

### Installation

1. **Clone or download the project:**

   ```bash
   cd ANOVA
   ```

2. **Install dependencies:**

   ```bash
   pip install streamlit numpy scipy matplotlib seaborn reportlab
   ```

3. **Run the application:**

   ```bash
   streamlit run app.py
   ```

4. **Access the app:**
   Open your browser to `http://localhost:8501`

---

## 📖 How to Use

### Step 1: Configure Settings

- Set the **significance level (α)** - typically 0.05
- Select the **number of groups** to compare (2-6)
- Optionally load a **sample dataset** for quick testing

### Step 2: Input Data

- Enter **group names** and **values** (comma-separated)
- Data is validated in real-time
- View statistics for each group as you enter data

### Step 3: Run Analysis

- Click **"🚀 Run ANOVA Analysis"** button
- The app calculates F-statistic, p-value, and effect size

### Step 4: Interpret Results

- View key metrics in metric cards
- Check hypothesis test verdict (Reject/Fail to Reject H₀)
- Review group summaries
- Analyze visualizations

### Step 5: Export Reports

- Download **PDF Report** - Complete analysis with all visualizations
- Download **TXT Report** - Detailed text summary with statistics

---

## 🔬 Statistical Background

### One-Way ANOVA

Tests whether means of 3+ independent groups differ significantly.

**Hypotheses:**

- **H₀ (Null):** μ₁ = μ₂ = ... = μₖ (All group means are equal)
- **H₁ (Alternative):** At least one group mean differs

**Test Statistic:**
$$F = \frac{\text{Variance Between Groups}}{\text{Variance Within Groups}}$$

**Decision Rule:**

- If p-value < α: **Reject H₀** → Significant difference exists
- If p-value ≥ α: **Fail to Reject H₀** → No significant difference

### Assumptions

1. **Independence:** Observations within groups are independent
2. **Normality:** Data approximately normally distributed per group
3. **Homogeneity:** Equal variances across groups (tested via Levene's test)

### Effect Size (Eta-squared η²)

Measures the proportion of variance explained by group differences:

- **η² < 0.01:** Negligible effect
- **0.01 ≤ η² < 0.06:** Small effect
- **0.06 ≤ η² < 0.14:** Medium effect
- **η² ≥ 0.14:** Large effect

---

## 📊 Sample Datasets

The app includes three pre-loaded examples:

1. **Student Exam Scores (3 teaching methods)**
   - Compare effectiveness of different teaching methods

2. **Crop Yield (3 fertilizers)**
   - Analyze impact of fertilizer types on crop yield

3. **No Significant Difference (similar groups)**
   - Example where groups are statistically equivalent

---

## 📁 Key Application Sections

### 01 — Background

Educational content explaining ANOVA concepts, hypotheses, and assumptions

### 02 — Configure

Settings panel for significance level, group count, and data input

### 03 — Output

Comprehensive results section with:

- Key metric cards
- Hypothesis testing verdict
- Group summaries
- Multiple visualizations
- Statistical tests
- Descriptive statistics table
- Insights and recommendations
- ANOVA summary table
- Report download options

---

## 📦 File Structure

```
app.py          - Main Streamlit application (single comprehensive file)
README.md       - Project documentation
LICENSE         - License information
```

---

## 🎓 Learning Objectives

Through this project, students will understand:

1. ✅ Concept of variance and its role in hypothesis testing
2. ✅ One-Way ANOVA methodology and theory
3. ✅ F-distribution and p-value interpretation
4. ✅ Assumption testing (Levene's test)
5. ✅ Effect size calculation and interpretation
6. ✅ Statistical decision-making
7. ✅ Data visualization best practices
8. ✅ Professional report generation

---

## 🛠️ Technologies Used

- **Streamlit** - Web framework for data applications
- **Python** - Programming language
- **NumPy** - Numerical computations
- **SciPy** - Statistical functions
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical graphics
- **ReportLab** - PDF generation

---

## 📝 License

This project is part of the Engineering Mathematics-4 (EM-4) curriculum.

---

## ✉️ Contact & Support

For questions or clarifications, contact Group 12 members.



---

 
**Developed for:** Engineering Mathematics-4 Project  
**Academic Year:** 2025-2026
