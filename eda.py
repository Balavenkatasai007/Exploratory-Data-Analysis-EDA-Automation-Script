# Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
df = pd.read_csv("C:\\Users\\saivi\\OneDrive\\Desktop\\tem_rel.csv")

# Step 3: Explore the data structure
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset info (columns, data types, missing values):")
print(df.info())

print("\nSummary statistics for numeric columns:")
print(df.describe())

print("\nCheck for missing values:")
print(df.isnull().sum())

# Step 4: Ask questions and explore patterns
# Example 1: Plot numeric columns to see trends
numeric_cols = df.select_dtypes(include=np.number).columns
for col in numeric_cols:
    plt.figure(figsize=(8,4))
    sns.lineplot(data=df, x=df.index, y=col)
    plt.title(f'Trend of {col} over index')
    plt.show()

# Example 2: Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation between numeric variables')
plt.show()

# Example 3: Distribution of numeric columns
for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True, bins=20)
    plt.title(f'Distribution of {col}')
    plt.show()

# Step 5: Detect anomalies or outliers
for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot for {col} to detect outliers')
    plt.show()

# Step 6: Detect duplicates
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# Step 7: Example of testing a hypothesis
# e.g., check if average of a column differs by category
if 'Month' in df.columns and 'Temperature' in df.columns:
    plt.figure(figsize=(10,5))
    sns.barplot(x='Month', y='Temperature', data=df)
    plt.title("Average Temperature per Month")
    plt.show()
