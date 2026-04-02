import pandas as pd

def load_logs():
    """
    Reads raw log data from CSV file.
    """
    try:
        df = pd.read_csv("data/logs.csv")
        print("Logs loaded successfully.")
        return df
    except Exception as e:
        print("Error loading logs:", e)
        return None