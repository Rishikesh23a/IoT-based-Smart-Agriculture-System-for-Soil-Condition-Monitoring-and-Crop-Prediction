# IoT-based-Smart-Agriculture-System-for-Soil-Condition-Monitoring-and-Crop-Prediction

🌾 IoT-based Smart Agriculture System for Soil Condition Monitoring and Crop Prediction

This project is an IoT-enabled Smart Agriculture System designed to monitor soil and environmental conditions—including temperature, humidity, soil moisture, and pH—using ESP8266 NodeMCU and real-time cloud connectivity through Firebase.

Additionally, it includes a Machine Learning–based Crop Recommendation System, a Power BI Dashboard, and a mobile application built using MIT App Inventor for live monitoring.

This system aims to support farmers with data-driven decision-making and optimized crop cultivation.

⭐ Key Features


🌡 Environmental Monitoring

• Temperature & Humidity using DHT11

• Soil Moisture Detection

• Soil pH Measurement

☁ Cloud Connectivity

• Real-time data updates to Firebase Realtime Database

📱 Mobile App

• Dashboard built using MIT App Inventor

• Displays live field conditions

• User-friendly interface

🤖 Machine Learning Crop Recommendation

• ML model trained on real agricultural datasets

• Suggests suitable crops based on soil/environment conditions

• Includes Streamlit-based deployment screenshots

📊 Analytics Dashboard

• Power BI Report for historical data visualization

💾 Dataset & Model Files

• Training files, pipeline, encoded samples, and ML models included

## 💼 Hardware Components Used

| 🔌 Component                | Purpose                            |
|-----------------------------|-------------------------------------|
| **ESP8266 NodeMCU**         | WiFi-enabled microcontroller        |
| **DHT11**                   | Temperature & humidity sensor       |
| **Soil Moisture Sensor**    | Monitors soil water content         |
| **pH Sensor**               | Measures soil acidity/alkalinity    |
| **Breadboard + Jumper Wires** | Prototyping                       |
| **Firebase**                | Cloud storage for sensor data       |
| **Mobile App (MIT App Inventor)** | Real-time monitoring         |



🔌 Working Architecture

1️⃣ Sensors collect environmental parameters
2️⃣ ESP8266 reads sensor data
3️⃣ Data is uploaded to Firebase Realtime Database
4️⃣ MIT App Inventor app fetches & displays live data
5️⃣ ML model predicts suitable crops
6️⃣ Power BI dashboard provides analytical insights

🛠 Folder Structure (Based on Your GitHub Repo)
IoT-based-Smart-Agriculture-System-for-Soil-Condition-Monitoring-and-Crop-Prediction/
│
├── Code/                            # ESP8266 code + library list
│   ├── esp8266_smart_agri.ino.txt
│   └── libraries-list.txt
│
├── CropRecommendation_ML_Model_Deploy_Using_Streamlit_Screenshots/
│   └── *.png    # All Streamlit deployment screenshots
│
├── CropRecommendation_ML_Model_Files & Data/
│   ├── Dataset.xlsx
│   ├── Model Files (pkl)
│   ├── Pipeline files
│   └── Encoded samples
│
├── Dashboard_Power_Bi/
│   └── Power BI dashboard files & screenshots
│
├── Docs/
│   ├── Firebase Setup
│   ├── Serial monitor logs
│   ├── Circuit diagrams
│   └── Documentation images
│
├── Firebase/
│   └── Firebase DB structure, screenshots, rules
│
├── Mobile_app/
│   └── Screenshots of MIT App Inventor UI
│
├── README.md
└── .gitattributes

🚀 Firebase Setup (Short Guide)

Go to Firebase Console → Create Project

Go to Realtime Database → Create database → Test Mode

Copy DB URL:

https://your-project-id-default-rtdb.firebaseio.com/


Get API Key from:
→ Project Settings → General → Web API Key

Add both values inside your ESP8266 .ino code

Upload code → Open Serial Monitor → Values update in Firebase

📱 Mobile App (MIT App Inventor)

The app includes:

🌡 Temperature display

💧 Humidity display

🌱 Soil moisture level

🧪 Soil pH value

🔄 Auto-refresh using Firebase live values

Screenshots are available inside:

Mobile_app/

🤖 Crop Recommendation ML Model

The project includes:

RandomForest.pkl

Trained ML pipeline

Dataset used for training

Preprocessing files

Deployment screenshots (Streamlit)

The model predicts the best crops based on:

Soil pH

Moisture

Temperature

Humidity

Environmental conditions

📊 Power BI Dashboard

Located inside:

Dashboard_Power_Bi/

Includes:

Trend analysis

Parameter comparison

Soil moisture patterns

Sensor behavior over time

🎓 Learning Outcomes

✔ Built a complete IoT pipeline: Sensors → Microcontroller → Cloud → App
✔ Implemented Machine Learning for crop prediction
✔ Designed a Power BI dashboard for analysis
✔ Learned Firebase integration
✔ Practiced GitHub version control & project organization
✔ Understood full-stack IoT + ML development

🔮 Future Enhancements

Automated irrigation system using relay + water pump

Weather API integration

Fertilizer recommendation model

Crop disease detection

Solar-powered IoT system

👨‍💻 Developer

Rushikesh Sable
MIT AOE College
📧 rushikeshsable9850@gmail.com
