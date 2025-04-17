import pandas as pd
from ics import Calendar, Event
from datetime import datetime, timedelta
import argparse

def generate_ics(input_excel, output_ics):
    df = pd.read_excel(input_excel)
    cal = Calendar()

    for _, row in df.iterrows():
        if pd.isna(row['Date']) or pd.isna(row['Text']):
            continue

        event = Event()
        event.name = f"Nudge: {row['Nudge ID']}"
        event.begin = datetime.combine(pd.to_datetime(row['Date']), datetime.min.time()) + timedelta(hours=9)
        event.duration = timedelta(minutes=15)
        event.description = row['Text']
        cal.events.add(event)

    with open(output_ics, "w") as f:
        f.writelines(cal)
    print(f".ics calendar exported to {output_ics}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="IHG_Calendar.xlsx", help="Excel file with calendar entries")
    parser.add_argument("--output", default="IHG_Nudge_Calendar.ics", help="Output .ics file")
    args = parser.parse_args()

    generate_ics(args.input, args.output)
