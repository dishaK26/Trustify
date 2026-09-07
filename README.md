🛡️ Trustify — AI Spam Detector Using NLP & Machine Learning

An end-to-end NLP and Machine Learning application that detects whether an email is Spam or Ham in real time.

￼ ￼ ￼ ￼

🚀 Live Demo

👉 https://trustify-zimqjvqg5yrmclkhecarxv.streamlit.app/

No installation required.
Paste any email into the application and Trustify will analyze it and predict whether it is Spam or Ham.

📂 GitHub Repository

View Source Code & Project Files →

🎯 What is Trustify?

Spam emails are not always obvious. Promotional messages, fraudulent offers, phishing attempts, and suspicious communications can look very similar to legitimate emails.
Trustify uses Natural Language Processing (NLP) and Machine Learning to automatically classify email text into two categories:
PredictionMeaning🟢 Ham (0)Legitimate email🔴 Spam (1)Spam email 
The project goes beyond model training by turning the final model into a real-time web application using Streamlit and deploying it for public access.

💡 Why I Built This

The objective was to take a real-world text classification problem through the complete machine learning lifecycle:
Raw Email → NLP Processing → Feature Engineering → Model Training → Model Evaluation → Model Selection → Deployment
This project helped me understand not just how to train a model, but also how to turn that model into a usable application.

🔄 Project Workflow

📧 RAW EMAIL │ ▼ ┌─────────────────┐ │ Text Cleaning │ └─────────────────┘ │ ▼ Lowercasing + Punctuation Removal │ ▼ Stopword Removal │ ▼ Stemming │ ▼ Cleaned Email │ ▼ ┌─────────────────┐ │ TF-IDF │ │ Vectorization │ └─────────────────┘ │ ▼ Numerical Features │ ▼ ┌────────────────────┐ │ Random Forest │ │ Classifier │ └────────────────────┘ │ ┌───────┴───────┐ ▼ ▼ 🟢 HAM 🔴 SPAM 

🧹 Data Preprocessing

Raw email text was processed using an NLP pipeline before being passed to the machine learning models.

Preprocessing Steps

Lowercasing

Standardizes text so words with different capitalization are treated consistently.

Punctuation Removal

Removes unnecessary punctuation from email text.

Stopword Removal

Removes common words that generally provide limited discriminatory information.

Porter Stemming

Reduces words to their stem/root form.

Example:

playing → play played → play plays → play 

Corpus Creation 

The cleaned text was reconstructed and stored as the final corpus.

🔢 Feature Engineering — TF-IDF

Machine learning algorithms require numerical input, so the cleaned email corpus was converted into numerical features using:

TF-IDF — Term Frequency–Inverse Document Frequency

TF-IDF represents the importance of words within documents while reducing the influence of words that appear frequently across the entire dataset.
The final vectorization generated approximately:
42,637 text features.
The trained vectorizer was saved separately so that new emails entered through the Streamlit application can be transformed using the same feature representation used during model training.

🤖 Machine Learning Models

Four classification algorithms were evaluated:

1. Logistic Regression

A strong baseline for high-dimensional text classification.

2. Random Forest

An ensemble learning algorithm that combines multiple decision trees to produce robust predictions.

3. Decision Tree

A tree-based classification algorithm that learns decision rules from the feature space.

4. Naive Bayes

A probabilistic algorithm commonly used for text classification.

📊 Model Performance

The models were evaluated using:

Precision

Recall

F1-score

Accuracy

Classification Report

Confusion Matrix

TF-IDF Model Comparison

ModelSpam PrecisionSpam RecallSpam F1AccuracyLogistic Regression0.960.990.970.98Random Forest0.980.980.980.98Decision Tree0.920.910.920.95Naive Bayes0.950.970.960.98 

🏆 Why Random Forest?

Although Logistic Regression and Random Forest achieved similar overall accuracy, Random Forest provided a strong balance between precision, recall and F1-score for the Spam class.
The final model produced:
MetricResultAccuracy98.36%Spam Precision98.65%Spam Recall99.05%Spam F1-score98.85% 

Confusion Matrix

Predicted HamPredicted SpamActual Ham28610Actual Spam7732 
This resulted in:

True Negative: 286

False Positive: 10

