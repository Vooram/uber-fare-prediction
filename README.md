Uber Ride Fare Prediction | Streamlit App

This project is a real-time **Uber Fare Prediction Web App** built using **Python**, **Streamlit**, and **machine learning** techniques. Users can input ride details like pickup location, dropoff coordinates, and passenger count to get an instant fare estimate.

Live App**:  https://uber-fare-prediction-mv7gukaabt3sk6az4clw5r.streamlit.app/
Dashboard Extension**: Power BI-style visuals also included!

---

Problem Statement

Ride-hailing users often want a fare estimate before booking. This project uses real-world Uber ride data to:

- Predict fare amounts using ML
- Visualize the pickup trends across NYC
- Analyze fare behavior based on distance and time

---

Features

- 📍 **Distance Calculation** between pickup and dropoff (via Haversine formula)
- 🧠 **Linear Regression Model** for predicting fare
- 🗺️ **Map visualizations** (pickup locations, distances)
- 📈 **Interactive Streamlit UI**
- 📅 **Datetime breakdown** (for future surge analysis)
- ✅ Ready to deploy on **Streamlit Cloud**

---

Technologies Used

| Tool | Purpose |
|------|---------|
| **Python** | Core logic, data processing |
| **Pandas** | DataFrame manipulation |
| **Scikit-learn** | ML model training |
| **Streamlit** | UI and deployment |
| **Matplotlib / Plotly** | Charts and visualization |
| **Geopy / Haversine** | Distance calculations |

---

## 📂 Project Structure

uber-fare-prediction/
├── app.py # Streamlit app
├── model.pkl # Trained regression model
├── data/ # Input data file
├── utils.py # Distance & helper functions
├── requirements.txt # App dependencies
└── README.md # This file

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app.py
Sample Screenshots
Add screenshots here after deployment
Example:


Upcoming Additions
 Surge pricing analysis by hour/day

 Tip amount prediction

 Route optimization

 Export Power BI visuals

📬 Contact
Made by Mithun Kumar Reddy Voora
📧 mithunkumarreddyvoora@gmail.com
