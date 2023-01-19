#!pip install wordcloud
#!pip install fileupload
#!pip install ipywidgets
#!jupyter nbextension install --py --user fileupload
#!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
#from IPython.display import display
#import fileupload
import io
import sys

def upload():
    global file_contents
    filename = "C:\\temp\\PY\\go_she_must.txt"
    f = open(filename, "r")
    file_contents = f.read()
    f.close()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are",
                           "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but",
                           "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each",
                           "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    frequencies = {}
    for x in file_contents.split(" "):
        word = x.strip(punctuations).lower()
        if word not in uninteresting_words and word.isalpha():
            frequencies[word] = frequencies[word]+1 if word in frequencies else 1
    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


upload()
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()