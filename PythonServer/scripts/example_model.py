import torch
from transformers import pipeline
from .base_model import BaseModel


class SentimentAnalysisModel(BaseModel):
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        self.model = pipeline("sentiment-analysis")

    def predict(self, input_data):
        result = self.model(input_data)[0]
        return result


if __name__ == "__main__":
    sentiment_model = SentimentAnalysisModel()
    result = sentiment_model.predict("I love this movie!")
    print(result)
