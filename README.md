# 🏠 Real Estate Price Predictor & Recommender System

An **end-to-end Machine Learning + Streamlit project** that predicts property prices and recommends similar listings based on user preferences. It combines real-time prediction with a content-based recommendation engine to enhance user experience for property buyers.

---

## 🚀 Features
Real-time price prediction using a trained ML pipeline  
Content-based property recommender based on user input  
Streamlit web app with a clean and interactive UI  
Location-aware suggestions using cosine similarity  
Modular and reusable code structure  

---

## 🛠️ Tech Stack
- Machine Learning: scikit-learn, pandas, numpy  
- Data Cleaning: pandas, numpy  
- NLP Processing: CountVectorizer, TF-IDF  
- Similarity Matching: Cosine Similarity  
- Web Framework: Streamlit  
- Model Storage: Joblib / Pickle  
- Deployment: GitHub + Streamlit  

---

## 📂 Project Structure
Real-State-price-Predictor-and-recommendation-System/  
├── app.py → Main Streamlit app  
├── predict.py → Price prediction logic  
├── recommend.py → Property recommender logic  
├── preprocess.py → Data cleaning & preprocessing functions  
├── pipeline.pkl → Trained ML pipeline (downloaded externally)  
├── data/  
│   └── cleaned_data.csv → Cleaned property dataset  
├── static/  
│   └── banner.png → App logo or banner image  
├── requirements.txt → Python dependencies  
└── README.md → Project documentation  

---

## How It Works
1️. User selects property details (location, area, BHK, etc.)  
2️. The ML pipeline preprocesses the input and predicts the property price.  
3️. The system finds similar listings using text + location similarity (cosine similarity).  
4️. The app displays the predicted price and top property recommendations.  

---

## 🔧 Setup Instructions
1️. **Clone the Repository**  
git clone https://github.com/Aman-sys-ui/Real-State-price-Predictor-and-recommendation-System.git  
cd Real-State-price-Predictor-and-recommendation-System  

2️. **Install Dependencies**  
pip install -r requirements.txt  

3️. **Download the ML Model (pipeline.pkl)**  
import gdown  
gdown.download("https://drive.google.com/uc?id=YOUR_FILE_ID", "pipeline.pkl", quiet=False)  

4️. **Run the Streamlit App**  
streamlit run app.py  

---

## ✅ Future Enhancements
- Add filters for price range, furnishing, etc.  
- Use geospatial distance for smarter location matching  
- Integrate map visualization using Folium or Leaflet  
- Deploy on Streamlit Cloud or Hugging Face Spaces  

---

## 🤝 Contributing
1️⃣ Fork this repository  
2️⃣ Create a new feature branch  
3️⃣ Commit and push your changes  
4️⃣ Submit a Pull Request  

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 👨‍💻 Author
**Aman**  
GitHub: https://github.com/Aman-sys-ui  

---

⭐ If you like this project, please give it a star!
