message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😔",
    ":D": "😃",
    ":p": "😛",
    ":o": "😲",
    ":*": "😘",
    ":|": "😐",
    ":x": "❤",
    "t": "🍅"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
