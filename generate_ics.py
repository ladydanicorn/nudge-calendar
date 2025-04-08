from ics import Calendar, Event
from datetime import datetime, timedelta
import pandas as pd

# Load populated nudge spreadsheet (replace with actual path if needed)
df = pd.read_excel("IHG_Calendar.xlsx") # Adjust path as necessary

# Create a new calendar
cal = Calendar()

# Loop through the DataFrame and create events
for _, row in df.iterrows():
    # Skip rows without valid data (just in case)
    if pd.isna(row['Nudge ID']) or pd.isna(row['Date']):
        continue

    # Create a new event
    e = Event()

    # Set a clear event title
    e.name = f"Nudge: {row['Nudge ID']}"

    # Set event start time (9:00 AM local time, no timezone specified)
    event_start = datetime.combine(row['Date'], datetime.min.time()) + timedelta(hours=9)
    e.begin = event_start

    # Set a placeholder duration (can be adjusted)
    e.duration = timedelta(minutes=15)

    # Build the event description
    desc = f"Category: {row['Category']}\n"
    if row['Category'] == "Dare to Connect":
        desc += f"Subcategory: {row['Subcategory']}\n"
    desc += f"\nNudge Content:\n{row['Text']}"
    e.description = desc

    # Add event to calendar
    cal.events.add(e)

# Export the calendar to an .ics file
with open("IHG_Nudge_Calendar.ics", "w") as f:
    f.writelines(cal)