False Negative: 7

True Positive: 732

The model was therefore not treated as a 100% accurate system. Real-world email classification can still produce false positives and false negatives.

💾 Model Persistence

After selecting Random Forest, the trained model and TF-IDF vectorizer were serialized using Joblib.
random_forest_model.pkl tfidf_vectorizer.pkl 
This allows the deployed application to load the already-trained objects instead of retraining the model every time the application starts.

Prediction Pipeline

New Email ↓ Preprocessing ↓ TF-IDF Vectorizer ↓ Random Forest Model ↓ Spam / Ham Prediction 

🌐 Streamlit Application

Trustify was converted into an interactive web application using Streamlit.
The user simply:
1. Opens Trustify ↓ 2. Pastes an email ↓ 3. Clicks Analyze Email ↓ 4. NLP preprocessing ↓ 5. TF-IDF transformation ↓ 6. Random Forest prediction ↓ 7. Spam / Ham result 
The application is publicly deployed, allowing users and recruiters to test the model without setting up the project locally.

🖥️ Application Preview

📸 Add your Streamlit application screenshot here

![Trustify Application](images/trustify-app.png) 
A screenshot of the live application can be added to the repository under:
images/ └── trustify-app.png 

🛠️ Tech Stack

Programming

Python

Data Processing

Pandas

NumPy

NLP

NLTK

Porter Stemmer

Stopword Removal

Machine Learning

Scikit-learn

Logistic Regression

Random Forest

Decision Tree

Naive Bayes

Feature Engineering

TF-IDF

Model Persistence

Joblib

Application & Deployment

Streamlit

Streamlit Community Cloud

Development

Jupyter Notebook

GitHub

📁 Project Structure

Trustify/ │ ├── app.py ├── spam_email_detection.ipynb ├── random_forest_model.pkl ├── tfidf_vectorizer.pkl ├── requirements.txt ├── README.md └── spam_ham_dataset.csv 

File Description

FilePurposeapp.pyStreamlit applicationspam_email_detection.ipynbComplete ML/NLP workflowrandom_forest_model.pklTrained Random Forest modeltfidf_vectorizer.pklTrained TF-IDF vectorizerrequirements.txtRequired Python dependenciesspam_ham_dataset.csvDataset used for trainingREADME.mdProject documentation 

⚙️ Run Locally

If you want to run Trustify locally:

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_LINK_HERE cd Trustify 

2. Install dependencies

pip install -r requirements.txt 

3. Run the Streamlit application

streamlit run app.py 
The application will open in your browser.

Recruiters: You can skip the local setup and directly test the deployed application using the Live Demo link at the top of this README.

⚠️ Limitations

Trustify is a machine learning prototype and has several limitations:

Performance depends on the training dataset.

Some legitimate emails may be classified as Spam.

Some Spam emails may be classified as Ham.

The current model primarily analyzes email text.

It does not independently inspect sender reputation, email headers, attachments, or URL safety.

Real-world emails can also differ from the dataset used for training, which can cause distribution shift and affect predictions.

🔮 Future Improvements

Potential improvements include:

🔗 URL and hyperlink analysis

📩 Email-header analysis

🌐 Sender/domain reputation features

📎 Attachment-risk analysis

⚙️ Hyperparameter tuning

🔄 Cross-validation

🧠 Explainable AI for prediction reasoning

📚 Larger and more diverse email datasets

🔁 Continuous model retraining

🔐 Combining NLP with cybersecurity signals

A future version could combine:
Email Text + Sender Information + URLs + Headers + Attachments
to create a more comprehensive email threat-detection system.

📚 Key Concepts Demonstrated

This project demonstrates practical implementation of:

Exploratory Data Analysis

Data Cleaning

Natural Language Processing

Text Preprocessing

Stopword Removal

Stemming

TF-IDF

Train-Test Split

Classification

Ensemble Learning

Model Comparison

Precision

Recall

F1-score

Confusion Matrix

Model Persistence

Streamlit

GitHub

Cloud Deployment

👩‍💻 Author

Disha
Built as an end-to-end Machine Learning + NLP portfolio project.

⭐ If you found this project interesting

Feel free to explore the repository and try the live Trustify application.

🚀 TRY TRUSTIFY LIVE →
