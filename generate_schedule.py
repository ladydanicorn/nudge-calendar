import argparse
import logging
from datetime import datetime, timedelta
import pandas as pd

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# CLI argument parser
parser = argparse.ArgumentParser(description="Generate a 365-day nudge schedule for iCalendar conversion.")
parser.add_argument('--output', required=True, help='Output Excel file name')
parser.add_argument('--start-date', required=False, default='2025-05-01', help='Start date for the calendar (YYYY-MM-DD)')
args = parser.parse_args()

# Start date and range
start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
dates = [start_date + timedelta(days=i) for i in range(365)]

# Weekday assignments
weekday_to_category = {
    "Monday": "Problem Handling",
    "Thursday": "Way of Clean",
    "Saturday": "Loyalty"
}

# Dare to Connect rotation subcategories
dtc_subcategories = [
    "Dare to Make the First Move",
    "Adapt to the Moment",
    "Relate to Guest Needs",
    "Enable Quality Downtime"
]

# Setup rotation tracker
dtc_index = 0
schedule = []

# Generate daily entries
for date in dates:
    day_name = date.strftime("%A")
    if day_name in weekday_to_category:
        category = weekday_to_category[day_name]
        subcategory = "N/A"
    else:
        category = "Dare to Connect"
        subcategory = dtc_subcategories[dtc_index]
        dtc_index = (dtc_index + 1) % len(dtc_subcategories)

    schedule.append({
        "Date": date.date(),
        "Day": day_name,
        "Category": category,
        "Subcategory": subcategory,
        "Nudge ID": "",
        "Text": ""
    })

# Create DataFrame and export
schedule_df = pd.DataFrame(schedule)
schedule_df.to_excel(args.output, index=False)
logging.info(f"Saved schedule to {args.output}")

