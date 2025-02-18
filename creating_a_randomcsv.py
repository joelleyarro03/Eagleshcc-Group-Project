import pandas as pd
import numpy as np
import random

# Number of rows and features
n_rows = 10
n_features = 5

# Generate random data for each feature
emails = [f"student{i}@hccs.edu" for i in range(n_rows)]
names = [f"Student{i}" for i in range(n_rows)]  # Simplified names
ages = np.random.randint(18, 65, size=n_rows) # Ages between 18 and 64
salaries = np.random.randint(30000, 100000, size=n_rows) # Salaries between 30k and 99k
genders = random.choices(["Male", "Female"], k=n_rows)

# Create a Pandas DataFrame
df = pd.DataFrame({
    "email": emails,
    "name": names,
    "age": ages,
    "salary": salaries,
    "gender": genders
})

# Save the DataFrame to a CSV file
df.to_csv("random_data.csv", index=False)  # index=False prevents writing row indices

print("CSV file 'random_data.csv' created successfully.")
#print(df) # Optional: Print the DataFrame to the console
