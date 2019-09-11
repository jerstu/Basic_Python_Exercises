# emoji converter dictionary
# modified to use a function


def emoji_converter(message):
    words = message.split(' ')  # returns an array split by spaces ' '
    emojis = {                  # define a dictionary of text to emoji
        ":)": "🙂",
        ":(": "☹"
    }
    output = ""
    for word in words:          # append emoji to output when found, default to original word
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))
