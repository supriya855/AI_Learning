import numpy as np

users = np.array([
    [5, 1, 0],  # user 0: likes action
    [1, 5, 0],  # user 1: likes comedy
    [0, 1, 5]   # user 2: likes romance
])

movies = np.array([
    [5, 0, 0],  # movie 0: action
    [0, 5, 0],  # movie 1: comedy
    [0, 0, 5],  # movie 2: romance
    [3, 3, 0],  # movie 3: action-comedy
])

scores = np.dot(users, movies.T)
print(scores)
# Calculate the similarity between users and movies using dot product
similarity1 = np.dot(users[0], movies[0])
similarity2 = np.dot(users[0], movies[1])
similarity3 = np.dot(users[0], movies[2])
similarity4 = np.dot(users[0], movies[3])
similarity = [similarity1, similarity2, similarity3, similarity4]         
print(similarity)
best_score = max(similarity)
best_movie_index = similarity.index(best_score)
print(f"User 0 should watch movie {best_movie_index} with a score of {best_score}.")