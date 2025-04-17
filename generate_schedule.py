import pandas as pd
from datetime import datetime, timedelta
import random
import argparse

DTC_SUBCATEGORIES = [
    "Dare to Make the First Move",
    "Adapt to the Moment",
    "Relate to Guest Needs",
    "Enable Quality Downtime"
]

def generate_schedule(start_date: str, output_path: str):
    date = datetime.strptime(start_date, "%Y-%m-%d")
    data = []

    dtc_rotation = DTC_SUBCATEGORIES.copy()
    random.shuffle(dtc_rotation)
    dtc_index = 0

    category_days = {
        0: "Problem Handling",  # Monday
        3: "Way of Clean",      # Thursday
        5: "Loyalty"            # Saturday
    }

    # Create a schedule for 365 days
    for i in range(365):
        day_of_week = date.weekday()
        category = category_days.get(day_of_week, "Dare to Connect")
        subcategory = ""

        if category == "Dare to Connect":
            subcategory = dtc_rotation[dtc_index % 4]
            dtc_index += 1
            if dtc_index % 4 == 0:
                random.shuffle(dtc_rotation)

        data.append({
            "Date": date.date(),
            "Day": date.strftime("%A"),
            "Category": category,
            "Subcategory": subcategory,
            "Nudge ID": "",
            "Text": ""
        })

        date += timedelta(days=1)

    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)
    print(f"Generated calendar: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", default="2025-05-01", help="Start date for the schedule")
    parser.add_argument("--output", default="IHG_Calendar.xlsx", help="Output Excel file")
    args = parser.parse_args()

    generate_schedule(args.start_date, args.output)
