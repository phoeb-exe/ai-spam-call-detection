import joblib
from utils.data_preprocessing import clean_text

class SpamModel:
    def __init__(self, model_path="artifacts/tf-idf_xgb.pkl"):
        self.model = joblib.load(model_path)

    def predict(self, text):
        cleaned = clean_text(text)
        prob = self.model.predict_proba([cleaned])[0][1]
        pred = self.model.predict([cleaned])[0]
        return pred, prob
