import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
     

def main():
    load_dotenv()
    st.set_page_config(page_title="PDFChat", page_icon=":books:")

    st.header("Chat with your own PDFs :books:")
    st.text_input("Ask anything about your PDFs:")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs and click the Process button", accept_multiple_files=True)
        if st.button("Process"):
             with st.spinner("Processing"):
                  #get pdf data
                  raw_text = get_pdf_text(pdf_docs)
                  st.write(raw_text)
                  #get text chunks

                  #create vector store out of embeddings

if __name__ == '__main__':
        main()