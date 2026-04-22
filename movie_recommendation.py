import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "movie": [
        "Dangal", "3 Idiots", "Pathaan", "Kabir Singh", "Gully Boy",
        "War", "RRR", "Baahubali", "Drishyam", "PK",
        "Bajrangi Bhaijaan", "KGF", "Jawan", "Animal", "Chennai Express"
    ],
    "genre_action": [0,0,1,0,0,1,1,1,0,0,0,1,1,1,0],
    "genre_comedy": [0,1,0,0,0,0,0,0,0,1,1,0,0,0,1],
    "genre_drama":  [1,1,0,1,1,0,1,1,1,1,1,1,0,1,0],
    "duration": [161,170,146,173,153,156,182,159,163,153,163,156,169,201,141],
    "year": [2016,2009,2023,2019,2019,2019,2022,2015,2015,2014,2015,2018,2023,2023,2013],
    "rating": [8.4,8.4,5.9,7.0,7.9,6.5,7.8,8.0,8.2,8.1,8.0,8.2,7.0,6.8,6.2]
}

df = pd.DataFrame(data)

X = df[["genre_action", "genre_comedy", "genre_drama", "duration", "year"]]
y = df["rating"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

df["predicted_rating"] = model.predict(X)


recommendations = df.sort_values(by="predicted_rating", ascending=False)

print("\n🎬 Recommended Indian Movies:\n")
print(recommendations[["movie", "predicted_rating"]])

print("\n🎯 Try your own preference:")

action = int(input("Action? (1/0): "))
comedy = int(input("Comedy? (1/0): "))
drama = int(input("Drama? (1/0): "))
duration = int(input("Preferred duration (minutes): "))
year = int(input("Release year: "))

user_input = [[action, comedy, drama, duration, year]]

pred = model.predict(user_input)
print(f"\n⭐ Predicted Rating for your preference: {pred[0]:.2f}")