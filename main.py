# Importing necessary libraries
import mysql.connector
import pyfiglet
import wikipediaapi
from datetime import datetime
import os

# Connect to the MySQL database
mycon = mysql.connector.connect(
    host="localhost",
    user="anand_maurya",
    password="ANAND6308anand",
    database="Library",
    collation="utf8mb4_unicode_520_ci",
)
cursor = mycon.cursor()


def clear_screen() -> None:
    # The operating system Windows.
    if os.name == "nt":
        os.system("cls")
    # The operating system is Unix-based
    else:
        os.system("clear")


# Function to display the return policy information
def returnPolicy() -> None:
    print("Return Policy : ")
    print("The issued book should be returned within 14 days(2 weeks).")
    print(
        "If the user kept the issued book for more than 14 days, then the\
    user have to pay ₹5 as fine for each extra day the user kept the issued\
    book."
    )
    print("--------------------------\n")


# Function to display a message for an invalid option
def validOption() -> None:
    print("\nPlease enter a valid option!")
    print("--------------------------\n")


# Function to handle program exit
def exiting() -> None:
    clear_screen()
    print("\033[3;34m--------------------------\033[0;0m")
    print("\033[3;33mExiting the program.")
    print("Thank You!\033[0;0m")
    print("\033[3;34m--------------------------\033[0;0m")
    exit(0)


# Function to display the user menu and handle user choices
def userMenu():
    # Displaying options for the user
    print("1. Add Note")
    print("2. Home")
    print("3. Back")
    print("4. Exit")
    # Taking user choice as input
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # Handle user choices
    if userChoice == 1:
        addNote()
    elif userChoice == 2:
        home()
    elif userChoice == 3:
        user()
    elif userChoice == 4:
        exiting()
    else:
        validOption()


# Function to display the add book menu and handle user choices
def addBookMenu():
    # Add book menu options
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # User choices handling
    if userChoice == 1:
        home()
    elif userChoice == 2:
        modifyBook()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


# Function to add a new book to the library
def addBook():
    print("--------------------------")
    print("Add Book")
    print("--------------------------")
    # Get user input for book details
    bookId = int(input("Enter the Book ID : "))
    bookName = input("Enter the Book Name : ")
    publicationYear = int(input("Enter the Book Publication Year : "))
    author = input("Enter the Book Author Name : ")
    print("--------------------------")
    cursor.execute("SELECT bookId FROM books")
    result = cursor.fetchall()
    mycon.commit()
    if (bookId,) in result:
        print(
            f'The book of book id "{bookId}" is already available in the digital library.'
        )
        print("--------------------------")
        addBookMenu()
    else:
        # Execute SQL query to insert the new book into the database
        cursor.execute(
            "INSERT INTO books (bookId, bookName, publicationYear, author) VALUES (%s, %s, %s, %s)",
            (bookId, bookName, publicationYear, author),
        )
        mycon.commit()
        # Notify the user that the book has been added successfully
        print("Book added Successfully!")
        print("--------------------------")
        addBookMenu()


# Function to display the delete book menu and handle user choices
def deleteBookMenu():
    # Delete book menu options
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # User choices handling
    if userChoice == 1:
        home()
    elif userChoice == 2:
        admin()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


# Function to delete a book from the library
def deleteBook():
    print("--------------------------")
    print("Delete Book")
    print("--------------------------")
    # Get user input for the book ID to be deleted
    bookId = int(input("Enter the Book ID : "))
    choice = input("Are you sure to delete the Book? (Yes/No) : ")
    print("--------------------------")
    cursor.execute("SELECT bookId FROM books")
    result = cursor.fetchall()
    mycon.commit()
    if choice.lower() in ["yes", "y"]:
        if (bookId,) in result:
            # Execute SQL query to delete the book from the database
            cursor.execute("DELETE FROM books WHERE bookId=%s", (bookId,))
            mycon.commit()
            # Notify the user that the book has been deleted successfully
            print("Book deleted Successfully!")
            print("--------------------------")
            deleteBookMenu()
        else:
            print(
                f'The book of book id "{bookId}" does not available in the digital library.'
            )
            print("--------------------------")
            deleteBookMenu()
    elif choice.lower() in ["no", "n"]:
        print("--------------------------")
        print("Book Not Deleted!")
        print("--------------------------")
        deleteBookMenu()
    else:
        validOption()


# Update book menu options
def updateBookMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # User choices handling
    if userChoice == 1:
        home()
    elif userChoice == 2:
        updateUser()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


def notBook(bookId):
    print(f'The book of book id "{bookId}" does not available in the digital library.')
    print("--------------------------")
    updateBookMenu()


