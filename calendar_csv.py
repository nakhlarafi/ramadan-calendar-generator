import pandas as pd

# Creating the structured data as per the required format
data_formatted = {
    "Subject": [],
    "Start Date": [],
    "Start Time": [],
    "End Date": [],
    "End Time": []
}

# Dates range from March 1, 2025, to March 30, 2025
dates = pd.date_range(start="2025-03-01", periods=30, freq='D').strftime('%-m/%-d/%Y')

# Sehri and Iftar times
sehri_times = [
    "05:11 AM", "05:09 AM", "05:08 AM", "05:06 AM", "05:04 AM", "05:02 AM", "05:00 AM", "04:58 AM",
    "05:56 AM", "05:55 AM", "05:53 AM", "05:51 AM", "05:49 AM", "05:47 AM", "05:45 AM", "05:43 AM",
    "05:41 AM", "05:39 AM", "05:37 AM", "05:35 AM", "05:33 AM", "05:31 AM", "05:29 AM", "05:27 AM",
    "05:25 AM", "05:23 AM", "05:20 AM", "05:18 AM", "05:16 AM", "05:14 AM"
]

iftar_times = [
    "05:42 PM", "05:43 PM", "05:44 PM", "05:46 PM", "05:47 PM", "05:49 PM", "05:50 PM", "05:51 PM",
    "06:53 PM", "06:54 PM", "06:55 PM", "06:57 PM", "06:58 PM", "06:59 PM", "07:01 PM", "07:02 PM",
    "07:03 PM", "07:05 PM", "07:06 PM", "07:07 PM", "07:09 PM", "07:10 PM", "07:11 PM", "07:13 PM",
    "07:14 PM", "07:15 PM", "07:16 PM", "07:18 PM", "07:19 PM", "07:20 PM"
]

# Generating Subject names and filling data
for i in range(30):
    data_formatted["Subject"].append(f"Sehri: Day {i+1}")
    data_formatted["Start Date"].append(dates[i])
    data_formatted["Start Time"].append(sehri_times[i])
    data_formatted["End Date"].append(dates[i])
    data_formatted["End Time"].append(sehri_times[i])
    
    data_formatted["Subject"].append(f"Iftaar: Day {i+1}")
    data_formatted["Start Date"].append(dates[i])
    data_formatted["Start Time"].append(iftar_times[i])
    data_formatted["End Date"].append(dates[i])
    data_formatted["End Time"].append(iftar_times[i])

# Create a DataFrame
df_formatted = pd.DataFrame(data_formatted)

# Save as CSV with UTF-8 encoding and proper headers for Google Calendar
file_path_shared = "sehri_iftar_shared.csv"
df_formatted.to_csv(file_path_shared, index=False, encoding='utf-8-sig')

print(f"CSV file saved as {file_path_shared}")