import re  # Used to match patterns.
import mysql.connector as sqltor  # To connect to the MYSQL database.
from hashlib import sha512  # Hashing algorithm for passwd storing.
import os  # For clearing the screen.


# ANSI COLOR CODES are used to colorize the text being printed on the screen.
# The following is the chart of color codes used.
#
# \033[91m: Red
# \033[92m: Green
# \033[93m: Yellow
# \033[94m: Blue
# \033[0m: Reset (reverts to default terminal color)


# @brief This creates the initial connection with the required database.
# @return The connection and cursor object.
def create_con():
    con = sqltor.connect(
        user="anand_maurya",
        passwd="ANAND6308anand",
        database="SchoolProject",
        host="localhost",
        collation="utf8mb4_unicode_520_ci",  # ABHIJOT REMOVE THIS LINE FOR YOUR CODE, THIS HELPS ME ONLY AS I DONT USE WINDOWS OS.
    )
    if not con.is_connected():
        print("\033[91mCan't connect to the database\033[0m")
    cursor = con.cursor()
    return con, cursor


# @brief Clears the terminal screen of any  previous content.
def clear_screen() -> None:
    # For Windows
    if os.name == "nt":
        os.system("cls")
    # For macOS and Linux
    else:
        os.system("clear")


# @brief This creates the passwd hash using sha512 hashing algorithm
# @param passwd: str The password to hash.
# @return str: The 128 bytes passwd hash.
def passwd_hasher(passwd: str) -> str:
    sha512_obj = sha512()
    sha512_obj.update(passwd.encode("utf-8"))
    return sha512_obj.hexdigest()


# @brief This checks if the given test string matches the given patter.
# @param test: str The string to test for matching.
# @param regex_pattern: re.Pattern The pattern that the test is to be matched against.
# @return bool: True if it matches else False.
def verify_regex(test: str, regex_pattern: re.Pattern) -> bool:
    is_matched = regex_pattern.search(test)
    # We check if the email matched and
    # if the string matched is the complete email string and not just the substring.
    if is_matched and is_matched.group() == test:
        return True
    return False


# @brief This prompts the user to input a valid phone number for account creation.
# @return int: The user inputted valid phone number.
def get_ph_no() -> int:
    print("\n\033[94m===============PHONE NUMBER===============\033[0m\n")
    ph_no = input("Enter Phone Number to create the account: ").strip()
    while not ph_no.isnumeric():
        print("\033[91mEnter a valid phone number\033[0m")
        ph_no = input("Enter Phone Number to create the account: ").strip()
    ph_no = int(ph_no)
    while ph_no < 1000000000 or ph_no > 9999999999:  # type: ignore
        print("\033[91mEnter a valid phone number\033[0m")
        ph_no = input("Enter Phone Number to create the account: ")
    return ph_no  # type: ignore


# @brief This prompts the user to input a valid email for account creation.
# @param email_regex: re.Pattern The email regex pattern to match the email against.
# @return str: The user inputted valid email address.
def get_email(email_regex: re.Pattern) -> str:
    print("\n\033[94m===============EMAIL===============\033[0m\n")
    # Verifying if the email is valid using regex pattern matching.
    email = input("Enter the email: ").strip()
    while len(email) > 1024 or not verify_regex(test=email, regex_pattern=email_regex):
        print(
            "\033[91mPlease enter a valid email/ Email too large to be supported\033[0m"
        )
        email = input("Enter the email: ").strip()
    return email


# @brief This prompts the user to input a valid password and secures it using sha256 encryption.
# @return The encrypted passwd hash.
def get_passwd() -> str:
    print("\n\033[94m===============PASSWORD===============\033[0m\n")
    # Getting a passwd and hashing it for security.
    passwd = input("Enter a strong passwd for your account: ").strip()
    confirm = input("Please confirm the passwd: ").strip()
    while passwd != confirm:
        print("\033[91mThe passwd and confirmation don't match up, Please check\033[0m")
        passwd = input("Enter a strong passwd for your account: ").strip()
        confirm = input("Please confirm the passwd: ").strip()
    confirm = ""
    return passwd_hasher(passwd=passwd)


