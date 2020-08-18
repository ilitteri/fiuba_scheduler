import pandas as pd

csv_file = 'schedule.csv'
df = pd.read_csv(csv_file)


dimensions = df.shape
print(df.info())