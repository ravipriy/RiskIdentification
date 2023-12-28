                                                *********************
                                                    About Project
                                                *********************
Welcome to the Automated Risk Identification Project documentation. This project aims to revolutionize risk management by leveraging artificial intelligence (AI) to automate the process of risk identification and prioritization. With a focus on the NIST Cybersecurity Framework (CSF), this innovative solution categorizes risks into Information Security (IS) and Data Privacy (DP) risks, providing a standardized approach to risk management.

Machine Learning Models
The heart of the project lies in its machine learning models, each tailored to predict specific aspects of risk:

Likelihood of Attack
Name
Prerequisites
Skills Required
Consequences
Mitigations


*************************************************************************

Download this repository extract model.rar in same directory.
it create folder named as "model" it contains "model.pickle"

*************************************************************************
			Setup Backend
download mysql 
default password is admin
if u want to change your mysql password 
make change in database.py

Make sure u already create table of users
use this syntax for create table

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);


*************************************************************************
Download this repository extract model.rar in same directory.
it create folder named as "model" it contains "model.pickle"

Now open terminal in same direcotry 

Step 1:
    First install requirements.txt using command 

    pip install -r requirements.txt

Step 2: 
    Run App.py Using command

    python App.py

Now visit localhost  http://127.0.0.1:5000 (ensure port Number)
*************************************************************************