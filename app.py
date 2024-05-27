import streamlit as st

def main():
    st.set_page_config(page_title="PDFChat", page_icon=":books:")

    st.header("Chat with your own PDFs :books:")
    st.text_input("Ask anything about your PDFs:")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDFs and click the Process button")
        st.button("Process")

if __name__ == '__main__':
        main()