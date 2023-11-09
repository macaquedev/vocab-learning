with open("hsk1--1-34.txt", encoding="utf-8") as f:
    lines = f.readlines()

with open("output.txt", "w+", encoding="utf-8") as f:
    for i in range(len(lines)):
        char, pinyin = lines[i].split(":")
        pinyin = pinyin.strip()

        f.write(pinyin + ": " + char + "\n")

