import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

def process_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in stop_words]
    keywords = set(tokens)
    command = find_closest_command(keywords)
    return command

def find_closest_command(keywords):
     return command

while True:
    text = input("Enter text: ")
    command = process_text(text)
    print("Nearest command:", command)

