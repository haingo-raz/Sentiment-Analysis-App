# About 
A basic sentiment analysis app using Streamlit to build the interface and HuggingFaace transformers to perform sentiment analysis.

# Prerequisites
To run this project, you need to have the following prerequisites installed:

- Streamlit: You can install it by running `pip install streamlit`.
- Transformers: You can install it by running `pip install transformers`.

# Definitions
## Transformers
Transformers are a type of deep learning model that have revolutionized natural language processing (NLP) tasks. They are based on the attention mechanism and have achieved state-of-the-art performance on various NLP tasks such as machine translation, text summarization, and sentiment analysis.

Transformers are designed to handle sequential data, such as sentences or documents, by capturing the relationships between words or tokens. They are composed of an encoder and a decoder, which work together to process and generate sequences of tokens.

The transformer architecture uses self-attention mechanisms to capture dependencies between words in a sentence, allowing the model to focus on relevant parts of the input during processing.

## Hugging Face
HuggingFace transformers is a popular library that provides pre-trained transformer models and tools for fine-tuning them on specific NLP tasks.

## Hugging Face Pipelines
Hugging Face Pipelines is a high-level API provided by the HuggingFace transformers library. It allows you to easily use pre-trained transformer models for various NLP tasks without the need for extensive coding.

With Hugging Face Pipelines, you can perform tasks such as text classification, named entity recognition, question answering, and sentiment analysis with just a few lines of code. It abstracts away the complexities of model loading, tokenization, and inference, making it accessible even to users with limited NLP knowledge.
