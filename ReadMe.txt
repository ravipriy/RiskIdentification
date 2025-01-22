# Automated Risk Identification Project

## 🚀 About the Project

The **Automated Risk Identification Project** aims to revolutionize risk management by leveraging **Artificial Intelligence (AI)** to automate risk identification and prioritization. Designed around the **NIST Cybersecurity Framework (CSF)**, this solution categorizes risks into **Information Security (IS)** and **Data Privacy (DP)** risks, providing a standardized and efficient approach to managing risks.

---

## ✨ Key Features

- **Risk Categorization**: Automatically classify risks as **Information Security (IS)** or **Data Privacy (DP)**.  
- **Machine Learning Models**: Advanced models tailored to predict:
  - Likelihood of Attack
  - Names and Categories of Risks
  - Prerequisites and Required Skills
  - Consequences of Risks
  - Possible Mitigations  

---

## 📂 Project Structure

```
RiskIdentification/
├── static/
├── templates/
├── App.py
├── database.py
├── requirements.txt
├── model/
│   └── model.pickle
└── README.md
```

- **`App.py`**: Main application file for running the backend.  
- **`database.py`**: Handles database connections and queries.  
- **`model/model.pickle`**: Pre-trained machine learning model for risk prediction.  
- **`static/` & `templates/`**: Frontend assets and HTML templates for the web interface.  

---

## 🛠️ Setup Instructions

Follow these steps to set up and run the project on your local machine:

### 1️⃣ Prerequisites

- **Python 3.7+**
- **MySQL Database**
- Basic knowledge of Python, MySQL, and machine learning concepts.

### 2️⃣ Installation

1. **Clone the Repository**:  

   ```bash
   git clone https://github.com/ravipriy/RiskIdentification.git
   cd RiskIdentification
   ```

2. **Extract Pre-trained Model**:  
   - Download the `model.rar` file (provided in the repository).  
   - Extract it into the same directory, which creates a folder named `model` containing `model.pickle`.

3. **Install Dependencies**:  

   ```bash
   pip install -r requirements.txt
   ```

### 3️⃣ Database Setup

1. Install and configure MySQL.  

   - Default password is `admin`.  
   - If you change the MySQL password, update it in `database.py`.

2. Create the **users** table in your MySQL database:  

   ```sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       email VARCHAR(255) NOT NULL UNIQUE,
       password VARCHAR(255) NOT NULL
   );
   ```

---

## ▶️ Running the Application

1. **Start the Backend**:  

   ```bash
   python App.py
   ```

2. **Access the Application**:  

   Open your browser and navigate to `http://127.0.0.1:5000` (ensure the port number matches).

---

## 🌟 Features in Action

Once running, the application provides an intuitive interface to:  
- Input risk parameters.  
- Get predictions on likelihood, consequences, and mitigations.  
- Manage users through a secure database.

---

## 🤝 Contributing

Contributions are welcome! If you have ideas or improvements, please:  
1. Fork the repository.  
2. Create a new branch.  
3. Submit a pull request with your changes.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

**Thank you for exploring this project! Feel free to reach out for collaboration or inquiries.** 😊

--- 
