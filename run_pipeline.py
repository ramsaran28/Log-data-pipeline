from pipeline.ingest import load_logs
from pipeline.transform import process_logs
from pipeline.store import save_logs

def run_pipeline():
    print("Starting data pipeline...\n")

    df = load_logs()
    df = process_logs(df)
    save_logs(df)

    print("\nPipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()