import pandas as pd
from datetime import datetime

# -----------------------------
# Step 1: Extract
# -----------------------------
def extract_data(file_path):
    """Reads customer data from CSV"""
    df = pd.read_csv("customers.csv")
    print(f"✅ Data extracted from {'customers.csv'}")
    return df

# -----------------------------
# Step 2: Transform
# -----------------------------
def transform_data(df):
    """Adds AgeGroup column and filters age >= 20"""

    # Define age group logic
    def assign_age_group(age):
        if age < 30:
            return "Young"
        elif age < 50:
            return "Adult"
        else:
            return "Senior"

    # Filter out customers younger than 20
    df = df[df['Age'] >= 20]

    # Add AgeGroup column
    df['AgeGroup'] = df['Age'].apply(assign_age_group)

    print("🧼 Data transformed.")
    return df

# -----------------------------
# Step 3: Load
# -----------------------------
def load_data(df, output_path):
    """Saves transformed data to a new CSV"""
    df.to_csv(output_path, index=False)
    print(f"📁 Transformed data saved to '{output_path}'")

# -----------------------------
# Step 4: Run Pipeline
# -----------------------------
def run_pipeline():
    input_file = "customers.csv"
    output_file = "filtered_customers.csv"

    # Timestamp
    start_time = datetime.now()

    # Run ETL
    df = extract_data(input_file)
    df_transformed = transform_data(df)
    load_data(df_transformed, output_file)

    end_time = datetime.now()
    print(f"\n⏱️ Pipeline executed at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Run the pipeline
if __name__ == "__main__":
    run_pipeline()
