def process_logs(df):
    """
    Cleans and processes log data.
    """
    if df is None:
        return None

    # Standardize log level text
    df["level"] = df["level"].str.upper()

    # Optional: remove duplicates
    df = df.drop_duplicates()

    print("Logs processed successfully.")
    return df