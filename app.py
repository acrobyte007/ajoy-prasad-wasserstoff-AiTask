import requests
from bs4 import BeautifulSoup
import streamlit as st
from transformers import pipeline

# URL input
url = st.text_input("Enter the URL")

# Initialize context
context = ""

# If URL is provided, scrape the webpage
if url:
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all paragraphs containing the text of the stories
            paragraphs = soup.find_all('p')

            # Extract and concatenate the text from the paragraphs
            context = " ".join([paragraph.get_text(strip=True) for paragraph in paragraphs if paragraph.get_text(strip=True)])


        else:
            st.error(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Set up the Streamlit app
st.title("Question Answering App")
st.write("This app allows you to input a context and ask questions based on that context.")

# Load the pre-trained question-answering pipeline
qa_pipeline = pipeline("question-answering")

# Check if context is provided
if context:
    # Provide instructions to the user
    st.write("You can now ask questions based on the provided context.")

    # Input question from the user
    question = st.text_input("Please enter your question:")

    # Check if question is provided
    if question:
        try:
            # Get the answer from the model
            result = qa_pipeline(question=question, context=context)

            # Display the answer
            st.write(f"**Answer:** {result['answer']}")
        except Exception as e:
            st.error(f"An error occurred during question answering: {e}")
else:
    st.write("Please provide a valid URL to extract context.")