from  database_connection import DatabaseConnection

"""
format of the cvs file
name,author,read\n
"""


def create_book_table():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
 


def prompt_add_book():
    #",0); DROP TABLE books
    name = input("Name of the book: ")
    author = input("Name of the author: ")
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?,?,0)', (name, author))
    
    
def get_all_books():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2] } for row in cursor.fetchall()] #[(name,author,read), (name,author,read)]


    return books

def list_book():
    bookss = get_all_books()
    for book in bookss:

        read = 'Yes' if book['read'] else 'No' 
        print(f"{book['name']} by the {book['author']}. Is it read? {read}")

def prompt_read_book():
    which_read = input("Which book did you read? ")
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=? ', (which_read,))
   
            


def prompt_delete_book():
    which_delete = input("WHich book dou you want to delete? ")
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=? ', (which_delete,))
   

# prompt_add_book()
# prompt_add_book()

# list_book()
# prompt_read_book()
# prompt_delete_book()
# list_book()

