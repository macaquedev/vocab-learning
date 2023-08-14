import os
import pickle


cardbox_name = "Spanish"
days = 30

with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "rb") as f:
    data = pickle.load(f)

for word in data:
    word.correct()

with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "wb") as f:
    pickle.dump(data, f)
