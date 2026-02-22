# 📞 AI Spam Call Detection An AI-powered system to automatically detect spam calls based on conversation transcripts. This project compares Machine Learning and Deep Learning approaches to determine the most stable and efficient model for spam detection. 

## 🚀 Project Overview Spam calls are disruptive and potentially harmful to users. This project aims to build an intelligent classification system that can: 
- Detect whether a call is **Spam** or **Legitimate Call** 
- Provide **real-time prediction via API** 
- Store prediction history in a database 

## 🧠 Models Implemented 
1️⃣ TF-IDF + XGBoost 
2️⃣ GRU (Gated Recurrent Unit) 

## 📊 Model Evaluation Evaluation metrics: 
- Accuracy 
- Precision 
- Recall 
- F1-Score 
- ROC-AUC 

### 🔎 Key Findings 
- **XGBoost demonstrated the most stable performance**, especially on imbalanced datasets. 
- **GRU showed signs of overfitting** due to limited dataset size. 

## 🛠️ Tech Stack 
- Python 
- FastAPI 
- Streamlit (UI Demo) 
- XGBoost 
- TensorFlow / Keras (GRU) 
- Scikit-learn 
- SQLite 
- Uvicorn 

## ⚙️ Installation 
### 1️⃣ Clone Repository
```bash
git clone https://github.com/phoeb-exe/ai-spam-call-detection.git
cd ai-spam-call-detection
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### ▶️ Run the API
```bash
uvicorn app.main:app --reload
```