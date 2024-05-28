import streamlit as st
# Import the transformers library from HuggingFace
import transformers
from transformers import pipeline

# Set the logging level to error
transformers.logging.set_verbosity_error()

# Load a pipeline using a custom model from HuggingFace Hub
sentiment_classifier = pipeline(task="sentiment-analysis",
                                model="finiteautomata/bertweet-base-sentiment-analysis")

st.title('Sentiment Analysis using HuggingFace Transformers')

# User input
user_input = st.text_area("Please provide your text here", height=150)

# Button to analyze the sentiment
if st.button("Analyze Sentiment"):

    sentiment = sentiment_classifier(user_input)

    # Display the results
    st.write(sentiment)
    st.write(sentiment[0]['label'] + " sentiment with a confidence score of " + str(sentiment[0]['score'] * 100) + "%")