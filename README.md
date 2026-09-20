# Electricity-Demand-Prediction
AI-Based Electricity Demand Prediction System

## Overview

The **AI-Based Electricity Demand Prediction System** is a Python-based academic project that predicts electricity demand using basic environmental and time-related factors.

The system takes inputs such as:

- Temperature
- Humidity
- Hour of the day
- Previous electricity demand

It then calculates the expected electricity demand and classifies it as **LOW, NORMAL, HIGH, or CRITICAL**.

The project is developed as a basic Python implementation of Code

---

## Problem Statement

Electricity demand changes according to factors such as temperature, humidity, time of day, and previous electricity consumption.

The purpose of this project is to provide a simple system that can estimate electricity demand and identify periods of high or critical demand.

---

## Objectives

- Predict electricity demand based on input conditions.
- Consider temperature and humidity effects.
- Consider different electricity-demand patterns during the day.
- Generate high-demand and critical-demand alerts.
- Store prediction records for future reference.
- Provide a simple command-line interface.
- Generate a summary of recorded electricity demand.

---

## Features

### 1. Add New Prediction

The user can enter:

- Date
- Temperature
- Humidity
- Hour
- Previous electricity demand

The system calculates the predicted demand.

### 2. Demand Classification

The predicted demand is classified into:

- LOW
- NORMAL
- HIGH
- CRITICAL

### 3. View All Predictions

Displays all previously generated electricity-demand predictions.

### 4. Search Prediction

Allows the user to search for a prediction using a specific date.

### 5. Generate Sample Data

The system can automatically generate sample electricity-demand records for testing and demonstration.

### 6. Demand Summary

Displays:

- Total number of records
- Average demand
- Highest demand
- Lowest demand
- Grid-capacity warning

### 7. Data Storage

Prediction records are stored in a JSON file so that data remains available after the program is closed.

---

## Technologies Used

- Python 3
- JSON
- File Handling
- Functions
- Lists
- Dictionaries
- Conditional Statements
- Loops
- Exception Handling
- Basic Mathematical Calculations

No external Python libraries are required.

---

## Project Structure

```text
Electricity-Demand-Prediction/
│
├── ashu.py
├── README.md
└── electricity_data.json
