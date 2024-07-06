# Invoice Extractor App

The Invoice Extractor App is a Streamlit-based application that leverages Google's Generative AI (Gemini) to analyze invoice images.
Users can upload invoice images and ask questions about their contents, with the AI providing intelligent responses based on the image data.

## Features

- Upload invoice images (JPG, JPEG, PNG)
- Ask questions about the invoice content
- Utilizes Google's Gemini AI model for information extraction
- User-friendly interface built with Streamlit

## Prerequisites

Before running this application, make sure you have the following:

- Python 3.6 or higher
- A Google API key for the Gemini model

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/invoice-extractor-app.git
   cd invoice-extractor-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

To run the application, use the following command:

```
streamlit run app.py
```

Then, open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

1. Upload an image of an invoice using the file uploader.
2. Enter your question about the invoice in the text input field.
3. Click the "SUBMIT" button to generate a response.
4. The app will display the extracted information based on your question.

## Dependencies

- google-generativeai
- streamlit
- python-dotenv
- langchain
- Pillow (PIL)

## Acknowledgements

- This project uses Google's Generative AI (Gemini) for invoice information extraction.
- Built with Streamlit for the web interface.
