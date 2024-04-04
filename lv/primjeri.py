import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data_C02_emission.csv")
# print(len(data))
# print(data)
# print(data.info())
# print(data.describe())
# print(data.max())
# print(data.min())
# print(data.iloc[2:6, 2:7])
# print(data.iloc[:, 2:5])
# print(data.iloc[:, [0, 4, 7]])
# print(data.Cylinders > 6)
# print(data[data.Cylinders > 6])
# print(data[(data["Cylinders"] == 4) & (data["Engine Size (L)"] > 2.4)].Model)
# new_data = data.groupby('Cylinders')
# print(new_data.count())
# print(new_data.size())
# print(new_data.sum())
# print(new_data.mean())

# print(data.isnull().sum())
# data.dropna(axis=0)

# plt.figure()
# data["Fuel Consumption City (L/100km)"].plot(kind="hist", bins=20)
# plt.figure()
# data["Fuel Consumption City (L/100km)"].plot(kind="box")
# plt.show()

# grouped = data.groupby("Cylinders")
# grouped.boxplot(column=["CO2 Emissions (g/km)"])
# data.boxplot(column=["CO2 Emissions (g/km)"], by="Cylinders")
# plt.show()

# data.plot.scatter(
#     x="Fuel Consumption City (L/100km)",
#     y="Fuel Consumption Hwy (L/100km)",
#     c="Engine Size (L)",
#     cmap="hot",
#     s=50,
# )
# plt.show()

nd = data.sort_values("Fuel Consumption City (L/100km)").head(3)[["Make","Model","Fuel Consumption City (L/100km)"]]
print(nd)