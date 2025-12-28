import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ba_reviews.csv')


insight = df.groupby("aircraft").agg(
    avg_rating=("rating", "mean"),
    review_count=("rating", "count")
).sort_values("avg_rating", ascending=False)

# seat type vs satisfaction
# seat_insight = df.groupby("seat_type").agg(
#     avg_rating=("rating", "mean"),
#     review_count=("rating", "count")
# ).sort_values("avg_rating", ascending=False)
# print(seat_insight)

# # visualization
# plt.figure(figsize=(10, 6))
# plt.bar(seat_insight.index, seat_insight['avg_rating'], color='skyblue')
# plt.xlabel('Seat Type')
# plt.ylabel('Average Rating')
# plt.title('Average Rating by Seat Type')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
# print(insight)

# SERVICE-WISE BREAKDOWN (Seat, Crew, Food, Entertainment)
breakown = df.groupby("seat_type")[[
    "seat_comfort", "cabin_staff_service",
    "food_beverages", "entertainment"
]].mean()
print(breakown)


print(df.groupby("traveller_type")["rating"].agg(["mean", "count"]))

# visualization
plt.figure(figsize=(10, 6))
plt.bar(insight.index, insight['avg_rating'], color='skyblue')
plt.xlabel('Aircraft')
plt.ylabel('Average Rating')
plt.title('Average Rating by Aircraft')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

