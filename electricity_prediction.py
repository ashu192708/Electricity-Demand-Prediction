import json
import os
import random
from datetime import datetime


FILE_NAME = "electricity_data.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_data(data):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError:
        return False


def calculate_demand(temperature, humidity, hour, previous_demand):
    demand = previous_demand

    # Temperature effect
    if temperature >= 35:
        demand += 1000
    elif temperature >= 30:
        demand += 600
    elif temperature >= 25:
        demand += 300
    elif temperature < 15:
        demand += 400

    # Humidity effect
    if humidity >= 80:
        demand += 250
    elif humidity >= 60:
        demand += 100

    # Time effect
    if 6 <= hour <= 9:
        demand += 500
    elif 18 <= hour <= 22:
        demand += 900
    elif 0 <= hour <= 5:
        demand -= 500

    # Small random variation
    demand += random.randint(-100, 100)

    if demand < 1000:
        demand = 1000

    return round(demand, 2)


def demand_level(demand):
    if demand >= 7500:
        return "CRITICAL"
    elif demand >= 6500:
        return "HIGH"
    elif demand >= 4500:
        return "NORMAL"
    else:
        return "LOW"


def add_prediction(data):
    print("\n========== ADD ELECTRICITY PREDICTION ==========")

    date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    try:
        temperature = float(input("Enter temperature (°C): "))
        humidity = float(input("Enter humidity (%): "))
        hour = int(input("Enter hour (0-23): "))
        previous_demand = float(
            input("Enter previous demand (MW): ")
        )
    except ValueError:
        print("Please enter valid numbers.")
        return

    if not 0 <= humidity <= 100:
        print("Humidity must be between 0 and 100.")
        return

    if not 0 <= hour <= 23:
        print("Hour must be between 0 and 23.")
        return

    predicted_demand = calculate_demand(
        temperature,
        humidity,
        hour,
        previous_demand
    )

    level = demand_level(predicted_demand)

    record = {
        "date": date,
        "temperature": temperature,
        "humidity": humidity,
        "hour": hour,
        "previous_demand": previous_demand,
        "predicted_demand": predicted_demand,
        "demand_level": level
    }

    data.append(record)

    if save_data(data):
        print("\nPrediction generated successfully!")
        print("--------------------------------")
        print("Predicted Demand :", predicted_demand, "MW")
        print("Demand Level     :", level)
        print("--------------------------------")
    else:
        print("Error while saving data.")


def view_predictions(data):
    print("\n========== ELECTRICITY PREDICTIONS ==========")

    if not data:
        print("No prediction records found.")
        return

    for record in data:
        print("\n--------------------------------")
        print("Date              :", record["date"])
        print("Temperature       :", record["temperature"], "°C")
        print("Humidity          :", record["humidity"], "%")
        print("Hour              :", record["hour"])
        print("Previous Demand   :", record["previous_demand"], "MW")
        print("Predicted Demand  :", record["predicted_demand"], "MW")
        print("Demand Level      :", record["demand_level"])
        print("--------------------------------")


def search_prediction(data):
    print("\n========== SEARCH PREDICTION ==========")

    date = input("Enter date (YYYY-MM-DD): ").strip()

    found = False

    for record in data:
        if record["date"] == date:
            print("\nPrediction Found!")
            print("--------------------------------")
            print("Date             :", record["date"])
            print("Temperature      :", record["temperature"], "°C")
            print("Humidity         :", record["humidity"], "%")
            print("Hour             :", record["hour"])
            print("Previous Demand  :", record["previous_demand"], "MW")
            print("Predicted Demand :", record["predicted_demand"], "MW")
            print("Demand Level     :", record["demand_level"])
            print("--------------------------------")

            found = True

    if not found:
        print("No prediction found for this date.")


def generate_sample_data(data):
    print("\n========== GENERATING SAMPLE DATA ==========")

    previous_demand = 4500

    for day in range(1, 11):
        temperature = random.randint(20, 40)
        humidity = random.randint(40, 90)
        hour = random.randint(0, 23)

        predicted_demand = calculate_demand(
            temperature,
            humidity,
            hour,
            previous_demand
        )

        level = demand_level(predicted_demand)

        record = {
            "date": f"2026-09-{day:02d}",
            "temperature": temperature,
            "humidity": humidity,
            "hour": hour,
            "previous_demand": previous_demand,
            "predicted_demand": predicted_demand,
            "demand_level": level
        }

        data.append(record)

        previous_demand = predicted_demand

    if save_data(data):
        print("Sample electricity data generated successfully.")
    else:
        print("Error while saving sample data.")


def show_summary(data):
    print("\n========== DEMAND SUMMARY ==========")

    if not data:
        print("No data available.")
        return

    total = 0
    highest = data[0]["predicted_demand"]
    lowest = data[0]["predicted_demand"]

    for record in data:
        demand = record["predicted_demand"]

        total += demand

        if demand > highest:
            highest = demand

        if demand < lowest:
            lowest = demand

    average = total / len(data)

    print("Total Records    :", len(data))
    print("Average Demand   :", round(average, 2), "MW")
    print("Highest Demand   :", highest, "MW")
    print("Lowest Demand    :", lowest, "MW")

    print("\nGrid Capacity Check:")

    if highest >= 7500:
        print("WARNING: Demand reached critical level!")
    elif highest >= 6500:
        print("WARNING: High electricity demand detected.")
    else:
        print("Demand is within normal range.")


def main():
    data = load_data()

    while True:
        print("\n")
        print("=" * 50)
        print(" ELECTRICITY DEMAND PREDICTION SYSTEM")
        print("=" * 50)

        print("1. Add New Prediction")
        print("2. View All Predictions")
        print("3. Search Prediction")
        print("4. Generate Sample Data")
        print("5. Show Demand Summary")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_prediction(data)

        elif choice == "2":
            view_predictions(data)

        elif choice == "3":
            search_prediction(data)

        elif choice == "4":
            generate_sample_data(data)

        elif choice == "5":
            show_summary(data)

        elif choice == "6":
            print("\nThank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()