# 🎮 Riot Analytics Elite

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge\&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Riot Games API](https://img.shields.io/badge/Riot_API-EB0029?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge\&logo=git\&logoColor=white)

A full-stack analytics platform built to retrieve, process, and visualize competitive player data from Riot Games services.

The application combines a high-performance REST API with an interactive dashboard, allowing users to quickly access summoner information, ranked statistics, and performance metrics through a simple and intuitive interface.

---

## 🎯 Project Overview

This project was developed to demonstrate modern full-stack development practices using Python, API integrations, asynchronous processing, and interactive data visualization.

The system consumes official Riot Games endpoints, processes player information, and presents the results through a web dashboard designed for fast exploration and analysis.

Key objectives:

* Real-time player data retrieval.
* Secure API integration.
* Interactive data visualization.
* Robust error handling.
* Clean separation between backend and frontend layers.

---

## 🏗️ System Architecture

The application follows a layered architecture that separates data acquisition from presentation.

### Backend (FastAPI)

Responsible for:

* API request handling.
* Communication with Riot Games services.
* Data processing and validation.
* Error handling and response formatting.
* Secure credential management.

### Frontend (Streamlit)

Responsible for:

* User interaction.
* Data visualization.
* Dashboard rendering.
* Real-time requests to the backend.

### External Integration

The system communicates directly with the Riot Games API through REST endpoints, retrieving:

* Summoner information.
* Ranked statistics.
* Competitive performance metrics.

---

## 🚀 Technologies Used

### Backend

* Python 3.10+
* FastAPI
* HTTPX
* Uvicorn

### Frontend

* Streamlit

### Development Tools

* Git
* GitHub
* Virtual Environment (venv)
* Environment Variables (.env)

---

## ✨ Features

### Player Lookup

* Search for Riot Games accounts.
* Retrieve profile information.
* Display competitive statistics.

### Interactive Dashboard

* User-friendly interface.
* Fast data retrieval.
* Real-time visualization.

### Defensive Programming

* Handles invalid requests.
* Manages API failures gracefully.
* Prevents application crashes when player data is unavailable.

### Security

* API keys stored through environment variables.
* Sensitive credentials excluded from version control.
* Git ignore rules configured for development artifacts.

---

## 📦 Installation

### Prerequisites

* Python 3.10+
* Riot Games API Key
* Git

### Clone Repository

```bash
git clone https://github.com/WaynerMoraes12/riot-analytics-elite.git

cd riot-analytics-elite
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
RIOT_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

Open two terminals.

### Terminal 1 — Backend API

```bash
uvicorn main:app --reload
```

API available at:

```text
http://127.0.0.1:8000
```

### Terminal 2 — Streamlit Dashboard

```bash
streamlit run dashboard.py
```

Dashboard available at:

```text
http://localhost:8501
```

---

## 📁 Project Structure

```text
/
├── main.py            # FastAPI application
├── dashboard.py       # Streamlit dashboard
├── .env               # Environment variables (not tracked)
├── .gitignore         # Git exclusion rules
├── requirements.txt   # Project dependencies
└── README.md          # Documentation
```

---

## 🛡️ Best Practices Implemented

* Separation of concerns (Backend / Frontend).
* Environment-based configuration.
* API key protection.
* Defensive programming.
* RESTful architecture.
* Modular project structure.
* Version control with Git.

---

## 📈 Future Improvements

* Match history analytics.
* Win-rate trend visualization.
* Player comparison system.
* Docker containerization.
* Automated testing.
* Deployment to cloud platforms.
* Database integration for historical tracking.

---

## 👨‍💻 Author

**Wayner Pires de Moraes**

QA Engineer | Automation Engineer | Python Developer

GitHub: https://github.com/WaynerMoraes12

---

*Built as a full-stack project focused on API integration, data processing, software architecture, and interactive analytics.*
