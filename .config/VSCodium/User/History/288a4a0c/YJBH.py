def emoji_converter(message):
    word = message.split()
    emoji = {
        ":)" : "😊",
        ":(" : "🙁",
        "-_-" : "😐",
    }
    output = ""
    for words in word:
        output += emoji.get(words, words) + emoji(value)
        return output


message = input(">")
print(emoji_converter(message))
    