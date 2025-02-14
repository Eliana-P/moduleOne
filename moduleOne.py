import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('bestsellers_with_categories.csv')

# Drop rows where any column has missing values
data_cleaned = data.dropna()

# Drop the 'Price' column
data_cleaned = data_cleaned.drop(columns=['Price'])


print(data.head())

print(data.columns)

fiction_books = data[data['Genre'].str.contains('Fiction', case=False, na=False)]
non_fiction_books = data[data['Genre'].str.contains('Non Fiction', case=False, na=False)]

#get rid of missing values for genre
fiction_books = fiction_books.dropna(subset=['User Rating'])
non_fiction_books = non_fiction_books.dropna(subset=['User Rating'])


# Calculate the average ratings for both genres
avg_fiction_rating = fiction_books['User Rating'].mean()
avg_non_fiction_rating = non_fiction_books['User Rating'].mean()


print(f"Average User Rating for Fiction books: {avg_fiction_rating}")
print(f"Average User Rating for Non Fiction books: {avg_non_fiction_rating}")


import matplotlib.pyplot as plt

# Create a bar chart comparing the average ratings for Fiction and Non-Fiction
genres = ['Fiction', 'Non Fiction']
avg_ratings = [avg_fiction_rating, avg_non_fiction_rating]

plt.bar(genres, avg_ratings, color=['blue', 'green'])
plt.xlabel('Genre')
plt.ylabel('Average User Rating')
plt.title('Average User Ratings for Fiction and Non Fiction Books')
plt.show()

