
import demoji


def emoji2text(text: str):
    output = demoji.findall(text)
    return output


test = emoji2text(""" 😄 Feeling ✨️ today! ☀️ Went for a long walk 🚶‍♂️, enjoyed a delicious 🍕, and now relaxing with a good book 📚 and some calming music 🎶. Life is good 😊 """)
print(test)
