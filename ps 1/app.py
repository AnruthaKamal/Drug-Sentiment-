import streamlit as st
import function
import json
with open('static_values.json', 'r') as json_file:
        loaded_static_val = json.load(json_file)
        word_columns = loaded_static_val['word_columns']
        unique_drugs = loaded_static_val['unique_drugs']
        unique_conditions = loaded_static_val['unique_conditions']

# Sample drug names and conditions
drug_names = ['Drug1', 'Drug2', 'Drug3']
conditions = ['Condition1', 'Condition2', 'Condition3']

# Get user inputs
st.title("Drug Sentiment Analyzer")

# Sidebar navigation
selected_page = st.sidebar.radio("Navigation", ["About", "Visualization", "Predict"])

# Display content based on the selected page
if selected_page == "About":
    st.header("About")
    st.write("""
This web application is designed to predict the sentiment of drug reviews based on user-provided information.
Users can input a review, select a drug name, and choose a medical condition to get predictions about the sentiment
of the given drug review.

### Key Features:
- **Input Fields:**
  - Users can enter their drug reviews in the provided text area.
  - Select the specific drug name and medical condition from dropdown menus.

- **Prediction:**
  - Clicking the "Predict" button triggers the sentiment prediction based on the review, drug name, and condition.
  - The application provides predictions for two sentiments: "Positive" or "Negative."

- **Machine Learning Model:**
  - The underlying machine learning model used for sentiment prediction is Logistic Regression.
  - Logistic Regression is a commonly used classification algorithm that works well for binary sentiment classification tasks.

- **Drug and Condition Information:**
  - The application is trained on a dataset with 588 unique drug names and 40 unique medical conditions.
  - It uses this information, along with the Logistic Regression model, to make predictions about the sentiment associated with a particular drug review.

### How to Use:
1. Navigate to the "Predict" tab.
2. Enter your drug review in the text area.
3. Select the drug name and medical condition from the dropdown menus.
4. Click the "Predict" button to get sentiment predictions.

Feel free to explore the other tabs, such as "Visualization," for additional insights and data exploration.
""")


elif selected_page == "Visualization":
    st.header("Visualization")
    screenshot_1 = 'pic1.png'
    screenshot_2 = 'pic2.png'
    screenshot_3 = 'pic3.png'
    screenshot_4 = 'pic4.png'
    screenshot_5 = 'pic3.png'
    screenshot_6 = 'pic6.png'
    screenshot_7 = 'pic7.png'
    screenshot_8 = 'pic8.png'
    screenshot_9 = 'pic9.png'
    screenshot_10 = 'pic10.png'


# Display screenshots
    st.image(screenshot_1, use_column_width=True)
    st.image(screenshot_2, use_column_width=True)
    st.image(screenshot_3, use_column_width=True)
    st.image(screenshot_4, use_column_width=True)
    st.image(screenshot_5, use_column_width=True)
    st.image(screenshot_6, use_column_width=True)
    st.image(screenshot_7, use_column_width=True)
    st.image(screenshot_8, use_column_width=True)
    st.image(screenshot_9, use_column_width=True)
    st.image(screenshot_10, use_column_width=True)



    #st.write("This is the visualization page. Add your data visualizations here.")

elif selected_page == "Predict":
    st.header("Predict")
    review = st.text_area("Enter your review:")
    selected_drug = st.selectbox("Select Drug Name:", unique_drugs)
    selected_condition = st.selectbox("Select Condition:", unique_conditions)
    predict_button = st.button("Predict")

    # Display the user inputs
    if predict_button:
        # Assuming you have a function named 'create_test_df' and 'make_predictions'
        test_df = function.create_test_df(review, selected_drug, selected_condition)
        pred = function.make_predictions(test_df)

        st.write("Review:", review)
        st.write("Selected Drug Name:", selected_drug)
        st.write("Selected Condition:", selected_condition)
        st.write("Prediction:", pred)