# AI-Powered Smart Recruitment System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/machine--learning-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent recruitment screening and candidate ranking system built using **Python**, **Scikit-Learn**, **TF-IDF Vectorization**, and **Random Forest Machine Learning**. The system analyzes candidate profiles against job requirements to predict candidate suitability and produce automated ranked recommendations.

---

## 🌟 Key Features
- **Automated Candidate Screening**: Uses natural language processing (TF-IDF) to calculate similarity scores between job requirements and candidate profiles.
- **Machine Learning Suitability Prediction**: Trains a Random Forest Regressor on experience, technical skills, and background metrics.
- **Weighted Ranking Engine**: Combines semantic similarity (60%) and ML suitability score (40%) to calculate a final matching percentage.
- **Scalable Architecture**: Easily configurable for large candidate databases and custom job requirements.

---

## 🛠️ Project Structure
```
ai-smart-recruitment-system/
├── data/
│   └── candidates.csv       # Preprocessed candidate dataset
├── src/
│   └── ranker.py            # Feature engineering, TF-IDF, & Random Forest model
├── main.py                  # CLI demonstration script
└── README.md                # Documentation & usage guide
```

---

## 🚀 Quick Start & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/elikantecharan/ai-smart-recruitment-system.git
   cd ai-smart-recruitment-system
   ```

2. **Install dependencies**:
   ```bash
   pip install pandas numpy scikit-learn
   ```

3. **Run the Demonstration**:
   ```bash
   python main.py
   ```

---

## 📊 Sample Output

```text
============================================================
      AI-POWERED SMART RECRUITMENT & RANKING SYSTEM
============================================================
[+] Initializing Machine Learning Model & Vectorizers...
[+] Model loaded successfully!

👉 SAMPLE JOB QUERY:
   "Python Machine Learning Engineer with Scikit-Learn, Pandas, and SQL skills."
------------------------------------------------------------
   Score: 92.4% | ID: 101 | Name: Aarav Sharma (4 yrs exp) | Skills: Python Machine Learning Scikit-Learn SQL Pandas
   Score: 86.1% | ID: 105 | Name: Vikram Singh (3 yrs exp) | Skills: Python Scikit-Learn Data Analytics SQL Statistics
   Score: 81.3% | ID: 107 | Name: Karan Joshi (6 yrs exp) | Skills: Python PyTorch TensorFlow Machine Learning NLP
------------------------------------------------------------
```

---

## 👤 Author
**Elikante Charan**  
- GitHub: [@elikantecharan](https://github.com/elikantecharan)  
- Email: elikantecharan@gmail.com  
- Portfolio: [https://elikantecharan.github.io/portfolio/](https://elikantecharan.github.io/portfolio/)
