import joblib
from preprocess import clean_text
import os

# Load saved model & vectorizer
save_dir = os.path.join(os.path.dirname(__file__), "../models")
model = joblib.load(os.path.join(save_dir, "model.pkl"))
vectorizer = joblib.load(os.path.join(save_dir, "vectorizer.pkl"))

def predict(text: str) -> str:
    """
    Predict whether a text is bullying or safe.
    """
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    return pred

# Test the service
if __name__ == "__main__":
    samples = [
        "hello ",
        "i hate you. You look nigga",
        ""
       
    ]
    for s in samples:
        print(f"{s} --> {predict(s)}")