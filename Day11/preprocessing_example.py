import pandas as pd 
from sklearn.preprocessing import LabelEncoder, StandardScaler

df = pd.read_csv("train.csv")

print("Original Dataset\n")
print(df.head())
print(df.info())
print(df.describe())

numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

print(df['Age'].isnull().sum())


categorical_cols = df.select_dtypes(include=["object"]).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])



encoder = LabelEncoder()
for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])



scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])



print("\nPreprocessed Dataset")
print(df.head())