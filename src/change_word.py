import os
import pickle
from word import Word

cardbox_name = "German"

with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "rb") as f:
    data = pickle.load(f)

#data.get_word("to lead to (dative)").foreign.pop()
#data.get_word("to lead to (dative)").foreign.append("mit D auskommen")
#data.get_word("to inform about something").cardbox = 5

#data.update_word("to appear, look like", "to appear, to look like")
data.delete_word("disgusting")
data.add_word(Word("eklig", "disgusting"))


with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "wb") as f:
    pickle.dump(data, f)
