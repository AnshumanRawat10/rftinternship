# DAY 18 - MOVIE DATASET ANALYSIS

import pandas as pd
import matplotlib.pyplot as plt
# -----------------------------
# DATASET
# -----------------------------
data = {
    "Movie": ["A", "B", "C", "D", "E", "F", "G"],
    "Rating": [8.5, 7.2, 9.0, 6.8, 8.0, 7.5, 9.2],
    "Genre": ["Action", "Comedy", "Action", "Drama", "Comedy", "Drama", "Action"],
    "Revenue": [500, 300, 800, 200, 450, 350, 900]
}

df = pd.DataFrame(data)

print("\nDataset:\n", df)

# -----------------------------
# HIGHEST RATED MOVIES
# -----------------------------
top_rated = df.sort_values(by="Rating", ascending=False)
print("\nTop Rated Movies:\n", top_rated)

# -----------------------------
# MOST PROFITABLE GENRES
# -----------------------------
genre_revenue = df.groupby("Genre")["Revenue"].sum()
print("\nRevenue by Genre:\n", genre_revenue)

# -----------------------------
# VISUALIZATION 1: GENRE vs REVENUE
# -----------------------------
plt.figure()
genre_revenue.plot(kind='bar')
plt.title("Genre vs Revenue")
plt.xlabel("Genre")
plt.ylabel("Total Revenue")
plt.show()

# -----------------------------
# VISUALIZATION 2: RATING DISTRIBUTION
# -----------------------------
plt.figure()
plt.hist(df["Rating"], bins=5)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# -----------------------------
# BONUS: CORRELATION
# -----------------------------
correlation = df["Rating"].corr(df["Revenue"])
print("\nCorrelation between Rating & Revenue:", correlation)

# -----------------------------
# BONUS: TOP 5 MOVIES
# -----------------------------
top5 = df.sort_values(by="Revenue", ascending=False).head(5)
print("\nTop 5 Movies by Revenue:\n", top5)