import pandas as pd
import numpy as np
from sqlalchemy import create_engine

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

engine = create_engine('sqlite://',
                       echo=False)

csvFiles = ['data2021.csv', 'data2022.csv', 'data2023.csv', 'data2024.csv', 'data2025.csv']

df = pd.concat(map(pd.read_csv, csvFiles), ignore_index=True)
df = df[['Model Year', 'Mfr Name', 'Division', 'Carline', 
         'City FE (Guide) - Conventional Fuel', 'City2 FE (Guide) - Alternative Fuel', 'Hwy FE (Guide) - Conventional Fuel',
         'Hwy2 Fuel FE (Guide) - Alternative Fuel', 'Comb FE (Guide) - Conventional Fuel', 'Comb2 Fuel FE (Guide) - Alternative Fuel',
         'EPA Calculated Annual Fuel Cost - Conventional Fuel -----  Annual fuel cost error. Please revise Verify. ', 'Fuel2 EPA Calculated Annual Fuel Cost - Alternative Fuel', 'FE Rating (1-10 rating on Label)',
         'GHG Rating (1-10 rating on Label)', '$ You Save over 5 years (amount saved in fuel costs over 5 years - on label) ',
         '$ You Spend over 5 years (increased amount spent in fuel costs over 5 years - on label) ',
         'City CO2 Rounded Adjusted', 'Hwy CO2 Rounded Adjusted', 'Comb CO2 Rounded Adjusted (as shown on FE Label)']]

df = df.rename(columns={
    "Model Year": "Year",
    "Mfr Name" : "Manufacturer",
    "Division": "Division",
    "Carline": "Car_Model",
    "City FE (Guide) - Conventional Fuel": "City_FE_Conventional",
    "City2 FE (Guide) - Alternative Fuel": "City_FE_Alternative",
    "Hwy FE (Guide) - Conventional Fuel": "Hwy_FE_Conventional",
    "Hwy2 FE (Guide) - Alternative Fuel": "Hwy_FE_Alternative",
    "Comb FE (Guide) - Conventional Fuel": "Comb_FE_Conventional",
    "Comb2 FE (Guide) - Alternative Fuel": "Comb_FE_Alternative",
    "EPA Calculated Annual Fuel Cost - Conventional Fuel -----  Annual fuel cost error. Please revise Verify. ": "Annual_Fuel_Cost_Conventional",
    "Fuel2 EPA Calculated Annual Fuel Cost - Alternative Fuel": "Annual_Fuel_Cost_Alternative",
    "FE Rating (1-10 rating on Label)": "Fuel_Efficiency_Rating",
    "GHG Rating (1-10 rating on Label)": "GHG_Rating",
    "$ You Save over 5 years (amount saved in fuel costs over 5 years - on label) ": "Savings_5Yrs",
    "$ You Spend over 5 years (increased amount spent in fuel costs over 5 years - on label) ": "Spending_5Yrs",
    "City CO2 Rounded Adjusted": "City_CO2",
    "Hwy CO2 Rounded Adjusted": "Hwy_CO2",
    "Comb CO2 Rounded Adjusted (as shown on FE Label)": "Comb_CO2"
})

# Remove any duplicate columns if any
df = df.loc[:,~df.columns.duplicated()].copy()

# Rename some divisions for better clarity
df['Division'].replace('Volvo Cars of North America, LLC', 'Volvo', inplace=True)
df['Division'].replace('Aston Martin Lagonda Ltd', 'Aston Martin', inplace=True)
df['Division'].replace('Ferrari North America, Inc.', 'Ferrari', inplace=True)
df['Division'].replace('Lotus Cars Ltd', 'Lotus', inplace=True)
df['Division'].replace('Roush Industries, Inc.', 'Roush', inplace=True)
df['Division'].replace('HYUNDAI MOTOR COMPANY', 'Hyundai', inplace=True)
df['Division'].replace('Mitsubishi Motors Corporation', 'Mitsubishi', inplace=True)
df['Division'].replace('Rolls-Royce Motor Cars Limited', 'Rolls-Royce', inplace=True)
df['Division'].replace('TOYOTA', 'Toyota', inplace=True)

# Merge some columns for better data processing and database practices
df['City_FE_Alternative'].fillna(df['City_FE_Conventional'], inplace=True)
df['Hwy2 Fuel FE (Guide) - Alternative Fuel'].fillna(df['Hwy_FE_Conventional'], inplace=True)
df['Comb2 Fuel FE (Guide) - Alternative Fuel'].fillna(df['Comb_FE_Conventional'], inplace=True)

# Drop extra columns
df.drop("City_FE_Conventional", axis=1, inplace=True)
df.drop("Hwy_FE_Conventional", axis=1, inplace=True)
df.drop("Comb_FE_Conventional", axis=1, inplace=True)

# Rename merged columns for better insight
df.rename(columns={
"City_FE_Alternative" : "City_FE",
"Hwy2 Fuel FE (Guide) - Alternative Fuel" : "Hwy_FE",
"Comb2 Fuel FE (Guide) - Alternative Fuel" : "Comb_FE"
    }, inplace=True)

df['Savings_5Yrs'] = -df['Savings_5Yrs'].abs()
df['Savings_5Yrs'].fillna(df['Spending_5Yrs'], inplace=True)

df.drop("Spending_5Yrs", axis=1, inplace=True)

df.rename(columns={
    "Savings_5Yrs" : "Money_5Yrs"
}, inplace=True)

# Dropped because it is not a useful indicator
df.drop("Annual_Fuel_Cost_Alternative", axis = 1, inplace = True)
print(df)
df.to_csv("data.csv", index=False)