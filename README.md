# 🛡️ Trustify

### AI Spam Detector using NLP & Machine Learning

**Trustify** is an end-to-end NLP and Machine Learning application that analyzes email content and classifies it as **Spam or Ham** using TF-IDF and Random Forest.

<p align="center">
  <a href="https://trustify-zimqjvqg5yrmclkhecarxv.streamlit.app/">🚀 Live Demo</a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="YOUR_GITHUB_LINK">💻 Repository</a>
</p>

---

## ✨ Features

* 📩 **Real-time Email Analysis**
* 🧠 **NLP-based Text Processing**
* 🔢 **TF-IDF Feature Extraction**
* 🌲 **Random Forest Classification**
* 📊 **Spam Probability**
* 🌐 **Streamlit Web Application**
* ☁️ **Cloud Deployment**

---

## 🏗️ Architecture

```text
┌──────────────────────────────┐
│         📩 Email Input       │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│      NLP Preprocessing       │
│ Lowercase • Stopwords        │
│ Punctuation • Stemming       │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       TF-IDF Vectorizer      │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│     🌲 Random Forest         │
│        Classifier            │
└──────────────┬───────────────┘
               ↓
        ┌──────┴──────┐
        ↓             ↓
    🟢 HAM        🔴 SPAM
```

---

## 📊 Model Performance

**Final Model:** TF-IDF + Random Forest

| Metric         |      Score |
| -------------- | ---------: |
| Accuracy       | **98.36%** |
| Spam Precision | **98.65%** |
| Spam Recall    | **99.05%** |
| Spam F1-Score  | **98.85%** |

The model was evaluated on a held-out test set of **1,035 emails**.

---

## 🛠️ Technology Stack

| Category           | Technologies              |
| ------------------ | ------------------------- |
| Language           | Python                    |
| Data Processing    | Pandas, NumPy             |
| NLP                | NLTK                      |
| Feature Extraction | TF-IDF                    |
| Machine Learning   | Scikit-learn              |
| Final Model        | Random Forest             |
| Model Persistence  | Joblib                    |
| Web Application    | Streamlit                 |
| Deployment         | Streamlit Community Cloud |
| Version Control    | GitHub                    |

---

## 📸 Application

### Email Analysis

![Trustify Interface]()

### Spam Detection

![Spam Prediction](images/trustify-spam.png)

---

## 🚀 Deployment

Trustify is deployed using **Streamlit Community Cloud**, so the application can be tested directly without setting up the project locally.

### 👉 [Open Trustify Live](YOUR_DEPLOYMENT_LINK)

---

## 📁 Project Structure

```text
Trustify/
│
├── app.py
├── spam_email_detection.ipynb
├── spam_ham_dataset.csv
├── random_forest_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## 📚 Documentation

For the complete project documentation, including:

* Dataset analysis
* NLP preprocessing
* Model experiments
* Model comparison
* Evaluation
* Technical decisions
* Deployment process
* Limitations
* Future improvements

→ **See [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md)**

---

## 👩‍💻 Author

### Disha

Computer Science Engineering Student focused on **Data Science, Machine Learning & AI**.

I enjoy building practical ML projects that move beyond notebooks into **usable, deployed applications**.

---

### ⭐ Explore Trustify

**[🚀 Live Demo](https://trustify-zimqjvqg5yrmclkhecarxv.streamlit.app/)**   |   **[💻 GitHub Repository](YOUR_GITHUB_LINK)**
