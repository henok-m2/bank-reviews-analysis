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
git clone https://github.com/henok_m2/bank-reviews-analysis.git
cd bank-reviews-analysis

# 2. Setup environment
python -m venv bank_env
source bank_env/bin/activate
pip install -r requirements.txt

# 3. Run analysis
jupyter notebook

# Task 3: Database Storage with PostgreSQL
## Persistent Data Storage for Bank Reviews Analysis

### 🎯 Objective
Design and implement a relational database in PostgreSQL to store cleaned and processed review data, simulating real-world data engineering workflows.

### ✅ Requirements Completed
- [x] Install and configure PostgreSQL database
- [x] Design relational database schema for banks and reviews
- [x] Create tables with proper constraints and relationships
- [x] Insert cleaned review data from CSV files
- [x] Write SQL queries to verify data integrity
- [x] Ensure database persistence and reliability

### 🗄️ Database Schema

#### Banks Table
sql
CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(50) NOT NULL UNIQUE,
    app_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



## Task 4 README: Insights and Recommendations

markdown
# Task 4: Insights and Recommendations
## Business Intelligence from Customer Reviews

### 🎯 Objective
Derive actionable insights from sentiment and thematic analysis, create compelling visualizations, and provide data-driven recommendations for app improvement.

### ✅ Requirements Completed
- [x] Identify 2+ satisfaction drivers per bank
- [x] Identify 2+ pain points per bank
- [x] Create 4+ professional visualizations
- [x] Generate actionable business recommendations
- [x] Address potential review biases and ethics
- [x] Deliver comprehensive final report

### 📊 Analysis Summary

#### Data Overview
- **Total Reviews Analyzed**: 9,806
- **Banks**: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), Dashen Bank
- **Time Period**: Full historical review dataset
#### Key Statistics
Commercial Bank of Ethiopia: 8,113 reviews | Avg Rating: 3.8 ⭐
Bank of Abyssinia: 1,184 reviews | Avg Rating: 3.6 ⭐
Dashen Bank: 502 reviews | Avg Rating: 4.2 ⭐

Overall Sentiment:
Positive: 49.9% | Negative: 31.9% | Neutral: 18.2%


### 📈 Visualizations Generated

#### 1. Sentiment Distribution by Bank
![Sentiment Distribution](plots/sentiment_by_bank.png)
- Comparative sentiment analysis across all banks
- Stacked percentage view for relative performance

#### 2. Rating Analysis
![Rating Analysis](plots/rating_analysis.png)
- Overall rating distribution (1-5 stars)
- Average rating by bank and sentiment correlation

#### 3. Theme Analysis
![Theme Analysis](plots/theme_analysis.png)
- Top 10 most common themes across all reviews
- Theme mentions by bank (heatmap)
- Theme-sentiment correlation
- Average rating by theme

#### 4. Word Clouds
![Word Clouds](plots/word_clouds.png)
- Visual representation of most frequent terms
- Bank-specific word clouds for qualitative insights

### 🎯 Key Insights Discovered

#### Commercial Bank of Ethiopia (CBE)
**Satisfaction Drivers:**
- Comprehensive feature set
- Wide service availability
- Regular updates and maintenance

**Pain Points:**
- Login and account access issues (32% of negative reviews)
- App crashes during peak hours
- Slow transaction processing

#### Bank of Abyssinia (BOA)
**Satisfaction Drivers:**
- Clean and intuitive user interface
- Easy navigation and setup
- Reliable basic functionality

**Pain Points:**
- Transaction failures (41% of negative reviews)
- Limited advanced features
- Customer support response times

#### Dashen Bank
**Satisfaction Drivers:**
- Highest overall satisfaction rate
- Reliable app performance
- Positive customer support feedback

**Pain Points:**
- Feature gaps compared to competitors
- Occasional update issues
- Limited customization options

### 💡 Business Recommendations

#### For Commercial Bank of Ethiopia
1. **Priority**: Fix login and authentication flow
   - Implement biometric authentication
   - Simplify password recovery process
   - **Timeline**: Next quarterly update

2. **Secondary**: Improve app stability
   - Optimize memory usage during peak hours
   - Implement crash analytics and monitoring
   - **Timeline**: Within 2 months

#### For Bank of Abyssinia
1. **Priority**: Enhance transaction reliability
   - Optimize backend processing infrastructure
   - Add instant transaction notifications
   - **Timeline**: Immediate focus

2. **Secondary**: Expand feature set
   - Add budgeting and financial planning tools
   - Implement bill payment automation
   - **Timeline**: Next major release

#### For Dashen Bank
1. **Priority**: Close feature gaps
   - Add peer-to-peer payment options
   - Implement investment tracking features
   - **Timeline**: Next feature release

2. **Secondary**: Enhance user engagement
   - Add personalized financial insights
   - Implement rewards and loyalty program
   - **Timeline**: Q3 planning

### 🔧 Technical Implementation

#### Analysis Pipeline
python
# Complete insights generation workflow
1. Database connection and data loading
2. Statistical analysis and metric calculation
3. Visualization generation (4+ plot types)
4. Theme extraction and pattern identification
5. Recommendation formulation
6. Report compilation


📋 Project Progress
✅ Task 1: Data Collection & Cleaning
✅ Task 2: Sentiment & Thematic Analysis
✅ Task 3: Database Storage (Next)
✅ Task 4: Insights & Reporting

👨‍💻 Author
Henok Mulugeta - 10 Academy AI Mastery Program

