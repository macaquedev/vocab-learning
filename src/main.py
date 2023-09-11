import pickle
import os
import string

from PyInquirer import style_from_dict, Token, prompt

from relpath import relpath
from word import Word, WordBank
from cardbox_name_validator import CardboxNameValidator


if __name__ == '__main__':
    style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })

    with open(relpath("..", "new_words.txt")) as f:
        data = f.readlines()

    words = WordBank()

    for line in data:
        if line.strip() == "":
            continue

        split_line = [i.strip() for i in line.strip().split(":")]
        words.add_word(Word(split_line[0], split_line[1]))

    if not os.path.isdir(relpath("..", "cardboxes")):
        os.mkdir(relpath("..", "cardboxes"))

    options = os.listdir(relpath("..", "cardboxes")) + ["Create new cardbox"]
    questions = [
        {
            'type': 'list',
            'name': 'cardbox',
            'message': 'Which cardbox would you like to study from?',
            'choices': options
        }
    ]
    answers = prompt(questions, style=style)
    cardbox_name = answers["cardbox"]
    if cardbox_name == "Create new cardbox":
        questions = [
            {
                'type': 'input',
                'name': 'cardbox_name',
                'message': 'What would you like to call the new cardbox?',
                'validate': CardboxNameValidator
            }
        ]
        answers = prompt(questions, style=style)
        cardbox_name = answers["cardbox_name"]

    questions = [
        {
            'type': 'confirm',
            'name': 'confirmation',
            'message': f'Add {len(words)} words to dictionary?',
            'default': False
        }
    ]
    answers = prompt(questions, style=style)
    add_words = answers["confirmation"]

    if os.path.isfile(relpath("..", "cardboxes", cardbox_name)):
        with open(relpath("..", "cardboxes", cardbox_name), "rb") as f:
            data = pickle.load(f)
        if add_words:
            data += words
    else:
        if not add_words:
            exit(-1)
        data = words

    correct = 0
    wrong = 0

    print(f"{len([word for word in data if word.due()])} words to learn today")
    for word in data:
        if word.due():
            user_answer = None
            while not user_answer:
                try:
                    user_answer = "".join([i for i in input(f"{correct+wrong+1}. {word.english}: ").strip() if i in string.ascii_letters + " ÜÖÄüöäßÁÉÍÓÚÑáéíóúñ-'"])
                except UnicodeDecodeError:
                    print("Something went wrong. Please input the word again.")

            old_cardbox = word.current_cardbox
            if user_answer in word.foreign:
                word.correct()
                print("Correct!")
                print(f"Old cardbox: {old_cardbox}, new cardbox: {word.current_cardbox}")
                correct += 1
            else:
                word.wrong()
                print("Wrong!")
                print(f"Old cardbox: {old_cardbox}, new cardbox: {word.current_cardbox}")
                print(word)
                wrong += 1

    if correct == wrong == 0:
        print("No words due now.")
        exit(-1)

    print(f"Words correct: {correct}")
    print(f"Words wrong: {wrong}")
    print(f"Score: {round(correct / (correct + wrong) * 100, 2)}%")

    with open(relpath("..", "cardboxes", cardbox_name), "wb") as f:
        pickle.dump(data, f)
