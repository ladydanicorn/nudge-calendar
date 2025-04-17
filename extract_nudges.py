import pandas as pd
import re
import os

def extract_nudges(file_path: str, prefix: str, category: str) -> pd.DataFrame:
    with open(file_path, "r", encoding="windows-1252") as file:
        lines = file.readlines()

    nudges = []
    current_nudge = []
    nudge_number = 1

    for line in lines:
        stripped = line.strip()
        if re.match(rf"^{nudge_number}\\.", stripped):
            if current_nudge:
                nudges.append({
                    "Nudge ID": f"{prefix}-{str(len(nudges) + 1):03d}",
                    "Category": category,
                    "Text": "\n".join(current_nudge).strip()
                })
            current_nudge = [stripped]
            nudge_number += 1
        else:
            if current_nudge:
                current_nudge.append(stripped)

    if current_nudge:
        nudges.append({
            "Nudge ID": f"{prefix}-{str(len(nudges) + 1):03d}",
            "Category": category,
            "Text": "\n".join(current_nudge).strip()
        })

    return pd.DataFrame(nudges)

def save_nudges(df: pd.DataFrame, output_path: str):
    df.to_excel(output_path, index=False)

def run_batch():
    inputs = [
        ("Crowne Plaza_Loyalty Nudges_Global_ENG.txt", "L", "Loyalty"),
        ("Crowne Plaza_WOC Nudges_Global_ENG.txt", "WOC", "Way of Clean"),
        ("Crowne Plaza_Problem Handling Nudges_Global_ENG.txt", "PH", "Problem Handling"),
        ("DTC-Edit-for-text.txt", "DTC", "Dare to Connect")
    ]

    for path, prefix, category in inputs:
        if not os.path.exists(path):
            print(f"Missing file: {path}")
            continue
        df = extract_nudges(path, prefix, category)
        save_nudges(df, f"{prefix}_Nudges.xlsx")
        print(f"Extracted {len(df)} {category} nudges to {prefix}_Nudges.xlsx")

if __name__ == "__main__":
    run_batch()
