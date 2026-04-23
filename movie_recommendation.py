import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics.pairwise import cosine_similarity

movies = [
    ("Dangal", 0, 0, 1, 161, 2016, 8.4),
    ("3 Idiots", 0, 1, 1, 170, 2009, 8.4),
    ("Pathaan", 1, 0, 0, 146, 2023, 5.9),
    ("Jawan", 1, 0, 0, 169, 2023, 7.0),
    ("Animal", 1, 0, 1, 201, 2023, 6.8),
    ("RRR", 1, 0, 1, 182, 2022, 7.8),
    ("KGF 2", 1, 0, 1, 168, 2022, 8.3),
]

for i in range(50):
    movies.append((
        f"Movie_{i}",
        random.randint(0, 1),
        random.randint(0, 1),
        random.randint(0, 1),
        random.randint(90, 180),
        random.randint(2010, 2024),
        round(random.uniform(5, 9), 1)
    ))

df = pd.DataFrame(movies, columns=[
    "movie", "action", "comedy", "drama", "duration", "year", "rating"
])


features = ["action", "comedy", "drama", "duration", "year"]
X = df[features]
y = df["rating"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

df["predicted_rating"] = model.predict(X)

print("\nEnter your preferences:\n")

action = int(input("Action (1/0): "))
comedy = int(input("Comedy (1/0): "))
drama = int(input("Drama (1/0): "))
duration = int(input("Duration: "))
year = int(input("Year: "))

user_vector = [[action, comedy, drama, duration, year]]

similarity_scores = cosine_similarity(user_vector, X)[0]

df["similarity"] = similarity_scores

df["final_score"] = 0.6 * df["predicted_rating"] + 0.4 * df["similarity"] * 10

recommendations = df.sort_values(by="final_score", ascending=False)

print("\n🎬 Top Recommendations:\n")
print(recommendations[["movie", "final_score"]].head(10))