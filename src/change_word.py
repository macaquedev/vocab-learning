import os
import pickle
from word import Word

cardbox_name = "German"

with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "rb") as f:
    data = pickle.load(f)

#data.get_word("to lead to (dative)").foreign.pop()
#data.get_word("to take part in").foreign.append("an D teilnehmen")
#data.get_word("to be about (the story is about)").foreign.pop()
#data.get_word("to be about (the story is about)").foreign.append("um D gehen")


#data.get_word("to inform about something").cardbox = 5
#data.delete_word("hereditary land")
#data.delete_word("place, spot")
data.delete_word("famine")
#data.update_word("to appear, look like", "to appear, to look like")
#data.delete_word("to apply to")
#data.add_word(Word("das Erbland", "hereditary land"))
#data.add_word(Word("der Benutzer", "user"))
#for english, foreign in data.words.items():
#    print(foreign)

with open(os.path.join(os.path.dirname(__file__), "..", "cardboxes", cardbox_name), "wb") as f:
    pickle.dump(data, f)
