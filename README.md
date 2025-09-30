Real Estate Price Predictor & Recommender System
🚀 Features
✅ Real-time Price Prediction using trained ML pipeline
✅ Content-Based Property Recommender based on user inputs
✅ Streamlit Web App with clean and interactive UI
✅ Location-aware suggestions using cosine similarity
✅ Modular code structure with reusable components

Tech Stack

Machine Learning: Scikit-learn, Pandas, NumPy

Data Cleaning: Pandas, NumPy

NLP Processing: CountVectorizer, TF-IDF

Similarity Matching: Cosine Similarity

Web Framework: Streamlit

Model Storage: Joblib/Pickle

Deployment-Ready: GitHub + Streamlit 
📂 Project Structure

Real-State-price-Predictor-and-recommendation-System/
├── app.py                   # Main Streamlit app

├── predict.py               # Price prediction logic

├── recommend.py             # Recommender logic

├── preprocess.py            # Data cleaning / processing

├── pipeline.pkl             # (Stored externally, loaded via gdown)

├── data/

│   └── cleaned_data.csv     # Cleaned property dataset

├── static/

│   └── banner.png           # App image/logo

├── requirements.txt         # Python dependencies

└── README.md                # This file
🧠 How It Works
1. User selects features (location, area, BHK, etc.)
2. ML pipeline preprocesses input and predicts the price.
3. App fetches similar listings using text + location similarity.
4. Outputs predicted price + top recommendations.
🔧 Setup Instructions
⚙️ 1. Clone this repo:
   git clone https://github.com/Aman-sys-ui/Real-State-price-Predictor-and-recommendation-System.git
   cd Real-State-price-Predictor-and-recommendation-System

📦 2. Install dependencies:
   pip install -r requirements.txt

📥 3. Download the ML model (pipeline.pkl):
   import gdown
   gdown.download("https://drive.google.com/uc?id=YOUR_FILE_ID", "pipeline.pkl", quiet=False)

▶️ 4. Run the Streamlit app:
   streamlit run app.py


✅ Future Enhancements
• Add filters for price range, furnishing, etc.
• Use Geospatial Distance for smarter location matching
• Integrate Map View using Folium or Leaflet
• Deploy on Streamlit Cloud or Hugging Face Spaces

🤝 Contributing
1. Fork this repo
2. Create a feature branch
3. Push and submit a PR

📜 License

This project is licensed under the MIT License.
👨‍💻 Author

Aman - GitHub: https://github.com/Aman-sys-ui

⭐

If you like this project, give it a star!
