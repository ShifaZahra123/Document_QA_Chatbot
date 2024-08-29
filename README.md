[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-0E86D4)](https://streamlit.io/)
![Language](https://img.shields.io/badge/Language-Python-0000FF)
[![Model](https://img.shields.io/badge/Model-Llama3--8b--8192-FF8C00)](https://groq.com/groundbreaking-gemma-7b-performance-running-on-the-groq-lpu-inference-engine/)
[![Embeddings](https://img.shields.io/badge/Embeddings-Google%20Generative%20AI-00C853)](https://ai.google.dev/)
[![API](https://img.shields.io/badge/API-Google%20Gemini%20API-0000FF)](https://ai.google.dev/gemini-api/docs)
[![API](https://img.shields.io/badge/API-Groq%20API-FF8C00)](https://groq.com/)

## Project Name: **Gemma Model Document Q&A**

This repository contains the source code for the **Gemma Model Document Q&A** web application, developed and deployed using Streamlit. The app allows users to ask questions related to specific documents, and it retrieves the most relevant answers based on the context provided by the documents.

## Features
1. **Document Ingestion**: Load and preprocess PDF documents from a specified directory.
2. **Vector Embedding**: Convert document chunks into vector embeddings using Google Generative AI Embeddings.
3. **Question Answering**: Answer user queries by retrieving relevant document chunks and generating context-based responses using the Llama3-8b-8192 model.

## How to Use the Web Application
1. Open the web application using Streamlit.
2. Click on the "Documents Embedding" button to preprocess the PDF documents and store them in a vector database.
3. Enter your question in the provided text input box.
4. The application will retrieve the most relevant document sections and generate an accurate response based on the context.

## Dataset
The PDF documents used in this application are loaded from a local directory (`./us_census`). Ensure that your documents are placed in this directory before running the application.

### Sample Application Workflow
![Workflow](Sample-Images/Workflow.PNG)

## Installation
To set up the application locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/ShifaZahra123/gemma-doc-qa.git
   ```
2. Navigate to the project directory:
   ```sh
   cd gemma-doc-qa
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the environment variables:
   - Create a `.env` file in the project root directory and add your `GROQ_API_KEY` and `GOOGLE_API_KEY`.

5. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
