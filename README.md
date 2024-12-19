---

# 💬 Chat with PDF Using RAG 

Interact with your PDF documents like never before! **Chat with PDF 2** makes it easy to upload, process, and query PDFs with the power of natural language processing and semantic search.

---

## ✨ Highlights
- 🖇️ **Effortless PDF Upload**: Just drag and drop your PDFs, and you're ready to go.
- 🧠 **AI-Powered Text Search**: Quickly find the information you need using semantic similarity.
- 🖹 **Smart Text Chunking**: Splits large content into manageable pieces for accurate querying.
- ⚡ **Lightning-Fast Search**: Powered by FAISS vectorization for instant results.

---

## 🏗️ Project Layout
```plaintext
Chat_With_PDF_2/
├── templates/
│   └── index.html          # Web interface for user interaction
├── uploads/                # Stores user-uploaded PDFs
├── app.py                  # The Flask-powered backend application
├── charts.pdf              # Example input PDF
├── Sthafal-project-tasks.pdf # Another sample PDF for testing
```

---

## 🚀 Getting Started

### 1️⃣ Installation
- Clone this repository:
  ```bash
  git clone https://github.com/your-username/Chat-With-PDF-2.git
  cd Chat-With-PDF-2
  ```
- Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 2️⃣ Running the App
- Start the server:
  ```bash
  python app.py
  ```
- Open your browser and go to:
  ```
  http://127.0.0.1:5000/
  ```

### 3️⃣ Upload and Query
1. Upload a PDF file.
2. Type your query and retrieve contextually relevant information in seconds!

---

## 🖼️ Visual Demo
### Home Page
🚀 **Upload your file here:**

![WhatsApp Image 2024-12-19 at 21 45 01_14d619b4](https://github.com/user-attachments/assets/bb558aad-f74c-44c2-8b33-1f52da23dd17)

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3
- **Backend**: Python + Flask
- **AI Models**: HuggingFace Transformers (`sentence-transformers/multi-qa-mpnet-base-dot-v1`)
- **PDF Parsing**: `pdfplumber`
- **Search Engine**: FAISS (Facebook AI Similarity Search)

---

## 🧩 How It Works
1. **📂 Upload PDFs**: Select any PDF file for text extraction.
2. **🔍 Extract & Index**: The app processes the text, splits it into meaningful chunks, and indexes them.
3. **🤔 Query**: Enter any query, and the system retrieves the most relevant content.

---

## 🌟 Planned Features
- 🌐 Deploy to the cloud (AWS, GCP, or Heroku).
- 🖋️ Add support for additional file formats (e.g., DOCX, TXT).
- 🔒 Implement user authentication for personalized experiences.

---

## 👩‍💻 Contribute
Want to make this better? Here’s how:
- Fork the repository
- Submit your pull requests with meaningful comments
- Report bugs or request features via GitHub Issues

---

## 💡 Inspiration
This project is a step toward simplifying interactions with unstructured document data. Whether it’s research papers, reports, or invoices—unlock the potential of your PDFs!

---

## 🏆 Acknowledgments
- [HuggingFace](https://huggingface.co/) for their powerful NLP models.
- [FAISS](https://github.com/facebookresearch/faiss) for efficient similarity search.

---


