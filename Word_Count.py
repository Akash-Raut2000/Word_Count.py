def count_words(text):
    # Split the text into words using whitespace as a delimiter
    words = text.split()
    return len(words)

# Get input text from the user
text = input("Enter some text: ")

# Call the count_words function to count the words
word_count = count_words(text)

# Display the word count
print(f"Word count: {word_count}")