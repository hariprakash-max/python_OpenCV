import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# Load dataset
df = pd.read_csv('news_dataset.csv')

# Preprocessing
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Tokenization
    tokens = word_tokenize(text)
    # Remove stopwords
    filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words]
    # Join tokens back into string
    preprocessed_text = ' '.join(filtered_tokens)
    return preprocessed_text

df['text'] = df['text'].apply(preprocess_text)

# Feature extraction
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
X = tfidf_vectorizer.fit_transform(df['text'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Evaluate the classifier
y_pred = rf_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

# Make predictions
def predict_fake_news(news_text):
    preprocessed_text = preprocess_text(news_text)
    features = tfidf_vectorizer.transform([preprocessed_text])
    prediction = rf_classifier.predict(features)
    return prediction[0]

# Example usage
news_text = "Study shows that eating chocolate daily can improve brain function."
prediction = predict_fake_news(news_text)
if prediction == 0:
    print("The news is genuine.")
else:
    print("The news is fake.")
