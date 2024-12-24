---

# **Graph-Based Retrieval-Augmented Generation (RAG)**

This project explores the implementation of **GraphRAG** and **LightRAG**, advanced Retrieval-Augmented Generation systems that integrate knowledge graphs for enhanced query performance. The project focuses on understanding, setting up, and experimenting with these systems.

---

## **📂 Project Overview**

### Key Features:
1. **Normal RAG**: Vector-based retrieval for general Q&A.
2. **GraphRAG**: Utilizes knowledge graphs for complex, relationship-based queries.
3. **LightRAG**: Optimized for lightweight and local processing.

### Tools and Libraries:
- Python 3.10 or later
- Neo4j (Graph database)
- FAISS (Vector database)
- spaCy (NER for relationship extraction)
- Ollama (LLM integration)
- Streamlit (Interactive UI)

---

## **📦 Project Setup**

### **1. Repository Clone**
```bash
git clone https://github.com/<course-github>/GraphBased-RAG.git
cd GraphBased-RAG
```

### **2. Install Dependencies**
Install Python packages and spaCy model:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### **3. LLM Model Pull (Ollama)**
```bash
ollama pull llama3.2:1b
```

### **4. Neo4j Docker Setup**
```bash
docker run \
--name neo4j \
-p 7474:7474 -p 7687:7687 \
-d \
-e NEO4J_AUTH=neo4j/password123 \
neo4j:latest
```

---

## **⚙️ Running the Application**

### **1. Start Streamlit Application**
Launch the interactive UI:
```bash
streamlit run app.py
```

### **2. Select RAG Implementation**
Choose from:
- **Normal RAG**: General question answering using FAISS and embeddings.
- **GraphRAG**: Graph-based question answering with Neo4j.
- **LightRAG**: Efficient, local processing.

### **3. Upload Document**
- Supported formats: **PDF, CSV**.
- Automatic text extraction and processing.

### **4. Query the System**
Enter a natural language query. For example:
- Normal RAG: *“What is melange in Dune?”*
- GraphRAG: *“What is the relationship between House Atreides and the Emperor?”*

### **5. Graph Visualization (GraphRAG)**
View entity relationships and communities in Neo4j.

---


## **🌐 File Structure**
```plaintext
GraphBased-RAG/
├── app.py                # Streamlit application
├── normal_rag.py         # Normal RAG logic
├── graphrag.py           # GraphRAG implementation
├── lightrag.py           # LightRAG implementation
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## **💡 Tips for Execution**
- Start with **Normal RAG** to understand basic functionality.
- Use small datasets for testing GraphRAG to avoid indexing delays.
- Test queries across all implementations for comparative analysis.

---

## **📜 Deliverables**
1. **Report**: A PDF detailing installation, execution, and findings.
2. **Presentation**: Highlights of features and results.
3. **GitHub Repository**: Well-documented code and instructions.

For any queries or issues, refer to the project documentation or reach out via GitHub.

--- 

## Screenshots

![graph](https://github.com/user-attachments/assets/4828cf1a-0bc7-43a8-a19d-032b5b47fe0a)
![graph(1)](https://github.com/user-attachments/assets/2a22b30e-6260-4bbf-adc8-2130abe6369e)
![graph(2)](https://github.com/user-attachments/assets/61db11d9-38c5-4b8a-b3ef-afddbceced09)
![graph(3)](https://github.com/user-attachments/assets/61656952-531e-4e11-84a8-ba4b8b351ea2)

