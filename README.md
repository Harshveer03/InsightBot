Great! Here's the full markdown text for your `README.md` file — ready to be copied and pasted directly into your GitHub repository:

---

```markdown
# 🤖 InsightBot

**InsightBot** is an end-to-end AI-powered Visual Question Answering (VQA) system that allows users to upload a PDF or image file and ask contextual questions about its content. It uses advanced deep learning models like **BLIP** (Bootstrapped Language-Image Pretraining) for image-based Q&A and extracts textual information from PDFs using **pdfplumber**.

---

## 🚀 Features

- 📄 Upload PDF documents or 🖼️ image files (JPG, PNG)
- 💬 Ask natural language questions about the uploaded content
- 🧠 AI-based contextual answers using **BLIP-VQA**
- ⚙️ Fast backend built with **Flask**
- 🌐 Clean UI with **Streamlit** frontend
- 🔗 Ready for GitHub and LinkedIn showcasing

---

## 🧠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Flask, pdfplumber
- **AI Model:** [Salesforce BLIP VQA Base](https://huggingface.co/Salesforce/blip-vqa-base)
- **Languages:** Python 3.10+

---

## 📁 Project Structure
```

InsightBot/
│
├── backend/
│ ├── app.py # Flask backend
│ ├── utils.py # PDF and image processing, BLIP model
│ └── requirements.txt # Python dependencies
│
├── frontend/
│ └── streamlit_app.py # Streamlit frontend app
│
├── uploaded_files/ # Temporary uploaded file storage
│
└── README.md

````

---

## ⚙️ Setup Instructions

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/InsightBot.git
cd InsightBot
````

### ✅ Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### ✅ Step 3: Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### ✅ Step 4: Run the Flask Backend

```bash
python app.py
```

> By default, the backend will run at `http://localhost:5000`

### ✅ Step 5: Run the Streamlit Frontend

Open a new terminal and run:

```bash
cd frontend
streamlit run streamlit_app.py
```

> Frontend runs on `http://localhost:8501`

---

## 🧪 Example Use

1. Upload a **PDF** or **Image**
2. Ask a question like:

   - _“What is the title of this project?”_
   - _“Who supervised this thesis?”_

3. Get an accurate response powered by BLIP or PDF parser.

## 🌐 Future Enhancements

- OCR support for scanned PDFs
- Chat history and context memory
- Support for multi-page PDFs
- Deployable via Docker / Streamlit Cloud

---

## 👨‍💻 Author

**Harshveer Singh**
Final-year B.Tech AIML student
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/harshveer-singh-1a6912205/)
[![GitHub](https://img.shields.io/badge/GitHub-black?style=flat&logo=github)](https://github.com/Harshveer03)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
