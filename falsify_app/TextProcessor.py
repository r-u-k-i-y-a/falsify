# General imports
from collections import defaultdict

# Imports from NLTK for NLP
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


class TextProcessor:

    # Function to clean and tokenize a give string column
    def tokenize_string_column(self, column_name):
        # Remove empty rows if available
        self[f'{column_name}'].dropna(inplace=True)

        # Convert string to lower case
        self[f'{column_name}'] = self[f'{column_name}'].str.lower()

        # Tokenize string
        self[f'{column_name}'] = [word_tokenize(str(text)) for text in self[f'{column_name}']]

        return self

    # Text cleaning functionalities using NLP techniques
    def clean_string_column(self, column_name):
        # Set up parts of speech tagging
        tag_map = defaultdict(lambda: wn.NOUN)
        tag_map['J'] = wn.ADJ
        tag_map['V'] = wn.VERB
        tag_map['R'] = wn.ADV

        # Loop each set of words in a review
        for index, review in enumerate(self[f'{column_name}']):
            # Final set of words to return
            results = []

            # Word new lemmatizer
            lemmatizer = WordNetLemmatizer()

            # Remove stop words,alpha numeric characters and set POS tag
            for word, tag in pos_tag(review):
                if word not in stopwords.words('english') and word.isalpha():
                    final_str = lemmatizer.lemmatize(word, tag_map[tag[0]])
                    results.append(final_str)

            # Set final set of words to column
            self.loc[index, f'{column_name}'] = str(results)

        return self
