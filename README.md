# Electricity Demand Prediction System

A simple **Electricity Demand Prediction System** built using Python. This project allows users to predict electricity demand based on temperature, humidity, hour of the day, and previous electricity demand through a command-line interface (CLI).

## Features

* Add a new electricity demand prediction
* View all prediction records
* Search predictions using a date
* Generate sample electricity data
* Display electricity demand summary
* Classify demand into LOW, NORMAL, HIGH, and CRITICAL levels
* Save prediction records using JSON
* Simple menu-driven interface
* No external Python libraries required

## Requirements

Before running the project, make sure Python is installed on your computer.

Check the Python version:

 ⁠bash
python --version

On macOS / Linux, you can also use:

python3 --version

The project works with Python 3.x.

Project Structure
Electricity-Demand-Prediction/
│
├── electricity_prediction.py
└── README.md

When the program saves prediction records, it automatically creates:

electricity_data.json
Installation
1.⁠ ⁠Clone or download the project

If you have downloaded the project, open the project folder in your terminal.

If using Git:

git clone <repository-url>

Then enter the project directory:

cd Electricity-Demand-Prediction
2.⁠ ⁠No additional packages required

This project uses only Python's built-in features, so you do not need to run pip install.

How to Run
Windows

Open Command Prompt or PowerShell and navigate to the project folder:

cd Desktop\Electricity-Demand-Prediction

Run the program:

python electricity_prediction.py

If python doesn't work, try:

py electricity_prediction.py
macOS / Linux

Open Terminal and navigate to the project folder:

cd ~/Desktop/Electricity-Demand-Prediction

Run:
python3 electricity_prediction.py

Main Menu

When the program starts, you will see:

==================================================
 ELECTRICITY DEMAND PREDICTION SYSTEM
==================================================
1.⁠ ⁠Add New Prediction
2.⁠ ⁠View All Predictions
3.⁠ ⁠Search Prediction
4.⁠ ⁠Generate Sample Data
5.⁠ ⁠Show Demand Summary
6.⁠ ⁠Exit

Enter the number corresponding to the operation you want to perform.

Usage
1.⁠ ⁠Add New Prediction

Select:
1
Then enter the required information:

Enter date (YYYY-MM-DD): 2026-09-21
Enter temperature (°C): 35
Enter humidity (%): 80
Enter hour (0-23): 19
Enter previous demand (MW): 5000

The system will calculate the predicted electricity demand and display its demand level.

Example:

Prediction generated successfully!
--------------------------------
Predicted Demand : 6150 MW
Demand Level     : NORMAL
--------------------------------
2.⁠ ⁠View All Predictions

Select:
2

The program displays all saved electricity prediction records, including:

Date
Temperature
Humidity
Hour
Previous demand
Predicted demand
Demand level
3.⁠ ⁠Search Prediction

Select:
3
Enter date (YYYY-MM-DD): 2026-09-21

The program displays the prediction records available for that date.

4.⁠ ⁠Generate Sample Data

Select:
4
The program automatically generates sample electricity prediction records.

This feature can be used for testing the system without entering every record manually.

5.⁠ ⁠Show Demand Summary

Select:
5
The program displays:

Total number of records
Average electricity demand
Highest electricity demand
Lowest electricity demand
Grid capacity warning

Example:
========== DEMAND SUMMARY ==========

Total Records    : 10
Average Demand   : 5235.4 MW
Highest Demand   : 6810 MW
Lowest Demand    : 3920 MW

Grid Capacity Check:
WARNING: High electricity demand detected.

========== DEMAND SUMMARY ==========

Total Records    : 10
Average Demand   : 5235.4 MW
Highest Demand   : 6810 MW
Lowest Demand    : 3920 MW

Grid Capacity Check:
WARNING: High electricity demand detected.

6.⁠ ⁠Exit

Select:
6

The program will close.

Demand Levels

The system classifies predicted electricity demand into four levels:

Below 4500 MW       → LOW
4500 - 6499 MW     → NORMAL
6500 - 7499 MW     → HIGH
7500 MW or above   → CRITICAL

How Prediction Works

The system calculates electricity demand using:

Temperature
Humidity
Hour of the day
Previous electricity demand

Temperature and humidity can increase the estimated demand.

Morning and evening hours also increase demand, while late-night and early-morning hours can reduce demand.

A small random variation is added to the calculated demand.

The final predicted demand is then classified into a demand level.

Example
==================================================
 ELECTRICITY DEMAND PREDICTION SYSTEM
==================================================
1.⁠ ⁠Add New Prediction
2.⁠ ⁠View All Predictions
3.⁠ ⁠Search Prediction
4.⁠ ⁠Generate Sample Data
5.⁠ ⁠Show Demand Summary
6.⁠ ⁠Exit

Enter your choice: 1
Enter date (YYYY-MM-DD): 2026-09-21
Enter temperature (°C): 35
Enter humidity (%): 80
Enter hour (0-23): 19
Enter previous demand (MW): 5000

Prediction generated successfully!

--------------------------------
Predicted Demand : 6150 MW
Demand Level     : NORMAL
--------------------------------

Data Storage

Prediction records are stored automatically in:

electricity_data.json

The program uses Python's built-in JSON and file handling features to save and load prediction records.

The JSON file is created automatically when prediction data is saved.

Future Improvements

The project can be extended with:

Real electricity consumption datasets
Machine learning-based prediction
Graphical data visualization
Weather data integration
More electricity demand factors
Graphical User Interface (GUI)
Web-based interface
Improved prediction accuracy


Technologies Used
Python 3
JSON
Python Lists
Python Dictionaries
Functions
File Handling
Conditional Statements
Loops
Exception Handling
Command Line Interface (CLI)

Author

ASHU

Integrated M.Tech (AI)
VIT Bhopal University

License

This project is intended for educational and learning purposes.
