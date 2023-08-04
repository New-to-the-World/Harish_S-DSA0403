import string

def tokenize_text(text):
    # Basic tokenization by splitting on whitespaces
    return text.split()

def remove_punctuation(word):
    # Remove punctuation from a word
    return word.translate(str.maketrans('', '', string.punctuation))

def count_word_frequency(tokens):
    word_freq = {}
    for token in tokens:
        # Remove punctuation and convert to lowercase
        word = remove_punctuation(token.lower())
        if word:
            # Increment the word count in the dictionary
            word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def main():
    # Step 1: Read the text document
    with open("C:/Users/mailm/Downloads/sample_text.txt", "r") as file:
        text = file.read()

    # Step 2: Tokenize the text
    tokens = tokenize_text(text)

    # Step 3: Calculate word frequency
    word_freq = count_word_frequency(tokens)

    # Step 4: Display the frequency distribution
    print("Word Frequency Distribution:")
    for word, frequency in word_freq.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
