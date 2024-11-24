import mysql.connector
import pyfiglet
import wikipediaapi
import os

from datetime import datetime


def connectToLibrary():
    """
    @brief Creates a database connection to the Library database.
    @return A tuple of database connection and cursor object.
    """
    con = mysql.connector.connect(
        host="localhost",
        user="anand_maurya",
        password="ANAND6308anand",
        database="Library",
        collation="utf8mb4_unicode_520_ci",
    )
    if not con.is_connected():
        print("Can't connect to database, try reloading.")
        exit(1)
    cursor = con.cursor()
    return con, cursor


def clearScreen() -> None:
    """
    @brief Clears the terminal screen of any previous content.
    """
    if os.name == "nt":  # windows system.
        os.system("cls")
    else:  # unix based system.
        os.system("clear")


def exitLibrary() -> None:
    """
    @brief Exits the program with a exit message.
    """
    clearScreen()
    print("\033[3;34m+-----------------------------+\033[0m")
    print("Exiting the program, Thank You!")
    print("\033[3;34m+-----------------------------+\033[0m")
    exit(0)


def printInvalidOptionInterface() -> None:
    """
    @brief Prints debug info if the user selected invalid option.
    """
    print("\n\033[3;31m+---------------------+\033[0m")
    print("Invalid option selected")
    print("\033[3;31m+---------------------+\033[0m\n")
    input("Press Enter to continue: ")


def printAdminInterface() -> None:
    """
    @brief Print the admin screen's interface.
    """
    clearScreen()
    print("\033[3;34m+---+\033[0m")
    print("Admin")
    print("\033[3;34m+---+\033[0m\n")
    print("1: Login into User Panel")
    print("2: Modify User")
    print("3: Display Users")
    print("4: Search Users")
    print("5: Modify Book")
    print("6: Issue Book")
    print("7: Return Book")
    print("8: Add Admin")
    print("9: Back")
    print("10: Exit")
    print("\033[3;34m+----------------------+\033[0m\n")


def printModifyUserInterface() -> None:
    """
    @brief Print the modify user screen's interface.
    """
    clearScreen()
    print("\033[3;34m+----------------+\033[0m")
    print("Modify User Screen")
    print("\033[3;34m+----------------+\033[0m\n")
    print("1: Add User")
    print("2: Delete User")
    print("3: Update User")
    print("4: Back")
    print("5: Exit")
    print("\033[3;34m+------------+\033[0m\n")


