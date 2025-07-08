# This is a script which I need to setup to run before my main.py, downloads my necessary nltk files 

# punkt - a tokenizer that will split my text into words or sentences
# stopwords - downloads simple common words that can be ignored
# wordnet - downloads wordnet database that is used for "Lemmatisation" which can turn words such as going to go

## This line tells python to download my files only if my main file is run directly, not when its imported
import nltk

##I need to define what I want my function to do  
def download_nltk_data() :
  try:
    print("Downloading necessary files. ")
    nltk.download('punkt')  
    nltk.download('stopwords')
    nltk.download('wordnet')
    print("The necessary files have been successfully downloaded! ")
    
## Except function in case something goes wrong such as disconnecting, logs the issue
  except Exception as e:
    print(f"An Error has occurred whilst downloading: {e}")
    

## This line tells python to download my files only if my main file is run directly, not when its imported.
if __name__ == "_ _main__" 
          download_nltk_data ()
