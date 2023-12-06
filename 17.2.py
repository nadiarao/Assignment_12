import sqlite3
connection = sqlite3.connect('books.db')

import pandas as pd
pd.options.display.max_colums = 10

pd.read_sql('SELECT * FROM authors', connection,
             index_col=['id'])

pd.read_sql('SELECT * FROM title', connection)
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
df.head()

pd. read_sql("""SELECT title, edition, copyright 
             FROM titles 
             WHERE copyright > '2016'""", connection)

pd.read_sql("""SELECT id, first, last
            FROM authors
            WHERE last LIKE 'D%'""",
            connection, index_col=['id'])

pd.read_sql('SELECT title FROM titles ORDER BY title ASC',
            connection)
pd.read_sql("""SELECT id, first, last
            FROM authors
            ORDER BY last, first""",
            connection, index_col=['id'])
pd.read_sql("""SELECT id, first, last
            FROM authors
            ORDER BY last DESC, first ASC""",
            connection, index_col=['id'])
pd.read_sql("""SELECT isbn, title, edition, copyright
            FROM titles
            WHERE title LIKE '%How to Program'
            ORDER BY title""", connection)
pd.read_sql(""" SELECT first, last, isbn
            FROM authors
            INNER JOIN author_ISBN
                ON authors.id = author_ISBN.id
            ORDER BY last, first""", connection).head()
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
                        VALUES ('Sue', 'Red')""")
pd.read_sql('SELECT id, first, last FROM authors',
            connection, index_col=['id'])
cursor = cursor.execute("""UPDATE authors SET last='Black'
                        WHERE last='Red' AND first='SUE'""")
cursor.rowcount

pd.read_sql('SELECT id, first, last FROM authors',
            connection, index_col=['id'])
cursor = cursor.execute('DELETE FROM authors WHERE id=6')

cursor.rowcount

pd.read_sql('SELECT id, first, last FROM authors',
            connection, index_col=['id'])
pd.read_sql("""SELECT title, edition FROM titles
            ORDER BY edition DESC""", connection).head(3)

pd.read_sql("""SELECT * FROM authors
            WHERE first LIKE 'A%'""", connection)
pd.read_sql("""SELECT isbn, title, edition , copyright
            FROM titles
            WHERE title NOT LIKE '%How to Program'
            ORDER BY title""", connection)



