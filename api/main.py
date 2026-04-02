from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/logs")
def get_logs(level: str = None):
    df = pd.read_csv("data/processed_logs.csv")

    if level:
        df = df[df["level"] == level.upper()]

    return df.to_dict(orient="records")