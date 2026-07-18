"""
Mini Project 1: Titanic Survival Prediction - Data Cleaning Project
Week 1 - ML Fundamentals + Data Preprocessing
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# ---------- STEP 1: Load & Explore ----------
df = pd.read_csv("titanic.csv")

print("Shape:", df.shape)
print("\nInfo:")
df.info()
print("\nDescribe:\n", df.describe())
print("\nMissing values:\n", df.isnull().sum())

# ---------- STEP 2: Handle Missing Data ----------
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.drop(columns=["Cabin"])
df = df.drop(columns=["PassengerId", "Name", "Ticket"])

print("\nMissing values after cleaning:\n", df.isnull().sum())

# ---------- STEP 3: Encode Categorical Variables ----------
le = LabelEncoder()
df["Sex"] = le.fit_transform(df["Sex"])
df = pd.get_dummies(df, columns=["Embarked"], prefix="Embarked", drop_first=True)

print("\nCleaned & encoded data preview:\n", df.head())

# ---------- STEP 4: Visualize Age Distribution ----------
plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=30, kde=True, color="steelblue")
plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("age_distribution.png")
print("\nSaved chart: age_distribution.png")

# ---------- STEP 5: Save Cleaned Dataset ----------
df.to_csv("titanic_cleaned.csv", index=False)
print("Saved cleaned dataset: titanic_cleaned.csv")
