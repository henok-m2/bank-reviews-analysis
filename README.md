# Bank Reviews Analytics

A data analytics project analyzing customer reviews for Ethiopian banking apps from Google Play Store.

## 📊 Project Overview

This project collects and analyzes user reviews to understand customer satisfaction for three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA) 
- Dashen Bank

## 🎯 What We Do

1. **Scrape Reviews** - Collect user reviews from Google Play Store
2. **Analyze Sentiment** - Determine positive/negative/neutral feelings
3. **Identify Themes** - Find common topics and issues
4. **Store in Database** - Save analyzed data in PostgreSQL
5. **Generate Insights** - Create visualizations and recommendations

## 📈 Results So Far

**Data Collected: 9,806 Reviews**
- CBE: 8,113 reviews
- BOA: 1,184 reviews  
- Dashen: 502 reviews

**Key Themes Found:**
- Account Access & Login Issues
- Transaction Problems
- App Performance & Speed
- User Interface Design
- Customer Support

## 🛠️ Project Structure

  bank-reviews-analysis/
├── notebooks/ # Jupyter notebooks for analysis
├── src/ # Python source code
├── data/ # CSV files with review data
├── scripts/ # Utility scripts
└── requirements.txt # Python dependencies


## 🚀 Quick Start


# 1. Clone repository
git clone https://github.com/YOUR_USERNAME/bank-reviews-analysis.git
cd bank-reviews-analysis

# 2. Setup environment
python -m venv bank_env
source bank_env/bin/activate
pip install -r requirements.txt

# 3. Run analysis
jupyter notebook

📋 Project Progress
✅ Task 1: Data Collection & Cleaning
✅ Task 2: Sentiment & Thematic Analysis
🔄 Task 3: Database Storage (Next)
⏳ Task 4: Insights & Reporting

👨‍💻 Author
Henok Mulugeta - 10 Academy AI Mastery Program
