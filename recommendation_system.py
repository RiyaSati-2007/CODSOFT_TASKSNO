# Recommendation System - CODSOFT Task 4

recommendations = {
    "action": [
        "John Wick",
        "The Dark Knight",
        "Mad Max: Fury Road",
        "Extraction",
        "Mission Impossible"
    ],
    "comedy": [
        "3 Idiots",
        "Hera Pheri",
        "Bhool Bhulaiyaa",
        "The Hangover",
        "Golmaal"
    ],
    "horror": [
        "The Conjuring",
        "Annabelle",
        "It",
        "The Nun",
        "Insidious"
    ],
    "romance": [
        "Titanic",
        "The Notebook",
        "La La Land",
        "Aashiqui 2",
        "Veer-Zaara"
    ],
    "sci-fi": [
        "Interstellar",
        "Inception",
        "The Matrix",
        "Avatar",
        "Gravity"
    ]
}

print("=== Movie Recommendation System ===")
print("Available Genres: Action, Comedy, Horror, Romance, Sci-Fi")

genre = input("\nEnter your favorite genre: ").lower()

if genre in recommendations:
    print("\nRecommended Movies:")
    for movie in recommendations[genre]:
        print("-", movie)
else:
    print("\nSorry! Genre not found.")
    