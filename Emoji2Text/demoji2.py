import demoji


def emoji2text(text: str):
    output = demoji.findall(text)
    return output


test = emoji2text(""" Woke up this morning feeling 😴, but a cup of coffee ☕ and some sunshine ☀️ quickly changed that! 🌈 Now I'm feeling energized and ready to tackle the day 💪. 🎧 Listening to some upbeat music 🎶 while I work, and I'm already feeling productive. 😊 Hope everyone has a wonderful day! """)
print(test)
