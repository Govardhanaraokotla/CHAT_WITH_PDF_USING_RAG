from flask import Flask, request, render_template
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
import pdfplumber
import os

app = Flask(__name__)

# Function to extract text from PDF
def extract_text_from_uploaded_pdf(pdf_file_path):
    pdf_content = []
    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                pdf_content.append(page_text)
    if not pdf_content:
        print("Error: No text found in the PDF.")
    return "\n".join(pdf_content)

# Function to split text into chunks
def divide_text_into_chunks(text_content, chunk_size=1000, overlap=200):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=chunk_size, chunk_overlap=overlap)
    return text_splitter.split_text(text_content)

# Create LangChain Document objects
def create_document_objects(text_chunks):
    return [Document(page_content=chunk) for chunk in text_chunks]

# Initialize embeddings
def initialize_text_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/multi-qa-mpnet-base-dot-v1")

# Create FAISS vector store
def build_vector_store_from_documents(document_objects, embedding_model):
    return FAISS.from_documents(document_objects, embedding_model)

# Initialize global variables
faiss_vector_store = None

@app.route("/", methods=["GET", "POST"])
def home():
    global faiss_vector_store
    query_results = []

    if request.method == "POST":
        # Step 1: Handle File Upload
        if "file" in request.files:
            uploaded_file = request.files["file"]
            if uploaded_file.filename.endswith(".pdf"):
                uploaded_pdf_path = os.path.join("uploads", uploaded_file.filename)
                os.makedirs("uploads", exist_ok=True)
                uploaded_file.save(uploaded_pdf_path)

                # Step 2: Extract, Chunk, and Store
                extracted_text = extract_text_from_uploaded_pdf(uploaded_pdf_path)
                if extracted_text.strip():
                    text_chunks = divide_text_into_chunks(extracted_text)
                    document_objects = create_document_objects(text_chunks)
                    embedding_model = initialize_text_embeddings()
                    faiss_vector_store = build_vector_store_from_documents(document_objects, embedding_model)
                else:
                    return render_template("index.html", results=["Error: No text found in the PDF."])

        # Step 3: Handle Query
        user_query = request.form.get("query")
        if user_query and faiss_vector_store:
            retriever = faiss_vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 1})
            retrieved_documents = retriever.get_relevant_documents(user_query)

            # Debugging: Print retrieved results
            print(f"User Query: {user_query}")
            if retrieved_documents:
                for index, document in enumerate(retrieved_documents, start=1):
                    print(f"Result {index}: {document.page_content[:200]}")  # Print first 200 characters
                query_results = [doc.page_content for doc in retrieved_documents]
            else:
                print("No relevant documents found.")

    return render_template("index.html", results=query_results)
if __name__ == "__main__":
    app.run(debug=True)