# 🌊 Development of Smart Water IoT System to Assess and Monitor the Quality of River Water

An end-to-end **IoT-based Smart Water Quality Monitoring System** that combines **embedded systems, cloud computing, machine learning, and web technologies** to continuously monitor river water quality in real time.

This project was developed as my **Undergraduate Final Year Project** and later resulted in a **peer-reviewed journal publication**.

---

## 📄 Publication

**International Journal of Latest Technology in Engineering, Management & Applied Science (IJLTEMAS)**

**Title:** Development of Smart Water IoT System to Assess and Monitor the Quality of River Water

**DOI:** https://doi.org/10.51583/IJLTEMAS.2026.150600128

---

# 📖 Overview

Monitoring river water quality is essential for environmental protection, public health, and sustainable water resource management. Traditional manual sampling methods are often time-consuming and unable to provide continuous monitoring.

This project addresses these challenges by developing an IoT-enabled water quality monitoring system capable of collecting sensor data in real time, transmitting it to the cloud, analyzing water quality using Machine Learning and Water Quality Index (WQI), visualizing results through a web application, and generating automated alerts whenever abnormal conditions are detected.

---

# ✨ Features

- 🌊 Real-time river water quality monitoring
- 📡 Wireless sensor data transmission using ESP8266
- ☁️ Cloud-based data storage and visualization
- 🤖 Machine Learning-based water quality analysis using XGBoost
- 📊 Water Quality Index (WQI) calculation
- 🌐 Web dashboard for monitoring sensor readings
- 📧 Automated alert notifications
- 📈 Historical sensor data visualization
- 🔬 Low-cost and scalable IoT solution

---

# 🏗 System Architecture

<p align="center">
<img src="Images/Picture%202.png" width="700">
</p>

The system continuously collects water quality parameters using multiple sensors connected to an Arduino Uno. Sensor readings are transmitted through an ESP8266 Wi-Fi module to the cloud, where they are stored, processed, analyzed, and visualized via a web application. Machine Learning and Water Quality Index (WQI) calculations provide meaningful insights into overall water quality.

---

# ⚡ Hardware Components

| Component | Purpose |
|-----------|---------|
| Arduino Uno | Main microcontroller |
| ESP8266 | Wi-Fi communication |
| pH Sensor | Measures acidity/basicity |
| Turbidity Sensor | Measures water clarity |
| Temperature Sensor (LM35) | Measures water temperature |
| TDS Sensor | Measures Total Dissolved Solids |
| LCD Display | Local monitoring |

---

# 💻 Software Stack

## Programming Languages

- Python
- C (Arduino)
- PHP
- JavaScript
- HTML
- CSS
- SQL

## Libraries & Tools

- Arduino IDE
- Python Requests
- PySerial
- Jupyter Notebook
- Visual Studio Code

## Cloud Platform

- Adafruit IO

---

# 🤖 Machine Learning

The collected sensor data is processed using **Extreme Gradient Boosting (XGBoost)** to estimate water potability.

### Dataset

| Attribute | Value |
|-----------|------:|
| Features | pH, Temperature, Solids, Turbidity |
| Target | Potability |
| Samples | 3277 |

Dataset:
https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability

---

# 📊 Water Quality Index (WQI)

The system computes the **Water Quality Index (WQI)** based on collected sensor readings to provide an overall assessment of river water quality.

| WQI | Water Quality |
|------|---------------|
| 90–100 | Excellent |
| 70–89 | Good |
| 50–69 | Moderate |
| 25–49 | Bad |
| 0–24 | Very Bad |

This enables users to interpret water quality more intuitively than relying solely on raw sensor measurements.

---

# 🔌 Circuit Diagram

<p align="center">
<img src="Images/Picture%201.png" width="700">
</p>

---

# 📷 Project Screenshots

## Sensor Data

<img src="Images/Picture%208.png">

---

## Cloud Dashboard

<img src="Images/Picture%207.png">

---

## Web Application

<img src="Images/Picture%203.png">

<img src="Images/Picture%204.png">

<img src="Images/Picture%205.png">

<img src="Images/Picture%206.png">

---

# 🚀 Getting Started

## Requirements

### Hardware

- Arduino Uno
- ESP8266
- pH Sensor
- Turbidity Sensor
- LM35 Temperature Sensor
- TDS Sensor
- LCD Display

### Software

- Python 3.6+
- Arduino IDE
- PHP 7+
- SQL Database

Install Python dependencies:

```bash
pip install requests pyserial
```

---

## Configuration

Configure the following before running the project:

### Website

Update

```text
config.php
```

with your database credentials.

### Python

Update

```text
serialread.py
```

- Serial Port
- Website Host Address

---

## Running the Project

1. Upload the Arduino program.
2. Connect the sensors.
3. Configure the PHP server.
4. Start the SQL database.
5. Run

```bash
python serialread.py
```

6. Open the web dashboard.

---

# 🎯 Future Improvements

- Deploy on AWS or Google Cloud Platform
- Mobile application integration
- Additional water quality sensors
- Deep Learning-based prediction models
- AI-powered anomaly detection
- GPS-enabled monitoring stations
- Interactive analytics dashboard

---

# 👨‍💻 Author

**Dinesh Ram S P**

B.E. Electronics and Communication Engineering

M.Tech Artificial Intelligence

---

# ⭐ If you found this project interesting, consider giving it a star!