# Function to update book details
def updateBook():
    print("--------------------------")
    print("Update Book Details")
    print("--------------------------")
    print("1. Update the Book ID")
    print("2. Update the Book Name")
    print("3. Update the Book Publication Year")
    print("4. Update the Book Author Name")
    print("5. Home")
    print("6. Back")
    print("7. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    cursor.execute("SELECT bookId FROM books")
    result = cursor.fetchall()
    mycon.commit()
    # User choices handling
    if userChoice == 1:
        currentBookId = int(input("Enter the Current Book ID : "))
        newBookId = int(input("Enter the New Book ID : "))
        if (currentBookId,) in result:
            # Execute SQL query to update the Book ID
            cursor.execute(
                "UPDATE books SET bookId=%s WHERE bookId=%s", (newBookId, currentBookId)
            )
            mycon.commit()
            print("Book ID changed Successfully!")
            print("--------------------------")
            updateBookMenu()
        else:
            notBook(currentBookId)
    elif userChoice == 2:
        bookId = int(input("Enter the Book ID : "))
        newBookName = input("Enter the New Book Name : ")
        if (bookId,) in result:
            # Execute SQL query to update the Book Name
            cursor.execute(
                "UPDATE books SET bookName=%s WHERE bookId=%s", (newBookName, bookId)
            )
            mycon.commit()
            print("Book Name changed Successfully!")
            print("--------------------------")
            updateBookMenu()
        else:
            notBook(bookId)
    elif userChoice == 3:
        bookId = int(input("Enter the Current Book ID : "))
        newPublicationYear = input("Enter the New Publication Year : ")
        if (bookId,) in result:
            # Execute SQL query to update the Publication Year
            cursor.execute(
                "UPDATE books SET publicationYear=%s WHERE bookId=%s",
                (newPublicationYear, bookId),
            )
            mycon.commit()
            print("Book Publication Year changed Successfully!")
            print("--------------------------")
            updateBookMenu()
    elif userChoice == 4:
        bookId = int(input("Enter the Current Book ID : "))
        newAuthor = input("Enter the New Author Name : ")
        if (bookId,) in result:
            # Execute SQL query to update the Author Name
            cursor.execute(
                "UPDATE books SET author=%s WHERE bookId=%s",
                (newAuthor, bookId),
            )
            mycon.commit()
            print("Book Author Name changed Successfully!")
            print("--------------------------")
            updateBookMenu()
        else:
            notBook(bookId)
    elif userChoice == 5:
        home()
    elif userChoice == 6:
        modifyBook()
    elif userChoice == 7:
        exiting()
    else:
        validOption()


# Function to display the issue book menu and handle user choices
def issueBookMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # User choices handling
    if userChoice == 1:
        home()
    elif userChoice == 2:
        admin()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


# Function to issue a book
def issueBook():
    print("--------------------------")
    print("Issue Book")
    print("--------------------------")
    bookId = input("Enter the Book ID to be Issued: ")
    userId = input("Enter the User ID to whom Book will be Issued: ")
    # Execute SQL query to check the issue status of the book
    cursor.execute("SELECT userId FROM users")
    result1 = cursor.fetchall()
    cursor.execute("SELECT bookId FROM books")
    result2 = cursor.fetchall()
    cursor.execute("SELECT issueStatus FROM books WHERE bookId=%s", (bookId,))
    result3 = cursor.fetchall()
    mycon.commit()
    if (userId,) in result1:
        if (bookId,) in result2:
            # Check if the book is not already issued
            if result3[0][0] == "not issued":
                # Execute SQL queries to update book details and mark it as issued
                cursor.execute(
                    "UPDATE books SET issueDate = CURRENT_DATE WHERE bookId = %s",
                    (bookId,),
                )
                cursor.execute(
                    "UPDATE books SET issueTime = CURRENT_TIME WHERE bookId = %s",
                    (bookId,),
                )
                cursor.execute(
                    "UPDATE books SET issueStatus = 'issued' WHERE bookId = %s",
                    (bookId,),
                )
                cursor.execute(
                    "UPDATE books SET returnDate = NULL WHERE bookId = %s", (bookId,)
                )
                cursor.execute(
                    "UPDATE books SET returnTime = NULL WHERE bookId = %s", (bookId,)
                )
                cursor.execute(
                    "UPDATE books SET issuedUserId = %s WHERE bookId = %s",
                    (userId, bookId),
                )
                mycon.commit()
                cursor.execute(
                    "select issuedUserId,bookName,issueDate,issueTime from books where bookId=%s",
                    (bookId,),
                )
                result = cursor.fetchall()
                cursor.execute(
                    "INSERT INTO issuedBooksDetails (userId,bookId,bookName,issueDate,issueTime) VALUES (%s, %s, %s, %s, %s)",
                    (result[0][0], bookId, result[0][1], result[0][2], result[0][3]),
                )
                mycon.commit()
                print("--------------------------")
                print(
                    f'Book of Book Id "{bookId}" is issued successfully to the User of User Id "{userId}".'
                )
                print("--------------------------")
                returnPolicy()
                issueBookMenu()
            else:
                # Notify the user that the book is already issued
                print(
                    f'The book of book id "{bookId}" is already issued by another user.'
                )
                print("--------------------------")
                issueBookMenu()
        else:
            print(
                f"Book with book id {bookId} does not available in the digital library."
            )
            print("--------------------------")
            issueBookMenu()
    else:
        print(f"User with user id {userId} does not exists in the digital library.")
        print("--------------------------")
        issueBookMenu()


# Function to display the return book menu and handle user choices
def returnBookMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # User choices handling
    if userChoice == 1:
        home()
    elif userChoice == 2:
        admin()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


# Function to return a book
def returnBook():
    print("--------------------------")
    print("Return Book")
    print("--------------------------")
    bookId = int(input("Enter the Book ID to be Returned: "))
    # Execute SQL query to check the issue status of the book
    cursor.execute("SELECT bookId FROM books")
    result1 = cursor.fetchall()
    cursor.execute("SELECT issueStatus FROM books WHERE bookId=%s", (bookId,))
    result2 = cursor.fetchall()
    mycon.commit()
    if (bookId,) in result1:
        # Check if the book is issued
        if result2[0][0] == "issued":
            # Execute SQL queries to update book details and mark it as returned
            cursor.execute(
                "UPDATE books SET returnDate = CURRENT_DATE WHERE bookId = %s",
                (bookId,),
            )
            cursor.execute(
                "UPDATE books SET returnTime = CURRENT_TIME WHERE bookId = %s",
                (bookId,),
            )
            cursor.execute(
                "UPDATE books SET issueStatus = 'not issued' WHERE bookId = %s",
                (bookId,),
            )
            mycon.commit()
            cursor.execute(
                "select issuedUserId,returnDate,returnTime from books where bookID = %s",
                (bookId,),
            )
            result = cursor.fetchall()
            cursor.execute(
                "UPDATE issuedBooksDetails SET returnDate = %s, returnTime = %s WHERE userId = %s AND bookId = %s",
                (result[0][1], result[0][2], result[0][0], bookId),
            )
            mycon.commit()
            cursor.execute(
                "UPDATE books SET issuedUserId = NULL WHERE bookId = %s", (bookId,)
            )
            mycon.commit()
            print(f'The book of book id "{bookId}" is returned successfully.')
            cursor.execute("select issueDate from books WHERE bookId = %s", (bookId,))
            issueDate = cursor.fetchall()
            cursor.execute("select returnDate from books WHERE bookId = %s", (bookId,))
            returnDate = cursor.fetchall()
            mycon.commit()
            cursor.execute(
                "UPDATE books SET issueDate = NULL WHERE bookId = %s", (bookId,)
            )
            cursor.execute(
                "UPDATE books SET issueTime = NULL WHERE bookId = %s", (bookId,)
            )
            cursor.execute(
                "UPDATE books SET returnDate = NULL WHERE bookId = %s", (bookId,)
            )
            cursor.execute(
                "UPDATE books SET returnTime = NULL WHERE bookId = %s", (bookId,)
            )
            mycon.commit()
            d1 = datetime.strptime(f"{issueDate[0][0]}", "%Y-%m-%d")
            d2 = datetime.strptime(f"{returnDate[0][0]}", "%Y-%m-%d")
            dateDifference = d1 - d2
            if dateDifference.days > 14:
                extraDays = dateDifference.days - 14
                fine = extraDays * 5
                print("Fine(in Rs.) : ", fine)
                cursor.execute(
                    "update issuedBooksDetails set fineInRs=%s where userId=%s and bookId=%s",
                    (fine, result[0][0], bookId),
                )
                mycon.commit()
            else:
                fine = 0 * 5
                print("Fine(in Rs.) : ", fine)
                cursor.execute(
                    "update issuedBooksDetails set fineInRs=%s where userId=%s and bookId=%s",
                    (fine, result[0][0], bookId),
                )
                mycon.commit()
                print("--------------------------")
                returnBookMenu()

        else:
            # Notify the user that the book is not issued
            print(f'The book of book id "{bookId}" is not issued by any user.')
            print("--------------------------")
            returnBookMenu()
    else:
        print(f"Book with book id {bookId} does not available in the digital library.")
        print("--------------------------")
        returnBookMenu()


# Function to display the add user menu and handle user choices
def addUserMenu():
    # Add user menu options
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # User choices handling
    if userChoice == 1:
        home()
    elif userChoice == 2:
        modifyUser()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


# Function to add a new user
def addUser():
    print("--------------------------")
    print("Add User")
    print("--------------------------")
    # Get user input for user details
    userId = int(input("Enter the User ID : "))
    userName = input("Enter the User Name : ")
    userPhoneNumber = input("Enter the User Phone Number : ")
    userEmailId = input("Enter the User Email ID : ")
    password = input("Enter the User Password : ")
    print("--------------------------")
    cursor.execute("SELECT userId FROM users")
    result = cursor.fetchall()
    mycon.commit()
    if (userId,) in result:
        print(
            f'The user of user number "{userId}" is already enrolled in the digital library.'
        )
        print("--------------------------")
        addUserMenu()
    else:
        # Execute SQL query to insert the new user into the database
        cursor.execute(
            "INSERT INTO users (userId, userName, phoneNumber, emailId, password) VALUES (%s, %s, %s, %s, %s)",
            (userId, userName, userPhoneNumber, userEmailId, password),
        )
        mycon.commit()
        # Notify the user that the user has been added successfully
        print("--------------------------")
        print("User added successfully!")
        print("--------------------------")
        addUserMenu()


# Function to display the delete user menu and handle user choices
def deleteUserMenu():
    # Delete user menu options
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # User choices handling
    if userChoice == 1:
        home()
    elif userChoice == 2:
        modifyUser()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


# Function to delete a user
def deleteUser():
    print("--------------------------")
    print("Delete User")
    print("--------------------------")
    # Get user input for the user ID to be deleted
    userId = int(input("Enter the User ID : "))
    choice = input("Are you sure to delete the User? (Yes/No) : ")
    cursor.execute("SELECT userId FROM users")
    result = cursor.fetchall()
    mycon.commit()
    if choice.lower() in ["yes", "y"]:
        if (userId,) in result:
            cursor.execute("DELETE FROM users WHERE userId=%s", (userId,))
            mycon.commit()
            # Notify the user that the user has been deleted successfully
            print("User deleted successfully!")
            print("--------------------------")
            deleteUserMenu()
        else:
            print(
                f'The user of user id "{userId}" does not enrolled in the digital library.'
            )
            print("--------------------------")
            deleteUserMenu()
    elif choice.lower() in ["no", "n"]:
        print("--------------------------")
        print("User Not Deleted!")
        print("--------------------------")
        deleteUserMenu()
    else:
        validOption()


# Function to display the update user menu and handle user choices
def updateUserMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    # User choices handling
    if userChoice == 1:
        home()
    elif userChoice == 2:
        updateUser()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


def notUser(userId):
    print(f'The user of user id "{userId}" does not enrolled in the digital library.')
    print("--------------------------")
    updateBookMenu()


# Function to update user details
def updateUser():
    print("--------------------------")
    print("Update User Details")
    print("--------------------------")
    # Display user update options
    print("1. Update the User ID")
    print("2. Update the User Name")
    print("3. Update the User Phone Number")
    print("4. Update the User Email ID")
    print("5. Update the User Password")
    print("6. Home")
    print("7. Back")
    print("8. Exit")
    # Get user choice
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    cursor.execute("SELECT userId FROM users")
    result = cursor.fetchall()
    mycon.commit()
    if userChoice == 1:
        # Update user ID
        currentUserId = int(input("Enter the Current User ID : "))
        newUserId = int(input("Enter the New User ID : "))
        if (currentUserId,) in result:
            cursor.execute(
                "update users set userId=%s where userId=%s", (newUserId, currentUserId)
            )
            mycon.commit()
            print("User ID changed Successfully!")
            print("--------------------------")
            updateUserMenu()
        else:
            notUser(currentUserId)
    elif userChoice == 2:
        # Update user name
        userId = int(input("Enter the User ID : "))
        newUserName = input("Enter the New User Name : ")
        if (userId,) in result:
            cursor.execute(
                "update users set userName=%s where userId=%s", (newUserName, userId)
            )
            mycon.commit()
            print("User Name changed Successfully!")
            print("--------------------------")
            updateUserMenu()
        else:
            notUser(userId)
    elif userChoice == 3:
        # Update user phone number
        userId = int(input("Enter the Current User ID : "))
        newPhoneNumber = input("Enter the New Phone Number : ")
        if (userId,) in result:
            cursor.execute(
                "update users set phoneNumber=%s where userId=%s",
                (newPhoneNumber, userId),
            )
            mycon.commit()
            print("User Phone Number changed Successfully!")
            print("--------------------------")
            updateUserMenu()
        else:
            notUser(userId)
    elif userChoice == 4:
        # Update user email ID
        userId = int(input("Enter the Current User ID : "))
        newEmailId = input("Enter the New Email ID : ")
        if (userId,) in result:
            cursor.execute(
                "update users set emailId=%s where userId=%s", (newEmailId, userID)
            )
            mycon.commit()
            print("User Email ID changed Successfully!")
            print("--------------------------")
            updateUserMenu()
        else:
            notUser(userId)
    elif userChoice == 5:
        # Update user password
        userId = int(input("Enter the Current User ID : "))
        newPassword = input("Enter the New Password : ")
        if (userId,) in result:
            cursor.execute(
                "update users set password=%s where userId=%s", (newPassword, userId)
            )
            mycon.commit()
            print("User Password changed Successfully!")
            print("--------------------------")
            updateUserMenu()
        else:
            notUser(userId)
    elif userChoice == 6:
        # Return to home
        home()
    elif userChoice == 7:
        # Go back to the previous menu
        modifyUser()
    elif userChoice == 8:
        # Exit the program
        exiting()
    else:
        validOption()


# Function to modify user
def modifyUser():
    print("--------------------------")
    print("Modify User")
    print("--------------------------")
    # Display user modification options
    print("1. Add User")
    print("2. Delete User")
    print("3. Update User Details")
    print("4. Home")
    print("5. Back")
    print("6. Exit")
    # Get user choice
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # User choices handling
    if userChoice == 1:
        # Add a new user
        addUser()
    elif userChoice == 2:
        # Delete a user
        deleteUser()
    elif userChoice == 3:
        # Update user details
        updateUser()
    elif userChoice == 4:
        # Return to home
        home()
    elif userChoice == 5:
        # Return to the previous menu
        admin()
    elif userChoice == 6:
        # Exit the program
        exiting()
    else:
        validOption()


# Display users menu options
def displayUsersMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    # User choices handling
    if userChoice == 1:
        home()
    elif userChoice == 2:
        admin()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


# Function to display all users
def displayUsers():
    print("--------------------------")
    print("Display Users")
    print("--------------------------")
    # Fetch all users from the database
    cursor.execute("SELECT * FROM users ORDER BY userId")
    result = cursor.fetchall()
    mycon.commit()
    if result:
        # Display user information
        print("Users enrolled in the Digital Library are :")
        i = 0
        for row in result:
            i += 1
            r = leftpad_calculator(i)
            print(f"{i}. User ID : {row[0]}")
            print(" " * r + f"User Name : {row[1]}")
            print(" " * r + f"Phone Number : {row[2]}")
            print(" " * r + f"Email ID : {row[3]}")
            print(" " * r + f"Admin Status : {row[5]}")
            print("--------------------------")
            displayUsersMenu()
    else:
        print("No users found.")
        print("--------------------------")
        displayUsersMenu()


# Search user menu options
def searchUsersMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    # User choices handling
    if userChoice == 1:
        home()
    elif userChoice == 2:
        searchUsers()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


# Function to search users by ID
def searchUsersbyId():
    print("--------------------------")
    print("Search Users by User ID")
    print("--------------------------")
    # Get user ID to search
    userId = int(input("Enter the User ID to search the User : "))
    # Search for the user in the database
    cursor.execute("SELECT * FROM users WHERE userId=%s", (userId,))
    result = cursor.fetchall()
    mycon.commit()
    if result:
        # Display user information if found
        print(f'User enrolled in the Digital Library with the User ID "{userId}" is :')
        i = 0
        for row in result:
            i += 1
            r = leftpad_calculator(i)
            print(f"{i}. User ID : {row[0]}")
            print(" " * r + f"User Name : {row[1]}")
            print(" " * r + f"Phone Number : {row[2]}")
            print(" " * r + f"Email ID : {row[3]}")
            print(" " * r + f"Admin Status : {row[5]}")
            print("--------------------------")
            searchUsersMenu()
    else:
        # Handle case when no user is found
        print(f'No user found with the user id "{userId}".')
        print("--------------------------")
        searchUsersMenu()


# Function to search users by keyword
def searchUsersbyKeyword():
    print("--------------------------")
    print("Search Users by Keyword")
    print("--------------------------")
    # Get keyword input from the user
    keyword = input("Enter a Keyword to search Users : ")
    # Search for users with the given keyword in their names
    cursor.execute(
        "SELECT * FROM users WHERE userName LIKE '%{}%' ORDER BY userId".format(keyword)
    )
    result = cursor.fetchall()
    mycon.commit()
    if result:
        # Display user information if users are found
        print(
            f'Users enrolled in the Digital Library with the Keyword "{keyword}" are :'
        )
        i = 0
        for row in result:
            i += 1
            r = leftpad_calculator(i)
            print(f"{i}. User ID : {row[0]}")
            print(" " * r + f"User Name : {row[1]}")
            print(" " * r + f"Phone Number : {row[2]}")
            print(" " * r + f"Email ID : {row[3]}")
            print(" " * r + f"Admin Status : {row[5]}")
            print("--------------------------")
            searchUsersMenu()
    else:
        # Handle case when no user is found
        print(f'No users found with the keyword "{keyword}".')
        print("--------------------------")
        searchUsersMenu()


# Function to search users
def searchUsers():
    print("--------------------------")
    print("Search Users")
    print("--------------------------")
    # User search menu
    print("1. Search by User ID")
    print("2. Search by Keyword")
    print("3. Home")
    print("4. Back")
    print("5. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # User choices handling
    if userChoice == 1:
        searchUsersbyId()
    elif userChoice == 2:
        searchUsersbyKeyword()
    elif userChoice == 3:
        home()
    elif userChoice == 4:
        admin()
    elif userChoice == 5:
        exiting()
    else:
        validOption()


# Function to modify books
def modifyBook():
    print("--------------------------")
    print("Modify Book")
    print("--------------------------")
    # Book modification menu
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Update Book Details")
    print("4. Home")
    print("5. Back")
    print("6. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # User choices handling
    if userChoice == 1:
        addBook()
    elif userChoice == 2:
        deleteBook()
    elif userChoice == 3:
        updateBook()
    elif userChoice == 4:
        home()
    elif userChoice == 5:
        admin()
    elif userChoice == 6:
        exiting()
    else:
        validOption()


# Function to display the change admin menu and handle user choices
def changeAdminMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # Handle user choices
    if userChoice == 1:
        home()
    elif userChoice == 2:
        admin()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


# Function to change the admin status
def changeAdmin():
    print("--------------------------")
    print("Change Admin")
    print("--------------------------")
    # Get new admin's ID and password from the user
    newAdminId = int(input("Enter the New Admin's User ID : "))
    newAdminPassword = input("Enter the New Admin's Password : ")
    choice = input("Are you sure to change the Admin? (Yes/No) : ")
    print("--------------------------")
    # Check if the entered user ID exists
    cursor.execute("SELECT password FROM users WHERE userId=%s", (newAdminId,))
    result = cursor.fetchall()
    mycon.commit()
    # Check the user's choice to proceed or cancel
    if choice.lower() in ["yes", "y"]:
        # If the user ID is not valid, print an error message
        if len(result) == 0:
            print("Please enter a valid user id!")
        else:
            # If the entered password matches the user's password
            if newAdminPassword == result[0][0]:
                # Update admin status for all users
                cursor.execute(
                    "UPDATE users SET adminStatus='not admin' WHERE adminStatus ='admin'"
                )
                cursor.execute(
                    "UPDATE users SET adminStatus='admin' WHERE userId=%s",
                    (newAdminId,),
                )
                mycon.commit()
                print("Admin Changed Successfully!")
                print("--------------------------")
                changeAdminMenu()
            else:
                print("Please enter a valid password!")
    elif choice.lower() in ["no", "n"]:
        print("Admin Not Changed!")
        print("--------------------------")
        changeAdminMenu()
    else:
        validOption()


def auth_user() -> int:
    clear_screen()
    print("--------------------------")
    print("Authenticate User")
    print("--------------------------\n")
    while True:
        id = int(input("Enter the user id : "))
        passwd = input("Enter the user password : ")
        status = []
        auth_query = f"SELECT adminStatus FROM users WHERE userId = {id} AND password = '{passwd}'"

        cursor.execute(auth_query)
        status = cursor.fetchall()
        if not status:
            print("---------------------------")
            print("Invalid userId or password.")
            print("---------------------------")
            continue
        break
    print("\033[0;35m----------------------\033[0;0m")
    print("\033[0;36mVerified successfully.\033[0;0m")
    print("\033[0;35m----------------------\033[0;0m")
    global USERID
    USERID = id
    return 1 if status[0][0] == "admin" else 0


def print_admin_screen() -> None:
    print("--------------------------")
    print("Admin")
    print("--------------------------\n")
    print("1: Login into User Panel")
    print("2: Modify User")
    print("3: Display Users")
    print("4: Search Users")
    print("5: Modify Book")
    print("6: Issue Book")
    print("7: Return Book")
    print("8: Change Admin")
    print("9: Back")
    print("10: Exit")
    print("--------------------------")


# Function to display the admin menu
def admin() -> None:
    while True:
        clear_screen()
        print_admin_screen()
        choice = int(input("Enter your choice to Continue : "))
        # Handle user choices
        if choice == 1:
            user()
        elif choice == 2:
            modifyUser()
        elif choice == 3:
            displayUsers()
        elif choice == 4:
            searchUsers()
        elif choice == 5:
            modifyBook()
        elif choice == 6:
            issueBook()
        elif choice == 7:
            returnBook()
        elif choice == 8:
            changeAdmin()
        elif choice == 9:
            break
        elif choice == 10:
            exiting()
        else:
            validOption()


def print_user_screen() -> None:
    print("--------------------------")
    print("User")
    print("--------------------------\n")
    print("1: About Library")
    print("2: Wikipedia Articles")
    print("3: Display Books")
    print("4: Search Books")
    print("5: Issued Books Details")
    print("6: Notes")
    print("7: Back")
    print("8: Exit")
    print("--------------------------")


# Function to display information about the library
def aboutLibrary() -> None:
    clear_screen()
    # Retrieve the name of the librarian who is also an admin
    cursor.execute("SELECT userName FROM users WHERE adminStatus='admin'")
    username = cursor.fetchall()
    # Retrieve the total number of books and users in the library
    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchall()

    print("--------------------------")
    print("About Library")
    print("--------------------------\n")
    # Display library information
    print("Year of Library's Establishment : ", 1860)
    print("Name of the Librarian : ", username[0][0])
    print("Total Number of Books Available in the Library : ", total_books[0][0])
    print("Total Number of Users Enrolled in the Library : ", total_users[0][0])
    print("--------------------------\n")
    input("Press enter to continue: ")


# Function to search & display the wikipedia articles
def wikipediaArticles() -> None:
    clear_screen()
    print("--------------------------")
    print("Search Articles")
    print("--------------------------\n")
    # Taking user input for the keyword and article length
    keyword = input("Enter the Keyword for searching the Wikipedia Article: ")
    print("--------------------------\n")
    # Creating a Wikipedia API object
    wiki = wikipediaapi.Wikipedia(language="en", user_agent="digitallibrary/1.1")
    # Fetching the page for the given search query
    page = wiki.page(keyword)
    # Checking if the page exists
    if not page.exists():
        print(
            f'Sorry, the Wikipedia Article for the keyword "{keyword}" does not exists.'
        )
    else:
        # Displaying article title
        print(f"Title: {page.title}")
        print(f"URL: {page.fullurl}")
        # Displaying a summary of the article within the specified
        print("Summary : ")
        print(page.summary)
    print("--------------------------\n")
    input("Press enter to continue: ")


# Function to display the list of books in the library
def displayBooks() -> None:
    clear_screen()
    print("--------------------------")
    print("Display Books")
    print("--------------------------\n")
    # Retrieve all books from the database
    cursor.execute(
        "SELECT bookId, bookName, publicationYear, author, issueStatus FROM books ORDER BY bookId"
    )
    books = cursor.fetchall()
    # Display books if available, otherwise notify the user
    if books:
        print("Books available in the Digital Library are :")
        print("--------------------------")
        for i, row in enumerate(books):
            print(f"{i + 1}. Book ID : {row[0]}")
            print(f"Book Name : {row[1]}")
            print(f"Publication Year : {row[2]}")
            print(f"Author Name : {row[3]}")
            print(f"Issue Status : {row[4]}")
            print("--------------------------")
    else:
        # Notify the user if no books are found
        print("No books found.")
        print("--------------------------\n")
    input("Press enter to continue: ")


# Function to search books by Book ID
def searchBooksById() -> None:
    clear_screen()
    print("--------------------------")
    print("Search Book By Id")
    print("--------------------------\n")
    # Get user input for Book ID
    id = int(input("Enter the Book ID to search the Book : "))
    print("--------------------------")
    # Execute SQL query to retrieve book information by Book ID
    cursor.execute(
        f"SELECT bookId, bookName, publicationYear, author, issueStatus FROM books WHERE bookId = {id}"
    )
    book = cursor.fetchall()
    # Display search results if books are found, otherwise notify the user
    if book:
        print(f'Book available in the Digital Library with the Book ID "{id}" is :')
        print("--------------------------")
        print(f"Book ID : {book[0][0]}")
        print(f"Book Name : {book[0][1]}")
        print(f"Publication Year : {book[0][2]}")
        print(f"Author Name : {book[0][3]}")
        print(f"Issue Status : {book[0][4]}")
    else:
        print(f'No book found with the book id "{id}".')
    print("--------------------------\n")
    input("Press enter to continue: ")


# Function to search books by keyword
def searchBooksByKeyword() -> None:
    clear_screen()
    print("--------------------------")
    print("Search Book By Keyword")
    print("--------------------------\n")
    # Get user input for keyword
    keyword = input("Enter a Keyword to search Books : ")
    print("--------------------------")
    # Execute SQL query to retrieve books by keyword
    cursor.execute(
        f"SELECT bookId, bookName, publicationYear, author, issueStatus FROM books WHERE bookName LIKE '%{keyword}%' ORDER BY bookId"
    )
    books = cursor.fetchall()
    # Display search results if books are found, otherwise notify the user
    if books:
        print(
            f'Books available in the Digital Library with the Keyword "{keyword}" are :'
        )
        print("--------------------------")
        for i, row in enumerate(books):
            print(f"{i + 1}. Book ID : {row[0]}")
            print(f"Book Name : {row[1]}")
            print(f"Publication Year : {row[2]}")
            print(f"Author Name : {row[3]}")
            print(f"Issue Status : {row[4]}")
            print("--------------------------")
        print()
    else:
        print(f'No books found with the keyword "{keyword}".')
        print("--------------------------\n")
    input("Press enter to continue: ")


# Function to display search options for books
def searchBooks() -> None:
    while True:  # To prompt user to enter again if invalid option.
        clear_screen()
        print("--------------------------")
        print("Search Books")
        print("--------------------------\n")
        print("1: Search by Book ID")
        print("2: Search by Keyword")
        print("3: Back")
        choice = int(input("Enter your Choice to Continue : "))
        # User choices handling
        if choice == 1:
            searchBooksById()
        elif choice == 2:
            searchBooksByKeyword()
        elif choice == 3:
            break
        else:
            validOption()


# Function to display the issued books details of a user
def issuedBooksDetails() -> None:
    clear_screen()
    print("--------------------------")
    print("Issued Books Details")
    print("--------------------------\n")
    returnPolicy()
    cursor.execute(
        f"SELECT bookId, bookName, issueDate, issueTime, returnDate, returnTime, fineInRs FROM issuedbooksdetails WHERE userId={USERID} ORDER BY bookId"
    )
    issued_details = cursor.fetchall()
    if issued_details:
        for i, row in enumerate(issued_details):
            print(f"{i +1}. Book ID : ", row[0])
            print("Book Name : ", row[1])
            print("Issue Date : ", row[2])
            print("Issue Time : ", row[3])
            print("Return Date : ", row[4])
            print("Return Time : ", row[5])
            print("Fine(in Rs.) : ", row[6])
            print("--------------------------")
        print()
    else:
        print("No Books Issued!")
        print("--------------------------\n")
    input("Press enter to continue: ")


# Function to add note
def addNote() -> None:
    clear_screen()
    print("--------------------------")
    print("Add Note")
    print("--------------------------\n")
    # Get note details from the user
    number = int(input("Enter the Note Number : "))
    title = input("Enter the Note Title : ")
    description = input("Enter the Note Description : ")
    print("--------------------------\n")
    cursor.execute(f"SELECT noteNumber FROM notes where userId={USERID}")
    result = cursor.fetchall()
    if (number,) in result:
        print(
            f'The note of note number "{number}" is already exists in the digital library.'
        )
    else:
        # Execute SQL query to insert the note into the database
        cursor.execute(
            f'INSERT INTO notes (userId, noteNumber, noteTitle, noteDescription, updateDate, updateTime) VALUES ({USERID}, {number}, "{title}", "{description}", CURRENT_DATE, CURRENT_TIME)',
        )
        mycon.commit()
        print(f'The note of note number "{number}" is added successfully.')
    print("--------------------------\n")
    input("Press enter to continue: ")


def print_note_does_not_exist(note_number):
    print(
        f'The note of the note number: "{note_number}" does not exists in the digital library.'
    )


# Function to delete a note
def deleteNote() -> None:
    clear_screen()
    print("--------------------------")
    print("Delete Note")
    print("--------------------------\n")
    # Get note number to be deleted from the user
    number = int(input("Enter the Note Number to Delete the Note: "))
    choice = input("Are you sure to delete the Note? (Yes): ")
    print("--------------------------\n")
    cursor.execute(f"SELECT noteNumber FROM notes where userId={USERID}")
    result = cursor.fetchall()
    if choice.lower() in ["yes", "y"]:
        if (number,) in result:
            # Execute SQL query to delete the note from the database
            cursor.execute(
                "delete FROM notes WHERE userId=%s and noteNumber=%s",
                (USERID, number),
            )
            mycon.commit()
            print(f'The note of note number "{number}" is deleted successfully.')
        else:
            print_note_does_not_exist(number)
    else:
        print("--------------------------")
        print("Note Not Deleted!")
    print("--------------------------\n")
    input("Press enter to continue: ")


# Function to display the update notes menu and handle user choices
def updateNotesMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    # Get user choice
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    # Handle user choices
    if userChoice == 1:
        home()
    elif userChoice == 2:
        updateNotes()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


def update_note_number() -> None:
    # Update Note Number
    currentNoteNumber = int(input("Enter the Current Note Number : "))
    newNoteNumber = int(input("Enter the New Note Number : "))
    cursor.execute(f"SELECT not")
    if (currentNoteNumber,) in result:
        # Update date and time
        cursor.execute(
            "update notes set updateDate=CURRENT_DATE where userId=%s and noteNumber=%s",
            (USERID, currentNoteNumber),
        )
        cursor.execute(
            "update notes set updateTime=CURRENT_TIME where userId=%s and noteNumber=%s",
            (USERID, currentNoteNumber),
        )
        # Update Note Number
        cursor.execute(
            "update notes set noteNumber=%s where userId=%s and noteNumber=%s",
            (newNoteNumber, USERID, currentNoteNumber),
        )
        mycon.commit()
        print("Note Number changed Successfully!")
        print("--------------------------")
        updateNotesMenu()
    else:
        print_note_does_not_exist(currentNoteNumber)


# Function to update a note
def updateNotes():
    clear_screen()
    print("--------------------------")
    print("Update Notes")
    print("--------------------------\n")
    # Display update options
    print("1. Update the Note Number")
    print("2. Update the Note Title")
    print("3. Update the Note Description")
    print("4. Back")
    # Get user choice
    userChoice = int(input("Enter your Choice to Continue : "))
    print("--------------------------")
    cursor.execute("SELECT noteNumber FROM notes where userId=%s", (USERID,))
    result = cursor.fetchall()
    mycon.commit()
    # Handle user choices
    if userChoice == 1:
        update_note_number()
    elif userChoice == 2:
       
            )
            # Update Note Title
            cursor.execute(
                "update notes set noteTitle=%s where userId=%s and noteNumber=%s",
                (newTitle, USERID, noteNumber),
            )
            mycon.commit()
            print("Note Title changed Successfully!")
            print("--------------------------")
            updateNotesMenu()
        else:
            print_note_does_not_exist(noteNumber)
    elif userChoice == 3:
        # Update Note Description
        noteNumber = int(input("Enter the Current Note Number : "))
        newDescription = input("Enter the New Note Description : ")
        if (noteNumber,) in result:
            # Update date and time
            cursor.execute(
                "update notes set updateDate=CURRENT_DATE where userId=%s and noteNumber=%s",
                (USERID, noteNumber),
            )
            cursor.execute(
                "update notes set updateTime=CURRENT_TIME where userId=%s and noteNumber=%s",
                (USERID, noteNumber),
            )
            # Update Note Description
            cursor.execute(
                "update notes set noteDescription=%s where userId=%s and noteNumber=%s",
                (newDescription, USERID, noteNumber),
            )
            mycon.commit()
            print("Note Description changed successfully!")
            print("--------------------------")
            updateNotesMenu()
        else:
            print_note_does_not_exist(noteNumber)
    elif userChoice == 4:
        return  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Change to break if loop is applied.
    else:
        validOption()


# Function to handle note modifications
def modifyNote():
    while True:
        clear_screen()
        print("--------------------------")
        print("Modify Notes")
        print("--------------------------\n")
        # Display modification options
        print("1. Add Note")
        print("2. Delete Note")
        print("3. Update Notes")
        print("4. Back")
        # Get user choice
        userChoice = int(input("Enter your Choice to Continue : "))
        # Handle user choices
        if userChoice == 1:
            addNote()
        elif userChoice == 2:
            deleteNote()
        elif userChoice == 3:
            updateNotes()
        elif userChoice == 4:
            break
        else:
            validOption()


# Function to display notes
def displayNotes():
    clear_screen()
    print("--------------------------")
    print("Display Notes")
    print("--------------------------\n")
    # Fetch all notes from the database
    cursor.execute(
        "SELECT noteNumber, noteTitle, noteDescription, updateDate, updateTime FROM notes ORDER BY noteNumber"
    )
    fetched_notes = cursor.fetchall()
    # Check if there are notes available
    if fetched_notes:
        print("Notes available in the Digital Library are :")
        for i, row in enumerate(fetched_notes):
            print(f"{i + 1}. Note Number : {row[0]}")
            print(f"Note Title : {row[1]}")
            print(f"Note Description : {row[2]}")
            print(f"Update Date : {row[3]}")
            print(f"Update Time : {row[4]}")
            print("--------------------------")
        print()
    else:
        # If no notes are found
        print("No notes found.")
        print("--------------------------\n")
    input("Press enter to continue: ")


# Function to display the search notes menu and handle user choices
def searchNotesMenu():
    print("1. Home")
    print("2. Back")
    print("3. Exit")
    userChoice = int(input("Enter your Choice to Continue : "))
    # Handle user choices
    if userChoice == 1:
        home()
    elif userChoice == 2:
        searchNotes()
    elif userChoice == 3:
        exiting()
    else:
        validOption()


# Function to search notes by note number
def searchNotesbynoteNumber():
    # Get the note number to search
    noteNumber = int(input("Enter the Note Number to search the Note : "))
    # Execute SQL query to fetch notes with the given note number
    cursor.execute("SELECT * FROM notes WHERE bookId=%s", (noteNumber,))
    result = cursor.fetchall()
    mycon.commit()
    # Check if notes are found
    if result:
        print(
            f'Note available in the Digital Library with the Note Number "{noteNumber}" is :'
        )
        i = 0
        for row in result:
            i += 1
            r = leftpad_calculator(i)
            print(f"{i}. Note Number : {row[1]}")
            print(" " * r + f"Note Title : {row[2]}")
            print(" " * r + f"Note Description : {row[3]}")
            print("--------------------------")
            searchNotesMenu()
    else:
        # If no notes are found with the given note number
        print(f'No note found with the note number "{noteNumber}".')
        print("--------------------------")
        searchNotesMenu()


# Function to search notes by keyword
def searchNotesbyKeyword():
    print("--------------------------")
    print("Search Notes by Keyword")
    print("--------------------------")
    # Get keyword from user
    keyword = input("Enter a Keyword to search Notes : ")
    # Execute SQL query to fetch notes with the given keyword in the title
    cursor.execute(
        "SELECT * FROM notes WHERE noteTitle LIKE '%{}%' ORDER BY noteNumber".format(
            keyword
        )
    )
    result = cursor.fetchall()
    mycon.commit()
    # Check if notes are found
    if result:
        print(
            f'Notes available in the Digital Library with the Keyword "{keyword}" are :'
        )
        i = 0
        for row in result:
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            i += 1
            r = leftpad_calculator(i)
            print(f"{i}. Note Number : {row[1]}")
            print(" " * r + f"Note Title : {row[2]}")
            print(" " * r + f"Note Description : {row[3]}")
            print("--------------------------")
            searchNotesMenu()
    else:
        # If no notes are found with the given keyword
        print(f'No notes found with the keyword "{keyword}".')
        print("--------------------------")
        searchNotesMenu()


# Function to handle note searching
def searchNotes():
    print("--------------------------")
    print("Search Notes")
    print("--------------------------")
    # Display search options
    print("1. Search by Note Number")
    print("2. Search by Keyword")
    print("3. Home")
    print("4. Back")
    print("5. Exit")
    # Get user choice
    userChoice = int(input("Enter your Choice to Continue : "))
    # Handle user choices
    if userChoice == 1:
        searchNotesbynoteNumber()
    elif userChoice == 2:
        searchNotesbyKeyword()
    elif userChoice == 3:
        notes()
    elif userChoice == 4:
        modifyNote()
    elif userChoice == 5:
        exiting()
    else:
        validOption()


# Function to manage notes
def notes():
    while True:
        clear_screen()
        print("--------------------------")
        print("Notes")
        print("--------------------------\n")
        print("1. Modify Note")
        print("2. Display Notes")
        print("3. Search Notes")
        print("4. Back")
        # Get user choice
        userChoice = int(input("Enter your Choice to Continue : "))
        print("--------------------------")
        # Handle user choices
        if userChoice == 1:
            modifyNote()
        elif userChoice == 2:
            displayNotes()
        elif userChoice == 3:
            searchNotes()
        elif userChoice == 4:
            break
        else:
            validOption()


# Function to display the user menu
def user() -> None:
    while True:
        clear_screen()
        print_user_screen()
        choice = int(input("Enter your choice to Continue : "))
        # Handle user choices
        if choice == 1:
            aboutLibrary()
        elif choice == 2:
            wikipediaArticles()
        elif choice == 3:
            displayBooks()
        elif choice == 4:
            searchBooks()
        elif choice == 5:
            issuedBooksDetails()
        elif choice == 6:
            notes()
        elif choice == 7:
            break
        elif choice == 8:
            exiting()
        else:
            validOption()


def print_home_screen() -> None:
    print(
        f"\033[1;31m{pyfiglet.figlet_format("Welcome to the", font="banner3", width=1000)}\n{pyfiglet.figlet_format("Digital Library", font="banner3", width=1000)}\033[0m"
    )
    print("\n--------------------------")
    print("Home")
    print("--------------------------\n")
    print("1: Login")
    print("2: Exit")
    print("--------------------------")


# Function to display the main menu
def home():
    while True:
        clear_screen()
        print_home_screen()
        user_choice = int(input("Enter your Choice to Continue : "))
        # Handle user choices
        if user_choice == 1:
            auth_level = auth_user()
            if auth_level == 0:
                user()
            elif auth_level == 1:
                admin()
        elif user_choice == 2:
            exiting()
        else:
            validOption()
            input("Press enter to continue: ")


if __name__ == "__main__":
    home()
