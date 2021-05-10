import pandas as pd
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import unicodedata
import re

#~~~~~~~~~~~~~~~acquire_csv~~~~~~~~~~~~~~~~~~~~~~~

def acquire_csv():
    
    df = pd.read_csv(r'f1_readmes.csv')
    
    return df


#~~~~~~~~~~~~~~~initial_clean~~~~~~~~~~~~~~~~~~~~~~~

def first_clean():
    
    
    # acquire the csv by running the acquire_csv function. make sure the csv is in your local folder
    df = acquire_csv()
    
    
    # drops the nulls located in the readme_contents column
    null_readme = df[df['readme_contents'].isnull()].index
    
    df.drop(null_readme , inplace=True)
    
    # keeps only those rows that are nulls in language column    
    df = df[df['language'].notna()]
      
    # drop written languages that are included in less than 6 repositories
    
    drop_written_languages = df[df['written_language'].map(df['written_language'].value_counts()) < 6].index
    
    df.drop(drop_written_languages , inplace=True)
    
    # drop languages that have less than 7 repositories
    drop_languages = df[df['language'].map(df['language'].value_counts()) < 7].index
    
    df.drop(drop_languages , inplace=True)
    
    return df

#~~~~~~~~~~~~~~~~~NLP_clean_function~~~~~~~~~~~~~~~

def clean_nlp(readme_contents):
    
    'A simple function to cleanup text data'
    
    ADDITIONAL_STOPWORDS = ['r', 'u', '2', 'ltgt', '\n', 'ha']
    
    wnl = nltk.stem.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english') + nltk.corpus.stopwords.words('portuguese') + nltk.corpus.stopwords.words('spanish') + nltk.corpus.stopwords.words('french') + ADDITIONAL_STOPWORDS
    readme_contents = (unicodedata.normalize('NFKD', readme_contents)
             .encode('ascii', 'ignore')
             .decode('utf-8', 'ignore')
             .lower())
    words = re.sub(r'[^\w\s]', '', readme_contents).split()
    return [wnl.lemmatize(word) for word in words if word not in stopwords]