# @brief This prompts the user to input a valid u_name that does not exist already.
# @param u_name: re.Pattern The regex pattern to match the u_name against.
# @param cursor: SQL_CURSOR The cursor object to the database having login table.
def get_u_name(cursor) -> str:
    print("\n\033[94m===============USER NAME===============\033[0m\n")
    u_name = input("Please enter your desired uname: ").strip()
    exist_query = f"SELECT * FROM login WHERE u_name = '{u_name}'"
    # We check if the username contains anything else than alphabets and digits and it is not currently used by someone else.
    cursor.execute(exist_query)
    already_exist = cursor.fetchall()
    while not u_name.isalnum() or already_exist:
        print(
            "\033[91mEnter a username with only alphabets and numbers OR u_name already exists.\033[0m"
        )
        u_name = input("Please enter your desired uname: ").strip()
        exist_query = f"SELECT * FROM login WHERE u_name = '{u_name}'"
        cursor.execute(exist_query)
        already_exist = cursor.fetchall()
    return u_name


# @brief This prompts the user to input the level of access this account will have.
# @return str: The access level "STU" OR "TEACH" OR "ADMIN".
def get_access_level() -> str:
    print("\n\033[94m===============ACCESS LEVEL===============\033[0m\n")
    access_level = (
        input("Enter the access level for this account STU/TEACH/ADMIN: ")
        .strip()
        .upper()
    )
    if access_level not in ["STU", "TEACH", "ADMIN"]:
        print("\033[91mEnter a valid access level.\033[0m")
        access_level = (
            input("Enter the access level for this account STU/TEACH/ADMIN: ")
            .strip()
            .upper()
        )
    return access_level


# @brief This creates an account of the user with a level of verification by the admin/teacher.
# @param email_regex: re.Pattern The regex pattern that checks for valid email.
# @param con: SQL_CONNECTION The connection object of the SchoolProject database.
# @param cursor: SQL_CURSOR The cursor object to the database having login table.
def create_account(email_regex: re.Pattern, con, cursor) -> None:
    clear_screen()
    print("\n\033[93m===============ACCOUNT CREATION===============\033[0m\n")
    ph_no = get_ph_no()
    email = get_email(email_regex=email_regex)
    passwd = get_passwd()
    u_name = get_u_name(cursor=cursor)
    # TODO: Make a level of verification for this access control.
    access_level = get_access_level()
    query = f"INSERT INTO login(email, passwd_hash, u_name, access_lvl, ph_no) VALUES('{email}', '{passwd}', '{u_name}', '{access_level}', {ph_no})"
    cursor.execute(query)
    con.commit()
    print("\n\033[92mYour account creation request has been sent to our moderators, They will respond back to you in 2-3 business days. THANK YOU\033[0m\n")


# @brief This returns appropriate number depicting if the login was successful.
# @param cursor: SQL_CURSOR The cursor object to the database having login table.
# @return int: -1: For invalid, 0: Student, 1: Teacher, 2: Admin
def login(cursor)->int:
    # We define:
    # -1 : Invalid login
    # 0 : Student
    # 1 : Teacher
    # 2 : Admin
    clear_screen()
    print("\n\033[93m===============LOGIN WINDOW===============\033[0m\n")
    u_name = input("Enter the username of the account you want to log in: ").strip()
    passwd = input("Enter the password to the account.")
    passwd = passwd_hasher(passwd=passwd)
    query = f"SELECT access_lvl, is_verified FROM login WHERE u_name = '{u_name}' AND passwd_hash = '{passwd}';"
    cursor.execute(query)
    if_exist = cursor.fetchall()
    if if_exist:
        if if_exist[0][1] == 1:
            if if_exist[0][0] == "STU":
                return 0
            elif if_exist[0][0] == "TEACH":
                return 1
            else:
                return 2
        else:
            print("\033[91mYour account has sadly not been verified yet by our admins, SORRY.\033[0m")
            return -1
    else:
        print(
            "\033[91mWrong username or password. Please check\033[0m"
        )
        return -1


def main() -> None:
    clear_screen()
    con, cursor = create_con()
    # We compile the pattern to improve performance during repeated use.
    email_pattern = r"^[\w.-]+@([\w-]+\.)+[\w]{2,4}$"
    email_regex = re.compile(email_pattern)
    print(login(cursor))

#! Sanitize input to prevent sql injection.
#! Make somewhat of a loop to prompt user to re login if invalid.
#! MAKE A METHOD FOR USER TO EXIT A PROCESS LIKE, CREATE ACCOUNT OR LOGIN mid way.


if __name__ == "__main__":
    main()
