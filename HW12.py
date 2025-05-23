import sqlite3
connection = sqlite3.connect('books.db')
import pandas as pd
pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])
pd.read_sql('SELECT * FROM titles', connection)
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
df.head()
pd.read_sql('SELECT first, last FROM authors', connection)
pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection)
pd.read_sql("""SELECT id, first, last FROM authors WHERE last LIKE 'D%'""", connection, index_col=['id'])
pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""", connection, index_col=['id'])
