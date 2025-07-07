# 📰 Fake News Detector

A machine learning-powered web application built with **Django** that classifies news articles as **Fake** or **Real** based on their textual content. This project helps identify misinformation using natural language processing techniques and a trained model.

---

## 🚀 Features

- ✅ Classifies news articles as Fake or Real
- ✅ Simple web interface to input news content
- ✅ Uses a pre-trained machine learning model
- ✅ Django-based backend for easy integration and extensibility

---

## 🛠️ Installation & Setup

Follow the steps below to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/HarshilKhandelwall/Fake-News-Detector.git
cd Fake-News-Detector
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv env
# On Windows:
env\Scripts\activate
# On Mac/Linux:
source env/bin/activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

### 6. Use the App
Open your browser and go to `http://127.0.0.1:8000/analyze/` to use the fake news detection form.

---

## 📁 Project Structure

```
Fake-News-Detector/
├── myproject/             # Django project settings
│   ├── settings.py
│   ├── urls.py
├── playground/            # Main app
│   ├── views.py
│   ├── templates/
│   │   ├── input.html
│   │   └── output.html
│   ├── static/
│   ├── model/             # Serialized ML model and preprocessing files
├── requirements.txt
├── manage.py
└── db.sqlite3
```

---

## 🧠 Model Overview

- **Input**: Raw news article text
- **Process**: Text vectorization using TF-IDF and prediction via a trained ML classifier
- **Output**: Label - *Fake* or *Real*, along with confidence score

> Note: The model files (like `vectorizer.pkl` and `model.pkl`) must be placed in the correct directory (`playground/model/`) for successful predictions.

---

## 📦 Dependencies

- Python 3.x  
- Django  
- scikit-learn  
- pandas  
- numpy  

To install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Feel free to fork the project and submit pull requests to improve functionality, UI, or model performance.

---

## 📄 License


This project is open-source and available under the [MIT License](LICENSE).
=======
This project is open-source and available under the [MIT License](LICENSE)
