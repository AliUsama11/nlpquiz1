!pip install nltk streamlit
import streamlit as st
import nltk
from nltk import bigrams, trigrams
from nltk.tokenize import word_tokenize
# Download NLTK resources (if not downloaded)
nltk.download('punkt')

def generate_ngrams(text, n):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Generate n-grams based on 'n'
    if n == 2:
        n_grams = list(bigrams(tokens))
    elif n == 3:
        n_grams = list(trigrams(tokens))
    else:
        st.warning("Unsupported 'n'. Please choose 2 for bigrams or 3 for trigrams.")
        return []
    
    return n_grams

def main():
    st.title('N-Gram Extractor')
    
    # User input for text passage
    user_input = st.text_area('Enter text here:', height=200)
    
    # User choice for n-gram type
    n = st.selectbox('Select n-gram type:', [2, 3])
    
    # Extract n-grams upon button click
    if st.button('Extract N-Grams'):
        if user_input:
            n_grams = generate_ngrams(user_input, n)
            st.write(f'{n}-grams extracted:')
            for gram in n_grams:
                st.write(gram)
        else:
            st.warning('Please enter text to extract n-grams.')

if __name__ == "__main__":
    main()
