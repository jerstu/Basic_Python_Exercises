# emoji converter dictionary

message = input(">")        # user input
words = message.split(' ')  # returns an array split by spaces ' '
emojis = {                  # define a dictionary of text to emoji
    ":)": "🙂",
    ":(": "☹"
}

output = ""
for word in words:          # append emoji to output when found, default to original word
    output += emojis.get(word, word) + " "
print(output)