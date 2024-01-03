# Drug Sentiment Analyzer

## Project Overview

**Project Title:** Drug Sentiment Analyzer

### Dataset Information
- The dataset comprises the following columns: `drugname`, `condition`, `review`, and `sentiment`.
- The dataset is balanced, with an equal representation of positive and negative sentiments.

### Text Preprocessing
- Text preprocessing involved the following steps:
  - Removal of stop words.
  - Elimination of punctuation.
  - Stemming to reduce words to their base form.
  - Tokenization to break down text into individual words.
- After preprocessing, the dataset revealed 17,000 unique words.

### Feature Extraction
- Feature extraction was performed by considering the most frequently used 1000 words after text preprocessing.
- These words were treated as features, and each review was represented by a binary vector indicating the presence (1) or absence (0) of each word.

### Categorical Data Encoding
- For categorical columns such as `condition` and `drugname`, one-hot encoding was applied to convert them into a numerical format suitable for model training.

### Model Training
- Four different algorithms were considered for model training: Support Vector Machine (SVM), Naive Bayes, Logistic Regression (LR), and k-Nearest Neighbors (KNN).
- After training, Logistic Regression outperformed other algorithms in terms of accuracy and performance.

### Deployment using Streamlit
- The Drug Sentiment Analyzer has been deployed using Streamlit.
- You can access the deployed application [here](https://drugsentiment.streamlit.app/).


## Conclusion
The Drug Sentiment Analyzer successfully analyzes sentiments associated with drug reviews. Logistic Regression stands out as the most effective model for this specific task, providing accurate predictions.


