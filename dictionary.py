message = input(">")
words = message.split(" ")
emojis = {
    "sad": ":)",
    "happy": ":(",
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)


