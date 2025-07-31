import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Loading Titanic dataset...")
df = sns.load_dataset('titanic')

# Basic info
print(f"✅ Dataset loaded: {df.shape[0]} passengers, {df.shape[1]} features")
print(f"✅ Survival rate: {df['survived'].mean():.1%}")
print(f"✅ Average age: {df['age'].mean():.1f} years")
print(f"✅ Missing values: {df.isnull().sum().sum()} total")
