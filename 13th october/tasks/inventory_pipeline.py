import pandas as pd
from datetime import datetime

# ----------------------------
# Step 1: Extract
# ----------------------------
def extract_data(file_path):
    """Read inventory CSV file."""
    df = pd.read_csv("inventory.csv")
    print(f" Data extracted from {'inventory.csv'}")
    return df

# ----------------------------
# Step 2: Transform
# ----------------------------
def transform_data(df):
    """Add RestockNeeded and TotalValue columns."""

    # RestockNeeded column
    df['RestockNeeded'] = df.apply(
        lambda row: "Yes" if row['Quantity'] < row['ReorderLevel'] else "No", axis=1
    )

    # TotalValue column
    df['TotalValue'] = df['Quantity'] * df['PricePerUnit']

    print(" Data transformed.")
    return df

# ----------------------------
# Step 3: Load
# ----------------------------
def load_data(df, output_path):
    """Save the final report to a CSV."""
    df.to_csv(output_path, index=False)
    print(f" Report saved to '{output_path}'")

# ----------------------------
# Step 4: Run Pipeline
# ----------------------------
def run_pipeline():
    input_file = "inventory.csv"
    output_file = "restock_report.csv"

    start_time = datetime.now()

    # ETL process
    df = extract_data(input_file)
    df_transformed = transform_data(df)
    load_data(df_transformed, output_file)

    end_time = datetime.now()
    print(f"\n⏱ Inventory pipeline completed at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    run_pipeline()
