# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Python**, **Pandas**, and **Scikit-learn**. The project recommends movies similar to a user-selected movie by analyzing metadata such as genres, keywords, cast, director, and overview.

Instead of relying on user ratings or collaborative filtering, this recommender uses **TF-IDF Vectorization** and **Cosine Similarity** to find movies with similar content.

---

## 📖 Overview

This project processes the **TMDB 5000 Movies Dataset** and creates a feature representation ("soup") for every movie by combining multiple metadata fields.

When a user enters a movie title, the program:

1. Finds the selected movie.
2. Compares its feature vector with every other movie.
3. Computes similarity scores using Cosine Similarity.
4. Returns the Top 5 most similar movies.

---

## 🚀 Features

- Merge TMDB Movies and Credits datasets
- Clean nested JSON columns using `ast.literal_eval()`
- Extract
  - Genres
  - Keywords
  - Cast
  - Director
  - Movie Overview
- Build a combined textual representation ("soup")
- Convert text into TF-IDF vectors
- Compute pairwise cosine similarity
- Recommend the Top 5 similar movies

---

## 🛠 Tech Stack

- Python
- Pandas
- Scikit-learn
- AST (Python Standard Library)

---

## 📂 Project Structure

```
Movie-Recommender/
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── main.py
└── README.md
```

---

## ⚙️ How It Works

### 1. Load Dataset

The TMDB Movies and Credits datasets are loaded using Pandas and merged into a single DataFrame.

---

### 2. Data Cleaning

Several columns contain JSON-like strings.

Using

```python
ast.literal_eval()
```

they are converted into Python objects and cleaned.

The following information is extracted:

- Genres
- Keywords
- Cast
- Director

---

### 3. Feature Engineering

Each movie is represented by a **movie soup**, which is a combination of:

- Genres
- Keywords
- Cast
- Director
- Overview

Example:

```
Action Adventure Superhero Batman Christian Bale Christopher Nolan Gotham ...
```

This allows the recommender to compare movies based on their overall content rather than just genre.

---

### 4. TF-IDF Vectorization

The movie soup is converted into numerical vectors using

```python
TfidfVectorizer()
```

TF-IDF assigns higher importance to words that are unique to a movie while reducing the influence of very common words.

---

### 5. Cosine Similarity

Each movie vector is compared against every other movie using

```python
cosine_similarity()
```

The result is a similarity matrix where

```
similarity[i][j]
```

represents how similar movie **i** is to movie **j**.

---

### 6. Recommendation

When a movie title is entered:

- Find its index
- Retrieve its similarity scores
- Sort the scores in descending order
- Exclude the movie itself
- Display the Top 5 recommendations

---

## 📸 Example

### Input

```
Enter a movie name:
The Dark Knight
```

### Output

```
Recommended Movies

The Dark Knight Rises
Batman Returns
Batman Begins
Batman
Batman Forever
```

---

## 🧠 Concepts Used

- Data Cleaning
- Feature Engineering
- Natural Language Processing (Basic)
- Information Retrieval
- TF-IDF
- Vector Space Model
- Cosine Similarity
- Content-Based Recommendation Systems

---

## 📊 Dataset

TMDB 5000 Movie Dataset

Contains:

- Movie Metadata
- Genres
- Cast
- Crew
- Keywords
- Overviews

---

## 🔮 Future Improvements

- Fuzzy search for movie titles
- Movie posters using TMDB API
- Streamlit Web Application
- Hybrid Recommendation System
- Recommendation explanations
- Genre filtering
- Save similarity matrix for faster startup
- Performance optimizations for larger datasets

---

## 📚 What I Learned

While building this project, I learned about:

- Cleaning structured datasets
- Parsing JSON-like strings in Python
- Feature engineering using textual metadata
- TF-IDF Vectorization
- Cosine Similarity
- Building a content-based recommendation pipeline
- Organizing data using Pandas
