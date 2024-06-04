import os
import glob
import nltk
from nltk.tokenize import word_tokenize

# Download the tokenizer data
nltk.download('punkt')

def read_markdown_files(directory):
    # Read all markdown files from the directory
    md_files = glob.glob(os.path.join(directory, '*.md'))
    all_text = ''
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            all_text += file.read() + ' '  # Add a space to separate file contents
    return all_text

def tokenize_text(text):
    # Tokenize the text using NLTK's word_tokenize
    tokens = word_tokenize(text)
    return tokens

def tokenize_and_count_tokens(text):
    """
    Tokenizes the input text and counts the total number of tokens.
    
    Args:
    text (str): The text to be tokenized.
    
    Returns:
    list: A list of tokens.
    int: The total number of tokens.
    """
    tokens = word_tokenize(text)
    return tokens, len(tokens)

if __name__ == "__main__":
    # Directory containing the markdown files
    directory = '~/UNI/3ºAno/inteligenciaArtificial/cadernosAI/' 

    # Read and concatenate markdown files
    concatenated_text = read_markdown_files(directory)

    # Tokenize the concatenated text
    tokens = tokenize_text(concatenated_text)

    # Count the total number of tokens
    tokens, total_tokens = tokenize_and_count_tokens(tokens)

    print(f'Total number of tokens: {total_tokens}')
    print(f'Tokens: {tokens}')
