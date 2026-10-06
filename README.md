# 🌱 AI-Powered Smart Agriculture System

An **AI-powered Smart Agriculture System** that uses Machine Learning to assist farmers and agricultural users in making data-driven decisions related to **crop selection, fertilizer recommendation, and crop yield prediction**.

The application is built using **Python, Flask, NumPy, Pandas, and Scikit-learn** and provides a simple web interface where users can enter soil and environmental parameters and receive ML-based predictions.

## 🚀 Features

### 🌾 Crop Recommendation

Recommends a suitable crop based on:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* Soil pH
* Rainfall

### 🧪 Fertilizer Recommendation

Provides a fertilizer recommendation based on soil nutrient values:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)

### 📈 Crop Yield Prediction

Predicts expected crop yield using environmental parameters such as:

* Rainfall
* Temperature
* Humidity

### 🌐 Web Application

The trained ML models are integrated into a **Flask web application**, allowing users to enter agricultural parameters through a browser and receive predictions.

### 🐳 Deployment Support

The project includes:

* `Dockerfile`
* `Gunicorn`
* `requirements.txt`

making the application suitable for deployment on cloud/server environments.

---

## 🏗️ System Architecture

```text
                 ┌───────────────────────┐
                 │       User Input      │
                 │ N, P, K, Temperature  │
                 │ Humidity, pH, Rainfall│
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │    Flask Web App      │
                 │       app.py          │
                 └───────────┬───────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
       ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
       │ Crop Model  │ │ Fertilizer  │ │ Yield Model │
       │             │ │    Model    │ │             │
       └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
              │               │               │
              ▼               ▼               ▼
       Crop Recommendation  Fertilizer     Yield
                            Recommendation Prediction
```

---

## 🧠 Machine Learning Models

The application uses three separate trained Machine Learning models:

| Model                  | Purpose                   | Input                                        |
| ---------------------- | ------------------------- | -------------------------------------------- |
| `crop_model.pkl`       | Crop recommendation       | N, P, K, temperature, humidity, pH, rainfall |
| `fertilizer_model.pkl` | Fertilizer recommendation | N, P, K                                      |
| `yield_model.pkl`      | Yield prediction          | Rainfall, temperature, humidity              |

The trained models are loaded into the Flask application using Python's `pickle` module and used to generate predictions from user-provided inputs.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* NumPy
* Pandas
* Pickle

### Backend

* Flask

### Deployment

* Gunicorn
* Docker

### Frontend

* HTML
* CSS
* Flask/Jinja2 Templates

---

## 📂 Project Structure

```text
AI-powered-smart-agriculture-system/
│
├── data/
│
├── static/
│   └── ...
│
├── templates/
│   └── index.html
│
├── Crop_recommendation.csv
│
├── app.py
│
├── crop_model.py
├── crop_model.pkl
│
├── fertilizer_model.py
├── fertilizer_model.pkl
│
├── yield_model.py
├── yield_model.pkl
│
├── accuracy.txt
├── requirements.txt
├── Dockerfile
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/saurishio/AI-powered-smart-agriculture-system.git
```

Navigate to the project directory:

```bash
cd AI-powered-smart-agriculture-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The project requirements include Flask, NumPy, Pandas, Scikit-learn 1.8.0, and Gunicorn.

---

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

The application runs on:

```text
http://localhost:5000
```

The Flask application is configured to listen on port `5000` and bind to `0.0.0.0`, making it suitable for server deployment.

Open the URL in your browser and enter the required agricultural parameters.

---

## 🧪 Example Input

An example input can contain:

```text
Nitrogen (N):     90
Phosphorus (P):   42
Potassium (K):    43
Temperature:      20.8
Humidity:         82
Soil pH:          6.5
Rainfall:         202
```

The system processes these values through the corresponding trained ML models and returns predictions.

---

## 🔬 Model Workflow

### Crop Recommendation

```text
Soil + Environmental Parameters
              ↓
        Feature Preparation
              ↓
        Trained ML Model
              ↓
       Recommended Crop
```

### Fertilizer Recommendation

```text
N + P + K
   ↓
Feature Preparation
   ↓
Trained ML Model
   ↓
Recommended Fertilizer
```

### Yield Prediction

```text
Rainfall + Temperature + Humidity
              ↓
      Feature Preparation
              ↓
        Trained ML Model
              ↓
        Yield Prediction
```

---

## 🐳 Running with Docker

Build the Docker image:

```bash
docker build -t smart-agriculture .
```

Run the container:

```bash
docker run -p 5000:5000 smart-agriculture
```

Then open:

```text
http://localhost:5000
```

---

## ☁️ Deployment

The application can be deployed to cloud infrastructure or a Linux server using **Gunicorn**.

Example:

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

The repository already includes Gunicorn in its dependency list and contains a Dockerfile for containerized deployment.

---

## 📊 Key Learning Outcomes

This project demonstrates practical experience with:

* Machine Learning model development
* Classification and prediction
* Feature preparation
* Model serialization using Pickle
* Flask-based ML deployment
* Integrating ML models with web applications
* REST-style backend development
* Docker-based application deployment
* Cloud/server deployment concepts

---

## 🔮 Future Improvements

Potential improvements include:

* 🌦️ Integrating real-time weather APIs
* 📍 Location-based crop recommendations
* 🌱 Adding more crop datasets
* 📊 Interactive analytics dashboard
* 📱 Mobile-friendly UI
* 🤖 Comparing multiple ML algorithms
* 📈 Advanced yield forecasting
* ☁️ Cloud-based model serving
* 🔐 User authentication
* 🗄️ Database integration
* 🔄 Automated model retraining
* 📡 IoT sensor integration for real-time soil monitoring

---

## ⚠️ Disclaimer

The predictions generated by this application are **machine-learning-based recommendations** and should not be treated as a substitute for professional agricultural advice.

Actual crop performance and fertilizer requirements can vary depending on soil conditions, geographical location, weather, farming practices, and other environmental factors.

---

## 👨‍💻 Author

**Saurish Chanda**

GitHub: [@saurishio](https://github.com/saurishio)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Repository:**
https://github.com/saurishio/AI-powered-smart-agriculture-system
