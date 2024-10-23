import pandas as pd

# Load the movie dataset
movies_df = pd.read_csv('movies.csv')

def recommend_movies(genre, rating):
    """
    Function to recommend movies based on user preferences.
    :param genre: Preferred genre
    :param rating: Minimum rating
    :return: List of recommended movies
    """
    recommended_movies = movies_df[(movies_df['Genre'] == genre) & (movies_df['Rating'] >= rating)]
    return recommended_movies

def main():
    print("Welcome to Movie Recommendation System")
    print("-------------------------------------")
    genre = input("Enter your preferred genre: ")
    rating = float(input("Enter your minimum rating (out of 10): "))

    recommended_movies = recommend_movies(genre, rating)

    if recommended_movies.empty:
        print("Sorry, no movies match your criteria.")
    else:
        print("\nRecommended Movies:")
        print(recommended_movies[['Title', 'Rating']])

if __name__ == "__main__":
    main()
