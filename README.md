# IHG Nudge Calendar Tools

This project contains tools to create and export a 365-day training nudge calendar as an `.ics` file for Google Calendar, Outlook, or Apple Calendar. It is designed to support hotel leaders with prewritten, daily training reminders.

---

## 📁 Project Files

- `extract_nudges.py` — converts raw `.txt` documents into structured Excel files with Nudge IDs and Text
- `generate_schedule.py` — builds a 365-day schedule starting May 1 with categories/subcategories
- `generate_ics.py` — converts the final Excel calendar into a downloadable `.ics` calendar file
- `IHG_Calendar.xlsx` — output of schedule file with mapped nudges (final calendar input)
- `DTC_Nudges.xlsx`, `L_Nudges.xlsx`, etc. — extracted nudge text files
- `IHG_Nudge_Calendar.ics` — final output calendar
- `project_landing_page.html` — standalone interface and download portal (optional)
- `requirements.txt` — dependency list

---

## 🔧 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Extract Nudge Text

```bash
python extract_nudges.py
```

This will read all the raw `.txt` files in the same folder and output one spreadsheet per category:
- `L_Nudges.xlsx` for Loyalty
- `WOC_Nudges.xlsx` for Way of Clean
- `PH_Nudges.xlsx` for Problem Handling
- `DTC_Nudges.xlsx` for Dare to Connect

---

### 2. Generate the Schedule

```bash
python generate_schedule.py
```

Optional:
```bash
--start-date YYYY-MM-DD   # Defaults to 2025-05-01
--output IHG_Calendar.xlsx
```

This creates a calendar structure assigning categories to each day, including rotating Dare to Connect subcategories. You can manually or programmatically assign nudge IDs and texts based on the extracted spreadsheets.

---

### 3. Generate the iCalendar File

```bash
python generate_ics.py
```

Optional:
```bash
--input IHG_Calendar.xlsx
--output IHG_Nudge_Calendar.ics
```

This script reads the final Excel file and converts each row into an `.ics` calendar event scheduled for 9:00 AM local time.

---

## 🧼 Excel Column Requirements

The final spreadsheet must include:

- `Date` (datetime)
- `Day` (weekday, optional)
- `Category` (e.g. Way of Clean, Loyalty)
- `Subcategory` (only used for Dare to Connect)
- `Nudge ID` (e.g. DTC-045, L-006)
- `Text` (actual nudge content)

---

Created by Danielle Bronson.
