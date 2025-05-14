from llama_index.core import SimpleDirectoryReader
from llama_index.core import Document
import sys
import os
from PyPDF2 import PdfReader
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exception import customexception
from logger import logging

def load_data(uploaded_file):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        # logging.info("data loading started...")
        # loader = SimpleDirectoryReader("Data")
        # document=loader.load_data()
        # logging.info("data loading completed...")
        # return document

        logging.info("Data loading started...")
        if uploaded_file is None:
            raise ValueError("No file uploaded.")
        
        # Read the uploaded PDF
        pdf = PdfReader(uploaded_file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        
        # Convert to LlamaIndex Document
        document = [Document(text=text)]
        logging.info("Data loading completed...")
        return document
    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)



    