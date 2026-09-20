# Electricity Demand Prediction System

## Overview

The Electricity Demand Prediction System is a basic Python project that predicts electricity demand using simple input-based rules.

The system considers factors such as:

- Temperature
- Humidity
- Hour of the day
- Previous electricity demand

It then calculates the predicted electricity demand and classifies it as LOW, NORMAL, HIGH, or CRITICAL.

This project is implemented using basic Python concepts and does not use machine learning libraries.

---

## Problem Statement

Electricity demand changes according to different conditions such as weather, time of day, and previous demand.

The purpose of this project is to create a simple system that can estimate electricity demand based on these factors.

---

## Objectives

- Predict electricity demand using basic Python logic.
- Use temperature, humidity, time, and previous demand as inputs.
- Classify electricity demand into different levels.
- Store prediction records for future use.
- Search prediction records by date.
- Generate sample electricity data.
- Display a summary of electricity demand.

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

### 2. View All Predictions

Displays all saved electricity prediction records.

### 3. Search Prediction

Allows the user to search for prediction records using a date.

### 4. Generate Sample Data

Automatically generates sample electricity prediction records for testing the system.

### 5. Show Demand Summary

Displays:

- Total number of records
- Average demand
- Highest demand
- Lowest demand
- Grid capacity warning

---

## Demand Levels

The predicted electricity demand is classified into four levels:

| Demand | Level |
|---|---|
| Below 4500 MW | LOW |
| 4500–6499 MW | NORMAL |
| 6500–7499 MW | HIGH |
| 7500 MW or above | CRITICAL |

---

## Technologies Used

- Python 3
- JSON
- File Handling
- Functions
- Conditional Statements
- Loops
- Lists
- Dictionaries
- Exception Handling
- Random Number Generation

No external Python libraries are required.

---

## Project Structure

```text
Electricity-Demand-Prediction/
│
├── electricity_prediction.py
└── README.md
