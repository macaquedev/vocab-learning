import os
import pickle
from word import Word

cardbox_name = "Mandarin"

with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "rb") as f:
    data = pickle.load(f)

#data.get_word("to lead to (dative)").foreign.pop()
#data.get_word("to take part in").foreign.append("an D teilnehmen")
#data.get_word("to be about (the story is about)").foreign.pop()
#data.get_word("to be about (the story is about)").foreign.append("um D gehen")


#data.get_word("to inform about something").cardbox = 5
#data.delete_word("to inherit")
#data.update_word("to appear, look like", "to appear, to look like")
data.delete_word("衣服")
data.add_word(Word("衣服", "clothes"))


with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "wb") as f:
    pickle.dump(data, f)
