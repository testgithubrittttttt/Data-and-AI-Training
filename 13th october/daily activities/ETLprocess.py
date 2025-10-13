# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# ----------------------------
# Step 1: Extract
# ----------------------------

# Load data from CSV into a pandas DataFrame
df = pd.read_csv("students.csv")  # File must be in the same directory

# Show the raw data
print(" Raw Data:")
print(df)

# ----------------------------
# Step 2: Transform
# ----------------------------

# Clean the 'Marks' column:
# Convert to numeric, set invalid values to NaN, then fill NaN with 0
df['Marks'] = pd.to_numeric(df['Marks'], errors='coerce').fillna(0)

# Convert to integer (optional)
df['Marks'] = df['Marks'].astype(int)

# Add a Pass/Fail column based on marks >= 50
df['Result'] = df['Marks'].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Add a Grade column based on range
def assign_grade(marks):
    if marks >= 75:
        return 'A'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C'
    elif marks >= 35:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Marks'].apply(assign_grade)

# Show transformed data
print("\n Transformed Data:")
print(df)

# ----------------------------
# Step 3: Load
# ----------------------------

# Save cleaned data to a new CSV file
output_file = "cleaned_students.csv"
df.to_csv(output_file, index=False)

print(f"\n Cleaned data saved to '{output_file}'")

# ----------------------------
# Step 4: Visualize
# ----------------------------

#  A. Plot Grade Distribution
grade_counts = df['Grade'].value_counts().sort_index()

plt.figure(figsize=(8, 5))
grade_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("🎓 Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

#  B. Plot Pass/Fail Distribution
result_counts = df['Result'].value_counts()

plt.figure(figsize=(6, 4))
result_counts.plot(kind='bar', color=['green', 'red'], edgecolor='black')
plt.title("Pass/Fail Distribution")
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
