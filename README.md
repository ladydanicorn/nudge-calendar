# IHG Nudge Calendar Tools

This project contains tools to create and export a 365-day training nudge calendar as an `.ics` file for Google Calendar, Outlook, or Apple Calendar. 

---

## 📁 Project Files

- `generate_schedule.py` — builds a 365-day schedule and exports it to Excel
- `generate_ics.py` — converts the schedule into a downloadable `.ics` calendar file
- `calendar_schedule.xlsx` — input/output file for nudges
- `IHG_Nudge_Calendar.ics` — final output for calendar distribution
- `README.md` — this documentation

---

## 🔧 Requirements

Install Python packages:

```bash
pip install pandas ics openpyxl
```

---

## ▶️ Usage

### 1. Generate the Schedule

```bash
python generate_schedule.py --output calendar_schedule.xlsx
```

Optional:
```bash
--start-date YYYY-MM-DD   # Defaults to 2025-05-01
```

This will create a file with:
- Date
- Day of week
- Category
- Subcategory (rotated Dare to Connect themes)
- Empty columns for Nudge ID and Text (to be filled in later)

---

### 2. Generate the iCalendar File

```bash
python generate_ics.py --input calendar_schedule.xlsx --output IHG_Nudge_Calendar.ics
```

Optional:
```bash
--start-date YYYY-MM-DD
```

This script reads from the Excel sheet and converts each row into an `.ics` event scheduled at 9:00 AM (floating local time).

---

## 🧼 Spreadsheet Column Requirements

Make sure the Excel file includes:

- `Date` (datetime)
- `Day` (weekday name, optional)
- `Category` (e.g. Way of Clean, Dare to Connect)
- `Subcategory` (only needed for Dare to Connect)
- `Nudge ID` (optional for naming the event)
- `Text` (nudge content)

---

Created by Danielle Bronson.