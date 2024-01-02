import json
import pandas as pd
import numpy as np
import nltk
import string
import re
import pickle

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
nltk.download('stopwords')

def to_lower(text):
  return text.lower()

def tokenize(text):
  return text.split()

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_stopwords(words):
    stop_words = set(stopwords.words("english"))
    filtered_text = [word for word in words if word not in stop_words]
    return filtered_text

def stem_words(words):
    stems = [stemmer.stem(word) for word in words]
    return stems

def text_preprocessing(text):
  text = to_lower(text)
  text = remove_punctuation(text)
  words = tokenize(text)
  words = remove_stopwords(words)
  words = stem_words(words)
  return words

def bag_of_words(corpus):
  bog = {}
  for i in corpus:
    for j in i:
      if j not in bog:
        bog[j] = 1
      else:
        bog[j] +=1
  return bog

def one_hot_encode(df,unique_drugs,unique_conditions):
    # Create a set of unique values for drugName and condition
    # Create a copy of the original DataFrame
    encoded_df = df.copy()
    # Create new binary columns for each unique value in drugName
    for drug in unique_drugs:
        encoded_df[drug] = (df['drugName'] == drug).astype(int)
    # Create new binary columns for each unique value in condition
    for condition in unique_conditions:
        encoded_df[condition] = (df['condition'] == condition).astype(int)
    # Drop the original 'drugName' and 'condition' columns
    encoded_df = encoded_df.drop(['drugName', 'condition'], axis=1)
    return encoded_df

def create_new_df(df,bog):
  res = []
  for i in df["preprocessed_text"] :
    temp = [0] * len(bog)
    for j in bog:
      if j in i :
        temp[bog.index(j)] = 1
    res.append(temp)
  df1 = pd.DataFrame(res,columns=bog)
  df = pd.concat([df1, df], axis=1)
  return df

def create_test_df(review,drugName,condition):
    data = {'drugName': drugName,
            'condition': condition,
            'review': review}
    print(data)

    # Create a DataFrame with one row
    test_df = pd.DataFrame(data,index=[0])
    with open('static_values.json', 'r') as json_file:
        loaded_static_val = json.load(json_file)
        word_columns = loaded_static_val['word_columns']
        unique_drugs = loaded_static_val['unique_drugs']
        unique_conditions = loaded_static_val['unique_conditions']

    # Display the DataFrame
    #test_df = create_new_df(df,word_columns)
    test_preprocessed = []
    test_preprocessed.append(text_preprocessing(test_df["review"][0]))
    test_df["preprocessed_text"] = list(test_preprocessed)
    ohc_test =  one_hot_encode(test_df,unique_drugs,unique_conditions)
    test_df_bog =  create_new_df(ohc_test,word_columns)
    test_df_bog = test_df_bog.drop(columns=["review","preprocessed_text"])
    return test_df_bog

def make_predictions(X_test):
   model_filename = "logistic_regression_model (1).pkl"
   with open(model_filename, 'rb') as model_file:
    loaded_LR = pickle.load(model_file)
   predictions = loaded_LR.predict(X_test)
   return predictions[0]
# print("Loaded JSON contents:")
# print(loaded_static_val['word_columns'])
