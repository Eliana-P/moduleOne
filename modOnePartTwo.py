
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('bestsellers_with_categories.csv')

data_cleaned = data.dropna(subset=['User Rating', 'Genre', 'Year'])

data_cleaned['Year'] = data_cleaned['Year'].astype(int)

# Filter Fiction and Non-Fiction books using genre
fiction_books = data_cleaned[data_cleaned['Genre'].str.contains('Fiction', case=False, na=False)]
non_fiction_books = data_cleaned[data_cleaned['Genre'].str.contains('Non[-\s]?Fiction', case=False, na=False)]

# Group by Year and Genre, calculate the average rating for each
fiction_avg_ratings = fiction_books.groupby('Year')['User Rating'].mean()
non_fiction_avg_ratings = non_fiction_books.groupby('Year')['User Rating'].mean()

avg_ratings = pd.DataFrame({
    'Fiction': fiction_avg_ratings,
    'Non Fiction': non_fiction_avg_ratings
})

plt.figure(figsize=(10, 6))

# Plot Fiction and Non-Fiction ratings
plt.plot(avg_ratings.index, avg_ratings['Fiction'], label='Fiction', color='blue', marker='o')
plt.plot(avg_ratings.index, avg_ratings['Non Fiction'], label='Non Fiction', color='green', marker='o')

plt.xlabel('Year')
plt.ylabel('Average User Rating')
plt.title('Average User Ratings for Fiction vs Non Fiction Books by Year')
plt.legend()

plt.grid(True)

plt.show()