#  dictionaries exercise
#  user inputs phone # and output is in words

#  first define a dictionary for numbers
number_words = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
# get users phone number
phone_number = input("Phone Number: ")

for number in phone_number:        # for each digit
    print(number_words[number])    # print the value

# Mosh's solution
# uses get method, with default value "!" in case there is non digit input
# concat a string to output
output = ""
for ch in phone_number:
    output += number_words.get(ch, "!") + " "
print(output)