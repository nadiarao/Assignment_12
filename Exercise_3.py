import sqlite3
import pandas as pd
import uuid


connection = sqlite3.connect('books.db')

query_a = """
    SELECT last
    FROM authors
    ORDER BY last DESC 
"""     

result_a = pd.read_sql(query_a, connection)
print(result_a)

# Query to select book titles in ascending order

query_b = """
    SELECT title
    FROM titles
    ORDER BY title ASC
""" 

result_b = pd.read_sql(query_b, connection)
print(result_b)

#c) Use an INNER JOIN to select all the books for a specific author. Include the title, copyright year, and ISBN. Order the information alphabetically by title:

author_id = 1

query_c = f"""
    SELECT titles.title, titles.copyright, author_ISBN.isbn
    FROM titles
    INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn
    WHERE author_ISBN.id = {author_id}
    ORDER BY titles.title  ASC 
"""    

result_c = pd.read_sql(query_c, connection)
print(result_c)

#d) Insert a new author into the authors table:

query_d = """
    INSERT INTO authors (first, last)
    VALUES ('John', 'Doe')
"""    

connection.execute(query_d)
connection.commit()
print("Inserts complete")

#e) Insert a new title for an author:

author_id = 1 
isbn = str(uuid.uuid4())[:13]

query_e = f"""
    INSERT INTO titles (isbn, title, edition, copyright)
    VALUES ('{isbn}', 'New Book Title', '1st Edition', '2023')
"""

connection.execute(query_e)
connection.commit()

query_e_author_isbn = f"""
    INSERT INTO author_ISBN (id, isbn)
    VALUES ({author_id}, '{isbn}')
""" 

connection.execute(query_e_author_isbn)
connection.commit()

print("Inserts complete")