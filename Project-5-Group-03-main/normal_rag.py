import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import PyPDF2
import io
from config import OLLAMA_BASE_URL, OLLAMA_MODEL

class NormalRAG:
    def __init__(self):
        """Initialize the RAG components"""
        self.llm = OllamaLLM(
            base_url=OLLAMA_BASE_URL,
            model=OLLAMA_MODEL
        )
        
        self.embeddings = OllamaEmbeddings(
            base_url=OLLAMA_BASE_URL,
            model=OLLAMA_MODEL
        )
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        
        self.vectorstore = None
        self.qa_chain = None
        
    def process_document(self, uploaded_file) -> str:
        """Process uploaded document"""
        try:
            # Get file extension
            file_extension = uploaded_file.name.split('.')[-1].lower()
            
            if file_extension == 'txt':
                text = uploaded_file.read().decode('utf-8')
            elif file_extension == 'pdf':
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
            else:
                return f"Unsupported file extension: {file_extension}"
            
            # Split text into chunks
            texts = self.text_splitter.split_text(text)
            
            # Create vector store
            self.vectorstore = FAISS.from_texts(
                texts,
                self.embeddings
            )
            
            # Create QA chain
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vectorstore.as_retriever(
                    search_kwargs={"k": 3}
                )
            )
            
            return f"Document processed successfully. Created {len(texts)} chunks."
            
        except Exception as e:
            error_msg = f"Error processing document: {str(e)}"
            print(error_msg)
            return error_msg
    
    def query(self, question: str) -> str:
        """Query the processed document"""
        try:
            if not self.qa_chain:
                return "Please process a document first!"
            
            # Use invoke instead of run
            response = self.qa_chain.invoke({"query": question})
            
            # Extract the answer from the response
            if isinstance(response, dict) and "result" in response:
                return response["result"]
            
        except Exception as e:
            error_msg = f"Error querying document: {str(e)}"
            print(error_msg)
            return error_msg