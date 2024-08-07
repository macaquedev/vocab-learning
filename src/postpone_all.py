import os
import pickle
import datetime

cardbox_name = "German"
days = 1

with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "rb") as f:
    data = pickle.load(f)


for word in data:
    word.date_next_due += datetime.timedelta(days=days)


with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "wb") as f:
    pickle.dump(data, f)
