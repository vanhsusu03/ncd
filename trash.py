
import pandas as pd
df = pd.read_excel('./data/data_test.xlsx')  # Add sheet name if needed: sheet_name='Sheet1'

# Save it as a CSV file
df.to_csv('./data/data_test.csv', index=False)