import streamlit as st

import csv
import matplotlib.pyplot as plt
import os
import pandas as pd
import re
import zipfile

import fitz
import nltk
import pdfplumber
import pytesseract

from collections import Counter
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
from wordcloud import WordCloud

nltk.download('stopwords')

uploaded = {} # to hold files and file info after uploading
INDIVIDUAL_WORD_CLOUDS = False
CONTAINS_SCANNED_PDFS = False # Set to true if you know your data contains scanned documents, but you cannot specify which are scanned
SCANNED_PDFS_TAGGED = False # Only set to True if you have named ALL scanned PDFs correctly i.e. file name ends with _scanned.pdf

# Add file uploader
uploaded_files = st.file_uploader(
    "Add your reference PDF files:", accept_multiple_files=True)

combine_wordcloud = st.checkbox('Combine Wordclouds')

def create_word_cloud(text, title):
    # Removing non-alphanumeric characters in string
    re_pattern = re.compile(r'[^\w\s]', re.UNICODE)
    text = re_pattern.sub('', text)

    # Remove unnecessary words (stop words) like "the", "and", etc.
    words_to_count = text.split() # Split sentence into list of words
    stop_word_set = set(stopwords.words('english'))
    words_to_count = [word for word in words_to_count if word not in stop_word_set] # Remove stop words

    # Count the words using Python's Counter
    word_cloud_dict = Counter(words_to_count)

    # Save word counts to CSV file
    # with open(f"./output/{title}.csv",'w') as csvfile:
    #   fieldnames=["word", "count"]
    #   writer=csv.writer(csvfile)
    #   writer.writerow(fieldnames)
    #   for key, value in word_cloud_dict.items():
    #       writer.writerow([key, value]) 

    wordcloud = WordCloud(
                      max_font_size=40, 
                      background_color="white"
                    ).generate_from_frequencies(word_cloud_dict)
    
    fig, ax = plt.subplots()
    # ax.figure(figsize=(16, 10))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    ax.set_title(title)

    st.pyplot(fig)


def get_combined_cloud(uploaded_files):
    files_text = ""
    for uploaded_file in uploaded_files:
        with fitz.open(stream=uploaded_file.read()) as doc:
            for page in doc.pages():
                extracted_text = page.get_text()
                # If no text was found, assume page was scanned and treat as picture
                if len(extracted_text) == 0:
                    pix = page.get_pixmap()
                    output = "outfile.png"
                    pix.save(output)
                    files_text += (pytesseract.image_to_string('outfile.png').lower() + " ")
                    os.remove("./outfile.png")
                else:
                    files_text += (extracted_text + " ")
    create_word_cloud(files_text, "combined Word Cloud")

def get_individual_clouds(uploaded_files):
    for uploaded_file in uploaded_files:
        single_file_text = ""
        with fitz.open(stream=uploaded_file.read()) as doc:
            for page in doc.pages():
                extracted_text = page.get_text()
                # If no text was found, assume page was scanned and treat as picture
                if len(extracted_text) == 0:
                    pix = page.get_pixmap()
                    output = "outfile.png"
                    pix.save(output)
                    single_file_text += (pytesseract.image_to_string('outfile.png').lower() + " ")
                    os.remove("./outfile.png")
                else:
                    single_file_text += (extracted_text + " ")
            create_word_cloud(single_file_text, uploaded_file.name)
    

if st.button('Generate'):
    if combine_wordcloud:
        get_combined_cloud(uploaded_files)
    else:
        get_individual_clouds(uploaded_files)
