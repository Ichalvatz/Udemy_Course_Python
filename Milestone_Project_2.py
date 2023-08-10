from utils import database


USER_CHOISE = """
ENter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choise: """
# choise_menu = {
#             'a' : print(),
#             'l' : print(),
#             'r' : print(),
#             'd' : pr int()
#         }

def menu():
    database.create_book_table()
    user_input = input(USER_CHOISE)
    while user_input != 'q':
        if user_input == 'a':
            database.prompt_add_book()
        elif user_input == 'l':
            database.list_book()
        elif user_input == 'r':
            database.prompt_read_book()
        elif user_input == 'd':
            database.prompt_delete_book()
        elif user_input =='s':
            pass
        else:
            print("Wrong input buddy choose again!")
        user_input = input(USER_CHOISE)

menu()
"""
Another option: every time a book is added, read, changed, or deleted,
change the file contents so that it matches what the application is showing."""