import sqlite3

db = sqlite3.connect('ebookstore_db')
cursor = db.cursor() # Get a cursor object

# Creating table
cursor.execute('''CREATE TABLE IF NOT EXISTS books(id INTERGER, 
title TEXT, author TEXT, qty INTERGER)''')

print('Database created!')
db.commit()

# Fintion to insert the five first books
def initial_libray():
    
    i_d = 3001
    title = 'A Tale of Two Cities'
    author = 'Charles Dickins'
    qty = 30

    cursor.execute('''INSERT INTO books VALUES(?,?,?,?)''', 
                (i_d, title, author, qty))

    print("Entry added!")
    db.commit()

    i_d = 3002
    title = "Harry Potter and the Philosopher's Tone"
    author = 'J.K. Rowling'
    qty = 40

    cursor.execute('''INSERT INTO books VALUES(?,?,?,?)''', 
                (i_d, title, author, qty))

    print("Entry added!")
    db.commit()

    i_d = 3003
    title = 'The Lion, the Witch, abd the Wardrobe'
    author = 'C.S Lewis'
    qty = 25

    cursor.execute('''INSERT INTO books VALUES(?,?,?,?)''', 
                (i_d, title, author, qty))

    print("Entry added!")
    db.commit()

    i_d = 3004
    title = 'The Lord of the Rings'
    author = 'J.R.R. Tolkien'
    qty = 37

    cursor.execute('''INSERT INTO books VALUES(?,?,?,?)''', 
                (i_d, title, author, qty))

    print("Entry added!")
    db.commit()

    i_d = 3005
    title = 'Alice in Wonderland'
    author = 'Lewis Carroll'
    qty = 12

    cursor.execute('''INSERT INTO books VALUES(?,?,?,?)''', 
                (i_d, title, author, qty))

    print("Entry added!")
    db.commit()

# Funtion to search for a specific book's details
def view_book():

    id_check = int(input("Please insert the ID of the book you'd like to search: "))
    cursor.execute('''SELECT * FROM books WHERE id=?''', (id_check,))

    data = cursor.fetchone()
    print(data)

# Function to insert a new book in the data base
def add_book():
    
    i_d = int(input("Enter the id of this book entry: "))
    title = input("Enter the title of the book entry: ")
    author = input("Enter the author of the book entry: ")
    qty = int(input("Enter the quantity of the book in stock: "))

    cursor.execute('''INSERT INTO books VALUES(?,?,?,?)''', 
                (i_d, title, author, qty))

    print("New book added!")
    db.commit()

# Funtion to update book's details
def update_book():

    cursor.execute('''SELECT * FROM books''')

    data = cursor.fetchall()
    print(data)

    id_select = int(input("Please select the ID of the book you would like to edit: "))

    edit_choice = input("What aspect would you like to edit (id, title, author, qty): ")

# If statement to update title, id, author, or quantity
    if edit_choice == "title":

        new_title = input("Please enter the new title of the book: ")

        cursor.execute('''UPDATE books SET title = ? WHERE id = ?
                        ''', (new_title, id_select,))

        print("Entry updated")
        db.commit()

    elif edit_choice == "id":

        new_id = input("Please enter the new id of the book: ")

        cursor.execute('''UPDATE books SET id = ? WHERE id = ?
                        ''', (new_id, id_select,))

        print("Entry updated")
        db.commit()

    elif edit_choice == "author":

        new_author = input("Please enter the new author of the book: ")

        cursor.execute('''UPDATE books SET author = ? WHERE id = ?
                        ''', (new_author, id_select,))

        print("Entry updated")
        db.commit()

    elif edit_choice == "qty":

        cursor.execute('''SELECT * FROM books''')

        data = cursor.fetchall()
        print(data)

        new_qty = input("Please enter the new qty of the book: ")

        cursor.execute('''UPDATE books SET qty = ? WHERE id = ?
                        ''', (new_qty, id_select,))

        print("Entry updated")
        db.commit()

# Function to delete books
def delet_book():

    cursor.execute('''SELECT * FROM books''')

    data = cursor.fetchall()
    print(data)

    id_select = int(input("Please select the ID of the book you would like to delete: "))

    cursor.execute('''
                    DELETE FROM books WHERE id = ?
                    ''', (id_select,))    
    
    print("Entry removed!")
    db.commit()

# Loop to introduce to the user a menu
while True:

    data_entry = input(str('''Please select one fo the following options:
                        'initial' to add the first five books,
                        'add' to add anew book to the data base,
                        'update' to update any book's information,
                        'delete' to delete any book,
                        'search' to search for a specific book,
                        or 'finish' to finish with the program: '''))

    if data_entry == 'initial':
        initial = initial_libray()
        continue
    elif data_entry == 'add':
        initial = add_book()
        continue
    elif data_entry == 'update':
        initial = update_book()
        continue
    elif data_entry == 'delete':
        initial = delet_book()
        continue
    elif data_entry == 'search':
        initial = view_book()
        continue
    elif data_entry == 'finish':
        print("The program is closed")
        break
    else:
        print("Please enter a valid option")
        continue


