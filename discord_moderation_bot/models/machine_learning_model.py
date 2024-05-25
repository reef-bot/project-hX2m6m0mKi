# machine_learning_model.py

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class ContentClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def train_model(self, X_train, y_train):
        X_train_counts = self.vectorizer.fit_transform(X_train)
        self.model.fit(X_train_counts, y_train)

    def predict(self, text):
        text_counts = self.vectorizer.transform([text])
        return self.model.predict(text_counts)[0]

    def save_model(self, model_path):
        np.save(model_path, self.model)

    def load_model(self, model_path):
        self.model = np.load(model_path, allow_pickle=True)

# End of machine_learning_model.py