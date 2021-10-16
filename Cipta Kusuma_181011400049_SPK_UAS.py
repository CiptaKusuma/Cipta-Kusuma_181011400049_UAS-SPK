from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer


from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

input_words = ['writing','written','wrote','friends','friendship','friendly',
              'connect','connected']

portstemmer_obj = PorterStemmer()
lancaster_obj = LancasterStemmer()
snowball_obj = SnowballStemmer('english')

wordnet_lemmatizer = WordNetLemmatizer()

import pandas as pd

port_result = [portstemmer_obj.stem(w) for w in input_words]
lancaster_result = [lancaster_obj.stem(w) for w in input_words]
snowball_result = [snowball_obj.stem(w) for w in input_words]

lemmatize_result_v = [wordnet_lemmatizer.lemmatize(w, pos='v') for w in input_words]
lemmatize_result_n = [wordnet_lemmatizer.lemmatize(w, pos='n') for w in input_words]

pd.DataFrame({
'input_word' : input_words,
'port' : port_result,
'lancaster' : lancaster_result,
'snowball' : snowball_result,
'lemmatizer Verb' : lemmatize_result_v,
'lemmatizer Noun' : lemmatize_result_n
})