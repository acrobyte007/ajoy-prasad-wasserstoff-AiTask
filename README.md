# Question Answering App

This Streamlit app allows users to input a URL and ask questions based on the text extracted from that webpage. It utilizes the BERT from transformers library for question answering and `BeautifulSoup` for web scraping.

## Setup

1. Clone the repository.
2. Install the dependencies by running `pip install -r requirements.txt`.
3. Run the app with Streamlit: `streamlit run app.py`.

## Usage

1. Provide a URL in the input box.
2. Wait for the app to extract the text from the webpage.
3. Once the text is extracted, input your question in the provided box.
4. The app will display the answer based on the input question and extracted context.

## Dependencies

- `beautifulsoup4==4.10.0`: For parsing HTML content.
- `requests==2.26.0`: For sending HTTP requests to retrieve webpage content.
- `streamlit==1.5.0`: For building and running the Streamlit app.
- `transformers==4.11.3`: For utilizing pre-trained question-answering models.