def addUser(db_con, db_cursor) -> None:
    """
    @brief Adds a new user to the users table in the Library database.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+------+\033[0m")
    print("Add User")
    print("\033[3;34m+------+\033[0m\n")
    id = int(input("Enter the user id for the user: "))
    name = input("Enter the username for the user: ")
    ph_no = input("Enter the phone number for the user: ")
    email = input("Enter the email for the user: ")
    passwd = input("Enter the password for the user: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT userId FROM users WHERE userId = {id}")
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        print(f"The user with the userId: {id} already exists, try again.")
    else:
        db_cursor.execute(
            f'INSERT INTO users VALUES({id}, "{name}", "{ph_no}", "{email}", "{passwd}", "not admin")'
        )
        db_con.commit()
        print("User added successfully.")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def deleteUser(db_con, db_cursor) -> None:
    """
    @brief Delete an existing user from the users table.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+---------+\033[0m")
    print("Delete User")
    print("\033[3;34m+---------+\033[0m\n")
    id = int(input("Enter the user ID to delete: "))
    choice = input("Are you sure you want to delete the note? (Y/N): ").lower()
    print("\033[3;34m+------------------------+\033[0m\n")
    if choice in ["yes", "y"]:
        db_cursor.execute(f"SELECT userId FROM users WHERE userId = {id}")
        # A check to confirm that if the user can perform the action they are trying to do.
        does_exist = bool(db_cursor.fetchall())
        if does_exist:
            db_cursor.execute(f"DELETE FROM users WHERE userId = {id}")
            db_con.commit()
            print(f"The user with userId: {id} deleted successfully.")
        else:
            print(f"The user with userId: {id} does not exist.")
    else:
        print("User not deleted!")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def printUpdateUserInterface() -> None:
    """
    @brief Print the update user screen's interface.
    """
    clearScreen()
    print("\033[3;34m+----------------+\033[0m")
    print("Update User Screen")
    print("\033[3;34m+----------------+\033[0m\n")
    print("1: Update User Id")
    print("2: Update User Name")
    print("3: Update User Phone Number")
    print("4: Update User Email")
    print("5: Update User Password")
    print("6: Back")
    print("7: Exit")
    print("\033[3;34m+-------------------------+\033[0m\n")


def updateUserId(db_con, db_cursor) -> None:
    """
    @brief Updates user id of the given user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+------------+\033[0m")
    print("Update User Id")
    print("\033[3;34m+------------+\033[0m\n")
    curr = int(input("Enter the user ID to update: "))
    new = input("Enter the new user ID to set: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT userId FROM users WHERE userId = {curr}")
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f"UPDATE users\
            SET userId = {new}\
            WHERE userId = {curr}"
        )
        db_con.commit()
        print(f"Current user Id: {curr} successfully changed to: {new}")
    else:
        print(f"We don't have any user with Id: {curr}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateUserName(db_con, db_cursor) -> None:
    """
    @brief Updates user name of the given user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+--------------+\033[0m")
    print("Update User Name")
    print("\033[3;34m+--------------+\033[0m\n")
    id = int(input("Enter the user ID to update: "))
    new = input("Enter the new name to set: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT userId FROM users WHERE userId = {id}")
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f'UPDATE users\
            SET userName = "{new}"\
            WHERE userId = {id}'
        )
        db_con.commit()
        print(f"Name of the user with  user Id: {id} successfully changed to: {new}")
    else:
        print(f"We don't have any user with Id: {id}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateUserPhoneNumber(db_con, db_cursor) -> None:
    """
    @brief Updates user phone number of the given user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+----------------------+\033[0m")
    print("Update User Phone Number")
    print("\033[3;34m+----------------------+\033[0m\n")
    id = int(input("Enter the user ID to update: "))
    new = input("Enter the new phone number to set: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT userId FROM users WHERE userId = {id}")
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f'UPDATE users\
            SET phoneNumber = "{new}"\
            WHERE userId = {id}'
        )
        db_con.commit()
        print(f"Phone of the user with  user Id: {id} successfully changed to: {new}")
    else:
        print(f"We don't have any user with Id: {id}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateUserEmailId(db_con, db_cursor) -> None:
    """
    @brief Updates email id of the given user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+---------------+\033[0m")
    print("Update User Email")
    print("\033[3;34m+---------------+\033[0m\n")
    id = int(input("Enter the user ID to update: "))
    new = input("Enter the new email to set: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT userId FROM users WHERE userId = {id}")
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f'UPDATE users\
            SET emailId = "{new}"\
            WHERE userId = {id}'
        )
        db_con.commit()
        print(f"Email of the user with  user Id: {id} successfully changed to: {new}")
    else:
        print(f"We don't have any user with Id: {id}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateUserPassword(db_con, db_cursor) -> None:
    """
    @brief Updates password of the given user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+------------------+\033[0m")
    print("Update User Password")
    print("\033[3;34m+------------------+\033[0m\n")
    id = int(input("Enter the user ID to update: "))
    new = input("Enter the new password to set: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT userId FROM users WHERE userId = {id}")
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f'UPDATE users\
            SET password = "{new}"\
            WHERE userId = {id}'
        )
        db_con.commit()
        print(
            f"Password of the user with  user Id: {id} successfully changed to: {new}"
        )
    else:
        print(f"We don't have any user with Id: {id}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateUser(db_con, db_cursor) -> None:
    """
    @brief The update user screen for admin.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    while True:
        printUpdateUserInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            updateUserId(db_con, db_cursor)
        elif choice == "2":
            updateUserName(db_con, db_cursor)
        elif choice == "3":
            updateUserPhoneNumber(db_con, db_cursor)
        elif choice == "4":
            updateUserEmailId(db_con, db_cursor)
        elif choice == "5":
            updateUserPassword(db_con, db_cursor)
        elif choice == "6":
            break
        elif choice == "7":
            exitLibrary()
        else:
            printInvalidOptionInterface()


def modifyUser(db_con, db_cursor) -> None:
    """
    @brief The modify user screen for admin.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    while True:
        printModifyUserInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            addUser(db_con, db_cursor)
        elif choice == "2":
            deleteUser(db_con, db_cursor)
        elif choice == "3":
            updateUser(db_con, db_cursor)
        elif choice == "4":
            break
        elif choice == "5":
            exitLibrary()
        else:
            printInvalidOptionInterface()


def displayUsers(db_cursor) -> None:
    """
    @brief Display's all the users in the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+-----------+\033[0m")
    print("Display Users")
    print("\033[3;34m+-----------+\033[0m\n")
    fetch_query = "SELECT userId, userName, phoneNumber, emailId issueStatus FROM users"
    db_cursor.execute(fetch_query)
    users = db_cursor.fetchall()
    if users:
        print("\033[3;34m+--------------------------+\033[0m")
        print("User in the Digital Library:")
        print("\033[3;34m+--------------------------+\033[0m")
        for i, row in enumerate(users):
            print(f"{i + 1}. User ID : {row[0]}")
            print(f"User Name : {row[1]}")
            print(f"Phone Number : {row[2]}")
            print(f"Email ID : {row[3]}")
            print("\033[3;34m+------------------------+\033[0m")
        print()
    else:
        print("\033[3;34m+------------------------+\033[0m\n")
        print("No users found.")
        print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def printSearchUserInterface() -> None:
    """
    @brief Print the search user screen's interface.
    """
    clearScreen()
    print("\033[3;34m+----------------+\033[0m")
    print("Search User Screen")
    print("\033[3;34m+----------------+\033[0m\n")
    print("1: Search User By ID")
    print("2: Search User By Keyword")
    print("3: Back")
    print("4: Exit")
    print("\033[3;34m+-----------------------+\033[0m\n")


def searchUserById(db_cursor) -> None:
    """
    @brief Searches for user with the given user id.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+----------------+\033[0m")
    print("Search Users By ID")
    print("\033[3;34m+----------------+\033[0m\n")
    id = int(input("Enter the userID to search: "))
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(
        f"SELECT userName, phoneNumber, emailId FROM users where userId = {id}"
    )
    user = db_cursor.fetchall()
    if user:
        print(f"User in the Digital Library with the user ID '{id}' is :")
        print("\033[3;34m+------------------------+\033[0m")
        print(f"User ID : {id}")
        print(f"User Name : {user[0][0]}")
        print(f"User Phone Number : {user[0][1]}")
        print(f"User Email Id: {user[0][2]}")
    else:
        print(f'No user found with the user id "{id}".')
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def searchUserByKeyword(db_cursor) -> None:
    """
    @brief Searches for user with the given user id.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+---------------------+\033[0m")
    print("Search Users By Keyword")
    print("\033[3;34m+---------------------+\033[0m\n")
    keyword = input("Enter the keyword to search:")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(
        f"SELECT userId, userName, phoneNumber, emailId FROM users WHERE userName LIKE '%{keyword}%'"
    )
    users = db_cursor.fetchall()
    if users:
        print(f"Users in the Digital Library with the Keyword '{keyword}' are :")
        print("\033[3;34m+------------------------+\033[0m")
        for i, row in enumerate(users):
            print(f"{i + 1}. User ID : {row[0]}")
            print(f"User Name : {row[1]}")
            print(f"User Phone Number : {row[2]}")
            print(f"User Email Address : {row[3]}")
            print("\033[3;34m+------------------------+\033[0m")
        print()
    else:
        print(f"No user with the keyword: '{keyword}' found.")
        print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def searchUsers(db_cursor) -> None:
    """
    @brief The search user screen for admin.
    @param db_cursor The cursor object to the Library database.
    """
    while True:
        printSearchUserInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            searchUserById(db_cursor)
        elif choice == "2":
            searchUserByKeyword(db_cursor)
        elif choice == "3":
            break
        elif choice == "4":
            exitLibrary()
        else:
            printInvalidOptionInterface()


def printModifyBookInterface() -> None:
    """
    @brief Print the modify book screen's interface.
    """
    clearScreen()
    print("\033[3;34m+----------------+\033[0m")
    print("Modify Book Screen")
    print("\033[3;34m+----------------+\033[0m\n")
    print("1: Add Book")
    print("2: Delete Book")
    print("3: Update Book")
    print("4: Back")
    print("5: Exit")
    print("\033[3;34m+------------+\033[0m\n")


def addBook(db_con, db_cursor) -> None:
    """
    @brief Adds a book into the books table in Library database.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+------+\033[0m")
    print("Add Book")
    print("\033[3;34m+------+\033[0m\n")
    id = int(input("Enter the book id for the book: "))
    name = input("Enter the name for the book: ")
    publication_year = int(input("Enter the publication year of the book: "))
    author = input("Enter the author for the book: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT bookId FROM books WHERE bookId = {id}")
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        print(f"The book with the bookId: {id} already exists, try again.")
    else:
        db_cursor.execute(
            f'INSERT INTO books(bookId, bookName, publicationYear, author)\
            VALUES({id}, "{name}", {publication_year}, "{author}")'
        )
        db_con.commit()
        print("Book added successfully.")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def deleteBook(db_con, db_cursor) -> None:
    """
    @brief Delete an existing book from the users table.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+---------+\033[0m")
    print("Delete Book")
    print("\033[3;34m+---------+\033[0m\n")
    id = int(input("Enter the book ID to delete: "))
    choice = input("Are you sure you want to delete the note? (Y/N): ").lower()
    print("\033[3;34m+------------------------+\033[0m\n")
    if choice in ["yes", "y"]:
        db_cursor.execute(f"SELECT bookId FROM books WHERE bookId = {id}")
        # A check to confirm that if the user can perform the action they are trying to do.
        does_exist = bool(db_cursor.fetchall())
        if does_exist:
            db_cursor.execute(f"DELETE FROM books WHERE bookId = {id}")
            db_con.commit()
            print(f"The book with bookId: {id} deleted successfully.")
        else:
            print(f"The book with bookId: {id} does not exist.")
    else:
        print("Book not deleted!")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def printUpdateBookInterface() -> None:
    """
    @brief Print the update book screen's interface.
    """
    clearScreen()
    print("\033[3;34m+----------------+\033[0m")
    print("Modify Book Screen")
    print("\033[3;34m+----------------+\033[0m\n")
    print("1: Update Book Id")
    print("2: Update Book Name")
    print("3: Update Book Publication Year")
    print("4: Update Book Author")
    print("5: Back")
    print("6: Exit")
    print("\033[3;34m+------------+\033[0m\n")


def updateBookId(db_con, db_cursor) -> None:
    """
    @brief Updates the book id of an existing book.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+------------------+\033[0m")
    print("Update Book Id")
    print("\033[3;34m+------------------+\033[0m\n")
    id = int(input("Enter the book ID to update: "))
    new = int(input("Enter the new book ID to set: "))
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT bookId FROM books WHERE bookId = {id}")
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f"UPDATE books\
            SET bookId = {new}\
            WHERE bookId = {id}"
        )
        db_con.commit()
        print(f"Book Id: {id} successfully changed to: {new}")
    else:
        print(f"We don't have any book with Id: {id}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateBookName(db_con, db_cursor) -> None:
    """
    @brief Updates the book name of an existing book.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+--------------------+\033[0m")
    print("Update Book Name")
    print("\033[3;34m+--------------------+\033[0m\n")
    id = int(input("Enter the book ID to update: "))
    new = input("Enter the new book name to set: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT bookId FROM books WHERE bookId = {id}")
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f'UPDATE books\
            SET bookName = "{new}"\
            WHERE bookId = {id}'
        )
        db_con.commit()
        print(f"Book name of the book with Id: {id} successfully changed to: {new}")
    else:
        print(f"We don't have any book with Id: {id}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateBookPublicationYear(db_con, db_cursor) -> None:
    """
    @brief Updates the book publication year of an existing book.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+--------------------------------+\033[0m")
    print("Update Book Publication Year")
    print("\033[3;34m+--------------------------------+\033[0m\n")
    id = int(input("Enter the book ID to update: "))
    new = input("Enter the new book publication year to set: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT bookId FROM books WHERE bookId = {id}")
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f"UPDATE books\
            SET publicationYear = {new}\
            WHERE bookId = {id}"
        )
        db_con.commit()
        print(
            f"Book publication year of the book with Id: {id} successfully changed to: {new}"
        )
    else:
        print(f"We don't have any book with Id: {id}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateBookAuthor(db_con, db_cursor) -> None:
    """
    @brief Updates the book author of an existing book.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+----------------------+\033[0m")
    print("Update Book Author")
    print("\033[3;34m+----------------------+\033[0m\n")
    id = int(input("Enter the book ID to update: "))
    new = input("Enter the new book author to set: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT bookId FROM books WHERE bookId = {id}")
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f'UPDATE books\
            SET author = "{new}"\
            WHERE bookId = {id}'
        )
        db_con.commit()
        print(f"Book author of the book with Id: {id} successfully changed to: {new}")
    else:
        print(f"We don't have any book with Id: {id}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateBook(db_con, db_cursor) -> None:
    """
    @brief The update book screen for the admin.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    while True:
        printUpdateBookInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            updateBookId(db_con, db_cursor)
        elif choice == "2":
            updateBookName(db_con, db_cursor)
        elif choice == "3":
            updateBookPublicationYear(db_con, db_cursor)
        elif choice == "4":
            updateBookAuthor(db_con, db_cursor)
        elif choice == "5":
            break
        elif choice == "6":
            exitLibrary()
        else:
            printInvalidOptionInterface()


def modifyBook(db_con, db_cursor) -> None:
    """
    @brief The modify book screen for the admin.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    while True:
        printModifyBookInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            addBook(db_con, db_cursor)
        elif choice == "2":
            deleteBook(db_con, db_cursor)
        elif choice == "3":
            updateBook(db_con, db_cursor)
        elif choice == "4":
            break
        elif choice == "5":
            exitLibrary()
        else:
            printInvalidOptionInterface()


def issueBook(db_con, db_cursor) -> None:
    """
    @brief Allows the admin to issue a book to a user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+--------------+\033[0m")
    print("Issue Book")
    print("\033[3;34m+--------------+\033[0m\n")
    book_id = int(input("Enter the book ID to issue: "))
    user_id = int(input("Enter the user ID to issue the book to: "))
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(
        f"SELECT issueStatus, bookName FROM books WHERE bookId = {book_id}"
    )
    # We don't bool cast it as we need to access the issueStatus
    book_data = db_cursor.fetchall()
    db_cursor.execute(f"SELECT userId FROM users WHERE userId = {user_id}")
    does_user_exist = bool(db_cursor.fetchall())
    if not book_data:
        print(f"The book with the Id: {book_id} does not exist.")
    elif book_data[0][0] == "issued":
        print(f"The book with the Id: {book_id} is already issued.")
    elif not does_user_exist:
        print(f"The user with the Id: {user_id} does not exist.")
    else:
        db_cursor.execute(
            f"UPDATE books SET issueStatus = 'issued' WHERE bookId = {book_id}"
        )
        db_cursor.execute(
            f"INSERT INTO issuedbooksdetails\
                          VALUES ({user_id}, {book_id}, CURRENT_DATE, CURRENT_TIME, NULL, NULL, 0, '{book_data[0][1]}')"
        )
        db_con.commit()
        print(f"Book with Id: {book_id} issued to user with the Id: {user_id}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def returnBook(db_con, db_cursor) -> None:
    """
    @brief Allows to return a book from a user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+--------------+\033[0m")
    print("Issue Book")
    print("\033[3;34m+--------------+\033[0m\n")
    book_id = int(input("Enter the book ID to return: "))
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT issueStatus FROM books WHERE bookId = {book_id}")
    issue_status = db_cursor.fetchall()
    # This is a good enough fix as we can't add books which haven't been returned yet.
    # We need user_id to pin point the correct user that is returning the book.
    db_cursor.execute(
        f"SELECT userId FROM issuedbooksdetails WHERE bookId = {book_id} AND returnDate IS NULL"
    )
    user_id = db_cursor.fetchall()[0][0]
    if not issue_status:
        print(f"The book with the Id: {book_id} does not exist.")
    elif issue_status[0][0] == "not issued":
        print(f"The book with the Id: {book_id} has not been issued yet.")
    else:
        db_cursor.execute(
            f'UPDATE books SET issueStatus = "not issued" WHERE bookId = {book_id}'
        )
        db_cursor.execute(
            f"UPDATE issuedbooksdetails SET returnDate = CURRENT_DATE, returnTime = CURRENT_TIME WHERE bookId = {book_id} AND userId = {user_id}"
        )
        db_con.commit()
        db_cursor.execute(
            f"SELECT issueDate, returnDate FROM issuedbooksdetails WHERE bookId = {book_id} AND userId = {user_id}"
        )
        issue_date, return_date = db_cursor.fetchall()[0]
        date_difference = datetime.strptime(
            f"{return_date}", "%Y-%m-%d"
        ) - datetime.strptime(f"{issue_date}", "%Y-%m-%d")
        # The 14 and 5 are explained in the returnPolicy function.
        if date_difference.days > 14:
            fine = (date_difference.days - 14) * 5
            if fine != 0:
                db_cursor.execute(
                    f"UPDATE issuedbooksdetails SET fineInRs = {fine} WHERE bookId = {book_id} and userId = {user_id}"
                )
        print("Book returned successfully")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def addAdmin(db_con, db_cursor) -> None:
    """
    @brief Adds a admin.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+----------------+\033[0m")
    print("Change Admin")
    print("\033[3;34m+----------------+\033[0m\n")
    to_promote = int(input("Enter the user id to promote to admin: "))
    choice = input("Do you really want to do it: (Y/N)").lower()
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(f"SELECT adminStatus FROM users WHERE userId = {to_promote}")
    admin_status = db_cursor.fetchall()
    if not admin_status:
        print(f"The user with the Id: {to_promote} does not exist.")
    elif admin_status[0][0] == "admin":
        print(f"The user with the Id: {to_promote} is already an admin.")
    elif choice in ["yes", "y"]:
        db_cursor.execute(f"UPDATE users SET adminStatus = 'admin' WHERE userID = {to_promote}")
        db_con.commit()
        print(f"The user with Id: {to_promote} successfully promoted to admin status.")
    else:
        print(f"The user with the Id: {to_promote} was not promoted.")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def adminScreen(login_id: int, db_con, db_cursor) -> None:
    """
    @brief The admin screen displaying all the options for the admin.
    @param login_id The login id of the current logged in user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    while True:
        printAdminInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            userScreen(login_id, db_con, db_cursor)
        elif choice == "2":
            modifyUser(db_con, db_cursor)
        elif choice == "3":
            displayUsers(db_cursor)
        elif choice == "4":
            searchUsers(db_cursor)
        elif choice == "5":
            modifyBook(db_con, db_cursor)
        elif choice == "6":
            issueBook(db_con, db_cursor)
        elif choice == "7":
            returnBook(db_con, db_cursor)
        elif choice == "8":
            addAdmin(db_con, db_cursor)
        elif choice == "9":
            break
        elif choice == "10":
            exitLibrary()
        else:
            printInvalidOptionInterface()


def printUserInterface() -> None:
    """
    @brief Print the user screen's interface.
    """
    clearScreen()
    print("\033[3;34m+---------+\033[0m")
    print("User Screen")
    print("\033[3;34m+---------+\033[0m\n")
    print("1: About Library")
    print("2: Wikipedia Articles")
    print("3: Display Books")
    print("4: Search Books")
    print("5: Issued Books Details")
    print("6: Access Notes Menu")
    print("7: Back")
    print("8: Exit")
    print("\033[3;34m+---------------------+\033[0m\n")


def aboutLibrary(db_cursor) -> None:
    """
    @brief Displays information about the library.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    db_cursor.execute("SELECT userName FROM users WHERE adminStatus = 'admin'")
    username = db_cursor.fetchall()[0][0]
    db_cursor.execute("SELECT COUNT(*) FROM books")
    total_books = db_cursor.fetchall()[0][0]
    db_cursor.execute("SELECT COUNT(*) FROM users")
    total_users = db_cursor.fetchall()[0][0]

    print("\033[3;34m+-----------+\033[0m")
    print("About Library")
    print("\033[3;34m+-----------+\033[0m\n")
    print("Year of Library's Establishment : ", 1860)
    print("Name of the librarian : ", username)
    print("Total number of books available in the library : ", total_books)
    print("Total number of users enrolled in the library : ", total_users)
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def wikipediaArticles() -> None:
    """
    @brief Allows the user to search a article on wikipedia based
    on a specific keyword inputted by the user.
    """
    clearScreen()
    print("\033[3;34m+-------------+\033[0m")
    print("Search Articles")
    print("\033[3;34m+-------------+\033[0m\n")
    keyword = input("Enter the keyword for searching wikipedia article: ")
    wiki = wikipediaapi.Wikipedia(language="en", user_agent="digitallibrary/1.1")
    page = wiki.page(keyword)
    print("\n\033[3;34m+------------------------+\033[0m")
    if not page.exists():
        print(f"Sorry, no wikipedia page for the keyword: '{keyword}' exists.")
    else:
        print(f"Title: {page.title}")
        print(f"URL: {page.fullurl}")
        print("Summary : ")
        print(page.summary)
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def displayBooks(db_cursor) -> None:
    """
    @brief Displays all the books present in the library.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+-----------+\033[0m")
    print("Display Books")
    print("\033[3;34m+-----------+\033[0m\n")
    fetch_query = (
        "SELECT bookId, bookName, publicationYear, author, issueStatus FROM books"
    )
    db_cursor.execute(fetch_query)
    books = db_cursor.fetchall()
    if books:
        print("\033[3;34m+-------------------------------------+\033[0m")
        print("Books available in the Digital Library:")
        print("\033[3;34m+-------------------------------------+\033[0m")
        for i, row in enumerate(books):
            print(f"{i + 1}. Book ID : {row[0]}")
            print(f"Book Name : {row[1]}")
            print(f"Publication Year : {row[2]}")
            print(f"Author Name : {row[3]}")
            print(f"Issue Status : {row[4]}")
            print("\033[3;34m+------------------------+\033[0m")
        print()
    else:
        print("\033[3;34m+------------------------+\033[0m\n")
        print("No books found.")
        print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def printSearchBooksInterface() -> None:
    """
    @brief Prints the search books interface.
    """
    clearScreen()
    print("\033[3;34m+----------+\033[0m")
    print("Search Books")
    print("\033[3;34m+----------+\033[0m\n")
    print("1: Search by Book ID")
    print("2: Search by Keyword")
    print("3: Back")
    print("4: Exit")
    print("\033[3;34m+------------------+\033[0m\n")


def searchBookById(db_cursor) -> None:
    """
    @brief Searches book with the given id.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+----------------+\033[0m")
    print("Search Books By ID")
    print("\033[3;34m+----------------+\033[0m\n")
    id = int(input("Enter the bookID to search: "))
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(
        f"SELECT bookName, publicationYear, author, issueStatus FROM books where bookId = {id}"
    )
    book = db_cursor.fetchall()
    if book:
        print(f"Book available in the Digital Library with the Book ID '{id}' is :")
        print("\033[3;34m+------------------------+\033[0m")
        print(f"Book ID : {id}")
        print(f"Book Name : {book[0][0]}")
        print(f"Publication Year : {book[0][1]}")
        print(f"Author Name : {book[0][2]}")
        print(f"Issue Status : {book[0][3]}")
    else:
        print(f'No book found with the book id "{id}".')
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def searchBookByKeyword(db_cursor) -> None:
    """
    @brief Searches book with the given keyword.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+---------------------+\033[0m")
    print("Search Books By Keyword")
    print("\033[3;34m+---------------------+\033[0m\n")
    keyword = input("Enter the keyword to search:")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(
        f"SELECT bookId, bookName, publicationYear, author, issueStatus FROM books WHERE bookName LIKE '%{keyword}%'"
    )
    books = db_cursor.fetchall()
    if books:
        print(
            f"Books available in the Digital Library with the Keyword '{keyword}' are :"
        )
        print("\033[3;34m+------------------------+\033[0m")
        for i, row in enumerate(books):
            print(f"{i + 1}. Book ID : {row[0]}")
            print(f"Book Name : {row[1]}")
            print(f"Publication Year : {row[2]}")
            print(f"Author Name : {row[3]}")
            print(f"Issue Status : {row[4]}")
            print("\033[3;34m+------------------------+\033[0m")
        print()
    else:
        print(f"No book with the keyword: '{keyword}' found.")
        print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def searchBooks(db_cursor) -> None:
    """
    @brief Allows the user to search book in the library based
    on user's choices.
    @param db_cursor The cursor object to the Library database.
    """
    while True:
        printSearchBooksInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            searchBookById(db_cursor)
        elif choice == "2":
            searchBookByKeyword(db_cursor)
        elif choice == "3":
            break
        elif choice == "4":
            exitLibrary()
        else:
            printInvalidOptionInterface()


def printReturnPolicy() -> None:
    """
    @brief Prints the return policy to the screen.
    """
    print("\033[3;34m+------------------------+\033[0m")
    print("Return Policy : ")
    print("The issued book should be returned within 14 days(2 weeks).")
    print(
        "If the user kept the issued book for more than 14 days, then the\n\
        user have to pay ₹5 as fine for each extra day the user kept the issued\n\
        book."
    )
    print("\033[3;34m+------------------------+\033[0m\n")


def issuedBooksDetails(login_id: int, db_cursor) -> None:
    """
    @brief Displays details about issued books to the user.
    @param login_id The login id of the current logged in user.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+-----------+\033[0m")
    print("Display Books")
    print("\033[3;34m+-----------+\033[0m\n")
    printReturnPolicy()
    fetch_query = f"SELECT bookId, issueDate, issueTime, returnDate, returnTime, fineInRs, bookName FROM issuedbooksdetails WHERE userId = {login_id}"
    db_cursor.execute(fetch_query)
    details = db_cursor.fetchall()
    if details:
        print(
            f"Details about the issued notes by the user with login id: {login_id} are:"
        )
        print("\033[3;34m+------------------------+\033[0m")
        for i, row in enumerate(details):
            print(f"{i + 1}. Book ID : {row[0]}")
            print(f"Book Name : {row[6]}")
            print(f"Issue Date : {row[1]}")
            print(f"Issue Time : {row[2]}")
            print(f"Return Date : {row[3]}")
            print(f"Return Time : {row[4]}")
            print(f"Fine in Rupees : {row[5]}")
            print("\033[3;34m+------------------------+\033[0m")
        print()
    else:
        print(f"No books are currently issued by the user with login id: {login_id}")
        print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def printNotesInterface() -> None:
    """
    @brief Prints the notes interface.
    """
    clearScreen()
    print("\033[3;34m+---+\033[0m")
    print("Notes")
    print("\033[3;34m+---+\033[0m\n")
    print("1: Add Notes")
    print("2: Delete Notes")
    print("3: Update Notes")
    print("4: Display Notes")
    print("5: Search Notes")
    print("6: Back")
    print("7: Exit")
    print("\033[3;34m+--------------+\033[0m\n")


def addNotes(login_id: int, db_con, db_cursor) -> None:
    """
    @brief Adds a new note to the notes table in the library database.
    @param login_id The login id of the current logged in user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+-------+\033[0m")
    print("Add Notes")
    print("\033[3;34m+-------+\033[0m\n")
    number = int(input("Enter the note's number: "))
    title = input("Enter the note's title: ")
    desc = input("Enter the note description: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(
        f"SELECT noteNumber FROM notes WHERE userId = {login_id} AND noteNumber = {number}"
    )
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        print(
            f"The note of note number: '{number}' already exists in the digital library, choose another number."
        )
    else:
        db_cursor.execute(
            f'INSERT INTO notes VALUES({login_id}, {number}, "{title}", "{desc}", CURRENT_DATE, CURRENT_TIME)'
        )
        db_con.commit()
        print(f'The note of note number: "{number}" is added successfully.')
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def deleteNotes(login_id: int, db_con, db_cursor) -> None:
    """
    @brief Deletes an already existing note from the notes table
    in the library database.
    @param login_id The login id of the current logged in user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+----------+\033[0m")
    print("Delete Notes")
    print("\033[3;34m+----------+\033[0m\n")
    number = int(input("Enter the note's number to delete: "))
    choice = input("Are you sure you want to delete the note? (Y/N): ").lower()
    print("\033[3;34m+------------------------+\033[0m\n")
    if choice in ["yes", "y"]:
        db_cursor.execute(
            f"SELECT noteNumber FROM notes WHERE userId = {login_id} AND noteNumber = {number}"
        )
        # A check to confirm that if the user can perform the action they are trying to do.
        does_exist = bool(db_cursor.fetchall())
        if does_exist:
            db_cursor.execute(
                f"DELETE FROM notes WHERE userId = {login_id} AND noteNumber = {number}"
            )
            db_con.commit()
            print(f"The note of the note number: {number} deleted successfully.")
        else:
            print(f"The note of the note number: {number} does not exist.")
    else:
        print("Note not deleted!")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def printUpdateNotesInterface() -> None:
    """
    @brief Prints the update notes interface.
    """
    clearScreen()
    print("\033[3;34m+----------+\033[0m")
    print("Update Notes")
    print("\033[3;34m+----------+\033[0m\n")
    print("1: Update Note Number")
    print("2: Update Note Title")
    print("3: Update Note Description")
    print("4: Back")
    print("5: Exit")
    print("\033[3;34m+------------------------+\033[0m\n")


def updateNoteNumber(login_id: int, db_con, db_cursor) -> None:
    """
    @brief Updates the note number of a particular note.
    @param login_id The login id of the current logged in user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+-----------------+\033[0m")
    print("Update Note Number")
    print("\033[3;34m+-----------------+\033[0m\n")
    curr_number = int(input("Enter the note number to update: "))
    new_number = int(input("Enter the new number to set: "))
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(
        f"SELECT noteNumber FROM notes WHERE userId = {login_id} AND noteNumber = {curr_number}"
    )
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f"UPDATE notes\
            SET updateDate = CURRENT_DATE,\
            updateTime = CURRENT_TIME,\
            noteNumber = {new_number}\
            WHERE userId = {login_id} AND noteNumber = {curr_number}"
        )
        db_con.commit()
        print(f"Note number: {curr_number} successfully changed to: {new_number}")
    else:
        print(f"You don't have any note with the number: {curr_number}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateNoteTitle(login_id: int, db_con, db_cursor) -> None:
    """
    @brief Updates the note title of a particular note.
    @param login_id The login id of the current logged in user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+----------------+\033[0m")
    print("Update Note Title")
    print("\033[3;34m+----------------+\033[0m\n")
    note_number = int(input("Enter the note number to update: "))
    new_title = input("Enter the new title to set: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(
        f"SELECT noteTitle FROM notes WHERE userId = {login_id} AND noteNumber = {note_number}"
    )
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f'UPDATE notes\
            SET updateDate = CURRENT_DATE,\
            updateTime = CURRENT_TIME,\
            noteTitle = "{new_title}"\
            WHERE userId = {login_id} AND noteNumber = {note_number}'
        )
        db_con.commit()
        print(
            f"Title of note with number: {note_number} successfully changed to: {new_title}"
        )
    else:
        print(f"You don't have any note with the number: {note_number}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateNoteDescription(login_id: int, db_con, db_cursor) -> None:
    """
    @brief Updates the note description of a particular note.
    @param login_id The login id of the current logged in user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+----------------------+\033[0m")
    print("Update Note Description")
    print("\033[3;34m+----------------------+\033[0m\n")
    note_number = int(input("Enter the note number to update: "))
    new_description = input("Enter the new description to set: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(
        f"SELECT noteDescription FROM notes WHERE userId = {login_id} AND noteNumber = {note_number}"
    )
    # A check to confirm that if the user can perform the action they are trying to do.
    does_exist = bool(db_cursor.fetchall())
    if does_exist:
        db_cursor.execute(
            f'UPDATE notes\
            SET updateDate = CURRENT_DATE,\
            updateTime = CURRENT_TIME,\
            noteDescription = "{new_description}"\
            WHERE userId = {login_id} AND noteNumber = {note_number}'
        )
        db_con.commit()
        print(
            f"Description of note with number: {note_number} successfully changed to: {new_description}"
        )
    else:
        print(f"You don't have any note with the number: {note_number}")
    print("\033[3;34m+------------------------+\033[0m\n")
    input("Press Enter to continue: ")


def updateNotes(login_id: int, db_con, db_cursor) -> None:
    """
    @brief The update notes screen that allows the user to update already existing notes.
    @param login_id The login id of the current logged in user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    while True:
        printUpdateNotesInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            updateNoteNumber(login_id, db_con, db_cursor)
        elif choice == "2":
            updateNoteTitle(login_id, db_con, db_cursor)
        elif choice == "3":
            updateNoteDescription(login_id, db_con, db_cursor)
        elif choice == "4":
            break
        elif choice == "5":
            exitLibrary()
        else:
            printInvalidOptionInterface()


def displayNotes(login_id: int, db_cursor) -> None:
    """
    @brief Displays the notes made by the user.
    @param login_id The login id of the current logged in user.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+-----------+\033[0m")
    print("Display Notes")
    print("\033[3;34m+-----------+\033[0m\n")
    db_cursor.execute(
        f"SELECT noteNumber, noteTitle, noteDescription, updateDate, updateTime FROM notes WHERE userId = {login_id}"
    )
    fetched = db_cursor.fetchall()
    if fetched:
        print("Your available notes are:")
        for i, row in enumerate(fetched):
            print(f"{i + 1}. Note Number : {row[0]}")
            print(f"Note Title : {row[1]}")
            print(f"Note Description : {row[2]}")
            print(f"Update Date : {row[3]}")
            print(f"Update Time : {row[4]}")
            print("\033[3;34m+------------------------+\033[0m")
        print()
    else:
        print("You currently have no notes.")
        print("\033[3;34m+------------------------+\033[0m\n")
    input("Press enter to continue: ")


def printSearchNotesInterface() -> None:
    """
    @brief Prints the search notes interface.
    """
    clearScreen()
    print("\033[3;34m+----------+\033[0m")
    print("Search Notes")
    print("\033[3;34m+----------+\033[0m\n")
    print("1: Search Note By Number")
    print("2: Search Note By Keyword")
    print("3: Back")
    print("4: Exit")
    print("\033[3;34m+-----------------------+\033[0m\n")


def searchNoteByNumber(login_id: int, db_cursor) -> None:
    """
    @brief Searches a note by the given number.
    @param login_id The login id of the current logged in user.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+-------------------+\033[0m")
    print("Search Note By Number")
    print("\033[3;34m+-------------------+\033[0m\n")
    number = int(input("Enter the note number to search: "))
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(
        f"SELECT noteTitle, noteDescription, updateDate, updateTime FROM notes WHERE userId = {login_id} AND noteNumber = {number}"
    )
    result = db_cursor.fetchall()
    if result:
        print(f"Notes available with the number: {number} are: ")
        print("\033[3;34m+------------------------+\033[0m\n")
        for i, row in enumerate(result):
            print(f"{i}. Note Number : {number}")
            print(f"Note Title : {row[0]}")
            print(f"Note Description : {row[1]}")
            print(f"Update Date : {row[2]}")
            print(f"Update Time : {row[3]}")
            print("\033[3;34m+------------------------+\033[0m")
        print()
    else:
        print(f"You currently have no notes with the number: {number}.")
        print("\033[3;34m+------------------------+\033[0m\n")
    input("Press enter to continue: ")


def searchNoteByKeyword(login_id: int, db_cursor) -> None:
    """
    @brief Searches a note by the given keyword.
    @param login_id The login id of the current logged in user.
    @param db_cursor The cursor object to the Library database.
    """
    clearScreen()
    print("\033[3;34m+--------------------+\033[0m")
    print("Search Note By Keyword")
    print("\033[3;34m+--------------------+\033[0m\n")
    keyword = input("Enter the note keyword to search: ")
    print("\033[3;34m+------------------------+\033[0m\n")
    db_cursor.execute(
        f'SELECT noteNumber, noteTitle, noteDescription, updateDate, updateTime FROM notes WHERE userId = {login_id} AND noteTitle LIKE "%{keyword}%"'
    )
    result = db_cursor.fetchall()
    if result:
        print(f"Notes available with the keyword: {keyword} are: ")
        print("\033[3;34m+------------------------+\033[0m\n")
        for i, row in enumerate(result):
            print(f"{i}. Note Number : {row[0]}")
            print(f"Note Title : {row[1]}")
            print(f"Note Description : {row[2]}")
            print(f"Update Date : {row[3]}")
            print(f"Update Time : {row[4]}")
            print("\033[3;34m+------------------------+\033[0m")
        print()
    else:
        print(f"You currently have no notes with the keyword: {keyword}.")
        print("\033[3;34m+------------------------+\033[0m\n")
    input("Press enter to continue: ")


def searchNotes(login_id: int, db_cursor) -> None:
    """
    @brief The search notes screen that allows the user to search notes
    through some parameters.
    @param login_id The login id of the current logged in user.
    @param db_cursor The cursor object to the Library database.
    """
    while True:
        printSearchNotesInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            searchNoteByNumber(login_id, db_cursor)
        elif choice == "2":
            searchNoteByKeyword(login_id, db_cursor)
        elif choice == "3":
            break
        elif choice == "4":
            exitLibrary()
        else:
            printInvalidOptionInterface()


def notes(login_id: int, db_con, db_cursor) -> None:
    """
    @brief The notes screen allowing user to manage the notes taken by them.
    @param login_id The login id of the current logged in user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    while True:
        printNotesInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            addNotes(login_id, db_con, db_cursor)
        elif choice == "2":
            deleteNotes(login_id, db_con, db_cursor)
        elif choice == "3":
            updateNotes(login_id, db_con, db_cursor)
        elif choice == "4":
            displayNotes(login_id, db_cursor)
        elif choice == "5":
            searchNotes(login_id, db_cursor)
        elif choice == "6":
            break
        elif choice == "7":
            exitLibrary()
        else:
            printInvalidOptionInterface()


def userScreen(login_id: int, db_con, db_cursor) -> None:
    """
    @brief The user screen displaying all the options for the admin.
    @param login_id The login id of the current logged in user.
    @param db_con The connection object to the Library database.
    @param db_cursor The cursor object to the Library database.
    """
    while True:
        printUserInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            aboutLibrary(db_cursor)
        elif choice == "2":
            wikipediaArticles()
        elif choice == "3":
            displayBooks(db_cursor)
        elif choice == "4":
            searchBooks(db_cursor)
        elif choice == "5":
            issuedBooksDetails(login_id, db_cursor)
        elif choice == "6":
            notes(login_id, db_con, db_cursor)
        elif choice == "7":
            break
        elif choice == "8":
            exitLibrary()
        else:
            printInvalidOptionInterface()


def printMainInterface() -> None:
    """
    @brief Prints the main screen's interface.
    """
    clearScreen()
    print(
        f"\033[1;34m{pyfiglet.figlet_format("Welcome to the", font="banner3", width=1000)}\n{pyfiglet.figlet_format("Digital Library", font="banner3", width=1000)}\033[0m"
    )
    print("\n\033[3;34m+--+\033[0m")
    print("Home")
    print("\033[3;34m+--+\033[0m\n")
    print("1: Login")
    print("2: Exit")
    print("\033[3;34m+------+\033[0m")


def loginScreen(db_cursor) -> tuple[int, str]:
    """
    @brief Prompts the user to login into their account, also provides error
    messages and a way to go back if the user doesn't want to login.
    @param db_cursor The cursor object to the Library database.
    @return A tuple containing the LoginID and if the user is admin or not.
    """
    while True:
        clearScreen()
        print("\033[3;34m+----------+\033[0m")
        print("Login Screen")
        print("\033[3;34m+----------+\033[0m\n")
        id = int(input("Enter the login id: "))
        passwd = input("Enter the password: ")
        auth_query = f"SELECT adminStatus FROM users WHERE userId = {id} AND password = '{passwd}'"

        db_cursor.execute(auth_query)
        status = db_cursor.fetchall()
        if not status:
            print("\033[3;31m+-------------------------+\033[0m")
            print("Invalid LoginID or Password")
            print("\033[3;31m+-------------------------+\033[0m\n")
            if (
                input("Press 'X' to go back, any other key to try again: ").lower()
                == "x"
            ):
                return -1, "backed"  # -1 is supposed to signify invalid user id.
            continue
        return id, status[0][0]


def main() -> None:
    """
    @brief The main application loop.
    """
    db_con, db_cursor = connectToLibrary()
    login_id = -1
    while True:
        printMainInterface()
        choice = input("Enter your choice to continue: ")
        if choice == "1":
            login_id, access_level = loginScreen(db_cursor)
            if access_level == "admin":
                adminScreen(login_id, db_con, db_cursor)
            elif access_level == "not admin":
                userScreen(login_id, db_con, db_cursor)
        elif choice == "2":
            exitLibrary()
        else:
            printInvalidOptionInterface()


# If this file is imported somewhere else, this ensures
# that the home function doesn't get called there.
if __name__ == "__main__":
    main()
