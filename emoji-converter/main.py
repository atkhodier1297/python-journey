message = input(">")
words = message.split(" ")

# Emojis dictionary for replacing words
emojis = {
    ":)": "😃",
    ":(": "🙁"
}

output = ""
for word in words:
    # Replace the word if it's in the emoji dictionary, otherwise keep the word
    output += emojis.get(word, word) + " "

print(output.strip())

# Use functions to simplify the code.

def replace_with_emojis(message):
    # Emojis dictionary for replacing words
    emoji_dict = {
        ":)": "😃",
        ":(": "🙁"
    }

    # Split the message into words
    words = message.split(" ")

    # Replace each word with its corresponding emoji (if available)
    output = ""
    for word in words:
        output += emoji_dict.get(word, word) + " "

    return output.strip()

# Input message
message = input("> ")

# Process the message and print the result
print(replace_with_emojis(message))
