def save_logs(df):
    """
    Saves processed data to a new CSV file.
    """
    if df is None:
        print("No data to save.")
        return

    df.to_csv("data/processed_logs.csv", index=False)
    print("Processed logs saved.")