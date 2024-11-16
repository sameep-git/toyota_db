import pandas as pd
import numpy as np

# xl2021 = pd.read_excel("2021.xlsx", "21", index_col = False)
# xl2022 = pd.read_excel("2022.xlsx", "22", index_col = False)
# xl2023 = pd.read_excel("2023.xlsx", "23MY", index_col = False)
# xl2024 = pd.read_excel("2024.xlsx", "24", index_col = False)
# xl2025 = pd.read_excel("2025.xlsx", "FEguide", index_col = False)

# xl2021.to_csv("data2021.csv", encoding='utf-8', index=False)
# xl2022.to_csv("data2022.csv", encoding='utf-8', index=False)
# xl2023.to_csv("data2023.csv", encoding='utf-8', index=False)
# xl2024.to_csv("data2024.csv", encoding='utf-8', index=False)
# xl2025.to_csv("data2025.csv", encoding='utf-8', index=False)

csvFiles = ['data2021.csv', 'data2022.csv', 'data2023.csv', 'data2024.csv', 'data2025.csv']

df = pd.concat(map(pd.read_csv, csvFiles), ignore_index=True)
df = df[['Model Year', 'Mfr Name', 'Division', 'Carline', 
         'City FE (Guide) - Conventional Fuel', 'City2 FE (Guide) - Alternative Fuel', 'Hwy FE (Guide) - Conventional Fuel',
         'Hwy2 Fuel FE (Guide) - Alternative Fuel', 'Comb FE (Guide) - Conventional Fuel', 'Comb2 Fuel FE (Guide) - Alternative Fuel',
         'Annual Fuel1 Cost - Conventional Fuel', 'Fuel2 EPA Calculated Annual Fuel Cost - Alternative Fuel', 'FE Rating (1-10 rating on Label)',
         'GHG Rating (1-10 rating on Label)', '$ You Save over 5 years (amount saved in fuel costs over 5 years - on label) ',
         '$ You Spend over 5 years (increased amount spent in fuel costs over 5 years - on label) ',
         'City FE (Guide) - Conventional Fuel', 'Hwy FE (Guide) - Conventional Fuel', 'Comb FE (Guide) - Conventional Fuel']]

print(df)