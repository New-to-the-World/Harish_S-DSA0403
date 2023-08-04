import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import matplotlib.pyplot as plt

file_path = 'C:/Users/mailm/Downloads/data.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Function to preprocess the text data
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    processed_text = " ".join(filtered_tokens)
    return processed_text

# Apply preprocessing to the 'feedback' column in the DataFrame
df['processed_feedback'] = df['feedback'].apply(preprocess_text)

# Calculate the frequency distribution of words in the preprocessed dataset
word_freq_dist = nltk.FreqDist(
    word_tokenize(" ".join(df['processed_feedback']))
)

# Function to display the top N most frequent words and their frequencies
def display_top_words(freq_dist, top_n):
    top_words = freq_dist.most_common(top_n)
    print(f"Top {top_n} most frequent words:")
    for word, freq in top_words:
        print(f"{word}: {freq}")

# User input for N (number of top words to display)
try:
    N = int(input("Enter the number of top words to display: "))
    display_top_words(word_freq_dist, N)

    # Plot a bar graph to visualize the top N most frequent words and their frequencies
    top_words, frequencies = zip(*word_freq_dist.most_common(N))
    plt.figure(figsize=(10, 6))
    plt.bar(top_words, frequencies)
    plt.xlabel('Words')
    plt.ylabel('Frequencies')
    plt.title(f'Top {N} Most Frequent Words')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
except ValueError:
    print("Invalid input. Please enter a valid integer for N.")
