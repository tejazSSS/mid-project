# 🎬 Movie Recommendation System (Content-Based + ML)

A simple yet powerful **movie recommendation system** built using **Python, Pandas, and Scikit-learn**.
This project combines **machine learning** and **similarity-based filtering** to recommend movies based on user preferences.

---

## 🚀 Features

* 📊 Uses **Linear Regression** to predict movie ratings
* 🎯 Uses **Cosine Similarity** to match user preferences
* 🔥 Combines **quality + personalization** for better recommendations
* 🧠 Demonstrates real-world recommender system concepts
* ⚡ Lightweight and beginner-friendly

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* NumPy (implicitly used)

---

## 📂 Project Structure

```
movie-recommendation/
│
├── movie_recommendation.py
├── README.md
```

---

## ⚙️ How It Works

### 1. Dataset Creation

* Uses a mix of:

  * Real movie data
  * Randomly generated movies
* Features include:

  * Genre (Action, Comedy, Drama)
  * Duration
  * Release Year
  * Rating

---

### 2. Machine Learning Model

* A **Linear Regression model** is trained to learn:

  ```
  rating = f(action, comedy, drama, duration, year)
  ```

---

### 3. User Input

User provides:

* Genre preference (1 or 0)
* Preferred duration
* Release year

---

### 4. Similarity Calculation

* Uses **Cosine Similarity** to find movies closest to user preferences

---

### 5. Final Recommendation Score

```
final_score = 0.6 × predicted_rating + 0.4 × similarity
```

* Predicted Rating → movie quality
* Similarity → relevance to user

---

### 6. Output

* Displays **Top 10 recommended movies**

---

## ▶️ How to Run

### Step 1: Install dependencies

```bash
pip install pandas scikit-learn
```

### Step 2: Run the program

```bash
python movie_recommendation.py
```

---

## 💡 Example Input

```
Action (1/0): 1
Comedy (1/0): 0
Drama (1/0): 1
Duration: 150
Year: 2022
```

---

## 📈 Sample Output

```
🎬 Top Recommendations:

Movie_12    8.91
RRR         8.75
KGF 2       8.60
...
```

---

## 🧠 Concepts Covered

* Linear Regression
* Feature Engineering
* Train-Test Split
* Cosine Similarity
* Content-Based Recommendation Systems

---

## ⚠️ Limitations

* No real user history
* Uses synthetic/random data
* Not as advanced as Netflix/YouTube systems

---

## 🔥 Future Improvements

* Add user profiles & history
* Implement collaborative filtering
* Use deep learning models
* Build a GUI (Tkinter / Web App)

---

## 🙌 Contributing

Feel free to fork this repo and improve it!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
