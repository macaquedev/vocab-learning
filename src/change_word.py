import os
import pickle


cardbox_name = "German"

with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "rb") as f:
    data = pickle.load(f)

# data.get_word("to accept").foreign.pop()
# data.get_word("to accept").foreign.append("akzeptieren")


#data.update_word("to appear, look like", "to appear, to look like")
data.delete_word("headline")
data.delete_word("to depend on (accusative)")

with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "wb") as f:
    pickle.dump(data, f)
