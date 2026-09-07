import streamlit as st
import joblib
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Page configuration
st.set_page_config(
    page_title="Trustify - Spam Detector",
    page_icon="🛡️",
    layout="wide"
)
st.markdown("""
<style>
    .stApp {
        background-color: #0F172A;
    }

    h1 {
        color: #38BDF8;
        font-size: 48px;
    }

    h2, h3 {
        color: #E2E8F0;
    }

    p {
        color: #CBD5E1;
    }

    .stButton > button {
        background-color: #2563EB;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #1D4ED8;
        color: white;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    textarea {
        background-color: #1E293B !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Download stopwords if needed
try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords")

# Load model and vectorizer
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

tfidf_vectorizer = joblib.load(
    os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")
)

model = joblib.load(
    os.path.join(BASE_DIR, "random_forest_model.pkl")
)

# Preprocessing
stemmer = PorterStemmer()
stopwords_set = set(stopwords.words("english"))


def preprocess_text(text):
    text = text.lower()
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )
    text = text.split()

    text = [
        stemmer.stem(word)
        for word in text
        if word not in stopwords_set
    ]

    return " ".join(text)



with st.sidebar:
    st.title("🛡️ Trustify")

    st.markdown("### About the Model")

    st.write("""
    TrustAI uses Natural Language Processing
    and Machine Learning to classify emails
    as **Spam** or **Ham**.
    """)

    st.markdown("---")

    st.markdown("### 🔧 Technology")

    st.write("""
    • TF-IDF Vectorization  
    • Random Forest Classifier  
    • NLP Preprocessing  
    • Python + Streamlit
    """)

    st.markdown("---")

    st.markdown("### 📊 Model Performance")

    st.metric("Accuracy", "98.36%")
    st.metric("Spam Recall", "99.05%")




st.title("🛡️ Trustify")

st.subheader(
    "AI-powered spam detection using NLP & Machine Learning"
)

st.write(
    "Protect your inbox by analyzing an email with our trained "
    "machine learning model."
)

st.markdown("---")

# Input section

st.markdown("### 📩 Analyze an Email")

email_text = st.text_area(
    "Paste your email content below:",
    height=250,
    placeholder="Paste the subject and email body here..."
)

if st.button("🔍 Analyze Email", use_container_width=True):

    if email_text.strip() == "":
        st.warning("⚠️ Please enter an email before analyzing.")

    else:

        # Preprocess
        cleaned_email = preprocess_text(email_text)

        # TF-IDF
        email_vector = tfidf_vectorizer.transform(
            [cleaned_email]
        )

        # Prediction
        prediction = model.predict(email_vector)[0]

        # Probability
        probability = model.predict_proba(email_vector)[0]

        spam_probability = probability[1]
        ham_probability = probability[0]

        st.markdown("---")

        st.markdown("### 📊 Analysis Result")

        if prediction == 1:

            st.error("🚨 SPAM EMAIL")

            st.write(
                f"Spam probability: **{spam_probability:.2%}**"
            )

        else:

            st.success("✅ HAM — LEGITIMATE EMAIL")

            st.balloons()

            st.write(
                f"Legitimate probability: **{ham_probability:.2%}**"
            )



st.markdown("---")

st.markdown("### ⚙️ How TrustAI Works")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 1️⃣ Input")
    st.write("Paste the email content.")

with col2:
    st.markdown("### 2️⃣ Analyze")
    st.write("NLP preprocessing + TF-IDF.")

with col3:
    st.markdown("### 3️⃣ Predict")
    st.write("Random Forest classifies the email.")


st.markdown("---")

st.caption(
    "TrustAI • Built with Python, NLP, TF-IDF & Random Forest"
)