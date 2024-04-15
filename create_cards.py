import tkinter as tk
from tkinter import filedialog
import csv
import json
import os

# Dictionary mapping modifiers to stats
modifier_to_stat = {
    "-4": 3,
    "-3": 4,
    "-2": 6,
    "-1": 8,
    "+0": 10,
    "+1": 12,
    "+2": 14,
    "+3": 16,
    "+4": 18
}

# Function to convert CSV data to JSON format
def csv_to_json(csv_file, json_file):
    json_data = []

    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            monster = {
                "count": 1,
                "color": "black",
                "title": row['Title'],
                "icon": row['Icon'],
                "contents": [
                    f"subtitle | {row['Subtitle']}",
                    "rule",
                    f"property | Armor class | {row['Armor class']}",
                    f"property | Hit points | {row['Hit points']}",
                    f"property | Attack | {row['Attack']}",
                    f"property | Move | {row['Move']}",
                    f"property | Level | {row['Level']}",
                    "rule",
                ],
                "tags": [
                    "creature"
                ]
            }
            
            # Check if Modifiers are provided and add them as dndstats
            if 'Modifiers' in row:
                modifiers = row['Modifiers'].split(', ')
                dnd_stats = []
                for modifier in modifiers:
                    modifier_parts = modifier.split()
                    if len(modifier_parts) == 2:  # Check if the format is correct
                        modifier_value = modifier_parts[1]
                        if modifier_value in modifier_to_stat:  # Check if modifier exists in dictionary
                            stat = modifier_to_stat[modifier_value]
                            dnd_stats.append(f"{stat}")
                if dnd_stats:           
                    monster["contents"].append("dndstats | " + " | ".join(dnd_stats))
                    monster["contents"].append("rule")
            
            # Add talents
            talents = [row['Talent 1'], row['Talent 2'], row['Talent 3']]
            prev_has_fill = False
            for talent in talents:
                if talent.strip():  # Check if talent is not empty
                    talent = talent.replace(":", "|")  # Replace ":" with "|"
                    if not prev_has_fill:
                         monster["contents"].append("fill")                
                    monster["contents"].append(f"property | {talent}")
                    monster["contents"].append("fill")
                    prev_has_fill = True
            
            json_data.append(monster)

    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=2)


# Function to handle button click event
def start_conversion():
    csv_path = csv_entry.get()
    json_path = json_entry.get()
    if not csv_path.endswith('.csv'):
        status_label.config(text="Error: Please select a CSV file.")
        return
    if not json_path.endswith('.json'):
        status_label.config(text="Error: Please select a JSON file.")
        return
    if not os.path.exists(csv_path):
        status_label.config(text="Error: CSV file does not exist.")
        return
    csv_to_json(csv_path, json_path)
    status_label.config(text="Conversion completed successfully!")

# Create the main window
root = tk.Tk()
root.title("Monster Card Generator v0.1.0")

# Create and place widgets
csv_label = tk.Label(root, text="CSV File import:")
csv_label.grid(row=0, column=0)

csv_entry = tk.Entry(root, width=50)
csv_entry.grid(row=0, column=1)

csv_button = tk.Button(root, text="Browse", command=lambda: csv_entry.insert(tk.END, filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])))
csv_button.grid(row=0, column=2)

json_label = tk.Label(root, text="JSON File export:")
json_label.grid(row=1, column=0)

json_entry = tk.Entry(root, width=50)
json_entry.grid(row=1, column=1)

json_button = tk.Button(root, text="Browse", command=lambda: json_entry.insert(tk.END, filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])))
json_button.grid(row=1, column=2)

convert_button = tk.Button(root, text="Convert", command=start_conversion)
convert_button.grid(row=2, column=1)

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
