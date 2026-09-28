import matplotlib.pyplot as plt

years = [2003, 2010, 2013, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
modularity = [0.0, 0.0, 0.0, 0.0, 0.0, 0.406, 0.612, 0.444, 0.244, 0.5]

plt.plot(years, modularity, marker='o')

plt.title("Community Structure Evolution Over Time")
plt.xlabel("Year")
plt.ylabel("Modularity Score")

plt.grid(True)
plt.show()