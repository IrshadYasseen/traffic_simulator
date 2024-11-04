import pandas as pd
from datetime import datetime
import os

def update_sheets(red, green):
    file_path = "signal_time.xlsx"

    if not os.path.exists(file_path):
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            red_df = pd.DataFrame(columns=['date', 'time', 'north', 'east', 'south', 'west'])
            green_df = pd.DataFrame(columns=['date', 'time', 'north', 'east', 'south', 'west'])
            red_df.to_excel(writer, sheet_name='Red_light', index=False)
            green_df.to_excel(writer, sheet_name='Green_light', index=False)

    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        red_df_existing = pd.read_excel(file_path, sheet_name='Red_light', engine='openpyxl')
        green_df_existing = pd.read_excel(file_path, sheet_name='Green_light', engine='openpyxl')
        
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")
        current_time = current_datetime.strftime("%H:%M:%S")
        
        red_df = pd.DataFrame({
            'date': [current_date],
            'time': [current_time],
            'north': [red[0]],
            'east': [red[1]],
            'south': [red[2]],
            'west': [red[3]]
        })

        green_df = pd.DataFrame({
            'date': [current_date],
            'time': [current_time],
            'north': [green[0]],
            'east': [green[1]],
            'south': [green[2]],
            'west': [green[3]]
        })

        red_df_combined = pd.concat([red_df_existing, red_df], ignore_index=True)
        green_df_combined = pd.concat([green_df_existing, green_df], ignore_index=True)

        red_df_combined.to_excel(writer, sheet_name='Red_light', index=False)
        green_df_combined.to_excel(writer, sheet_name='Green_light', index=False)
