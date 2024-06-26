import pandas as pd

movies = pd.read_csv('/Users/saulo/Downloads/archive/movies.csv')
movies.info() # see information about dataset

#see first 10 rows
pd.set_option('display.max_columns', None)
print(movies.head(10))


#removing projects with less than 50 minutes runtime
movies2 = movies[movies['runtime'] > 50 ]
#removing projects with more than 300 minutes runtime
movies3 = movies2[movies2['runtime'] <= 300]

#checking min and max runtime
min_runtime = movies3['runtime'].min()
print(min_runtime)

max_runtime = movies3['runtime'].max()
print(max_runtime)

#removing rows with zero revenue
movies3 = movies3[movies3['revenue'] > 100000]

#removing projects with 0 in budget
movies3 = movies3[movies3['budget'] > 0]

#checking min revenue
min_revenue = movies3['revenue'].min()
print(min_revenue)

#checking total rows
row_count = len(movies3)
print(f'it contains {row_count} rows')

#exporting file
movies3.to_csv('C:/Users\saulo/OneDrive/Desktop/movies3.csv')






