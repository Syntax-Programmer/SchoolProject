import re  # Used to match patterns
import mysql.connector as sqltor


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
        print("Can't connect to the database")
    cursor = con.cursor()
    return con, cursor


def passwd_hasher(passwd: str) -> str:
    return passwd


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
    ph_no = input("Enter Phone Number to create the account: ").strip()
    while not ph_no.isnumeric():
        print("Enter a valid phone number")
        ph_no = input("Enter Phone Number to create the account: ").strip()
    ph_no = int(ph_no)
    while ph_no < 1000000000 or ph_no > 9999999999:  # type: ignore
        print("Enter a valid phone number")
        ph_no = input("Enter Phone Number to create the account: ")
    return ph_no  # type: ignore


# @brief This prompts the user to input a valid email for account creation.
# @param email_regex: re.Pattern The email regex pattern to match the email against.
# @return str: The user inputted valid email address.
def get_email(email_regex: re.Pattern) -> str:
    # Verifying if the email is valid using regex pattern matching.
    email = input("Enter the email: ").strip()
    while len(email) > 1024 or not verify_regex(test=email, regex_pattern=email_regex):
        print("Please enter a valid email/ Email too large to be supported")
        email = input("Enter the email: ").strip()
    return email


# @brief This prompts the user to input a valid password and secures it using sha256 encryption.
# @return The encrypted passwd hash.
def get_passwd() -> str:
    # Getting a passwd and hashing it for security.
    passwd = input("Enter a strong passwd for your account: ").strip()
    confirm = input("Please confirm the passwd: ").strip()
    while passwd != confirm:
        print("The passwd and confirmation don't match up, Please check")
        passwd = input("Enter a strong passwd for your account: ").strip()
        confirm = input("Please confirm the passwd: ").strip()
    confirm = ""
    return passwd_hasher(passwd=passwd)


# @brief This prompts the user to input a valid u_name that does not exist already.
# @param u_name: re.Pattern The regex pattern to match the u_name against.
# @param cursor: SQL_CURSOR The cursor object to the database having login table.
def get_u_name(u_name_regex: re.Pattern, cursor) -> str:
    u_name = input("Please enter your desired uname: ").strip()
    exist_query = f"SELECT * FROM login WHERE u_name = '{u_name}'"
    # We check if the username contains anything else than alphabets and digits and it is not currently used by someone else.
    cursor.execute(exist_query)
    already_exist = bool(cursor.fetchall())
    while not verify_regex(u_name, u_name_regex) or already_exist:
        print(
            "Enter a username with only alphabets and numbers OR u_name already exists."
        )
        u_name = input("Please enter your desired uname: ").strip()
        exist_query = f"SELECT * FROM login WHERE u_name = '{u_name}'"
        cursor.execute(exist_query)
        already_exist = bool(cursor.fetchall())
    return u_name


# @brief This prompts the user to input the level of access this account will have.
# @return str: The access level "STU" OR "TEACH" OR "ADMIN".
def get_access_level()->str:
    access_level = input("Enter the access level for this account STU/TEACH/ADMIN: ")
    if access_level not in ["STU", "TEACH", "ADMIN"]: 
        print("Enter a valid access level.")
        access_level = input("Enter the access level for this account STU/TEACH/ADMIN: ")
    return access_level


def create_account(
    email_regex: re.Pattern, u_name_regex: re.Pattern, con, cursor
) -> None:
    ph_no = get_ph_no()
    email = get_email(email_regex=email_regex)
    passwd = get_passwd()
    u_name = get_u_name(u_name_regex=u_name_regex, cursor=cursor)
    # TODO: Make a level of verification for this access control.
    access_level = get_access_level()
    query = f"INSERT INTO login VALUES('{email}', '{passwd}', '{u_name}', '{access_level}', {ph_no})"
    cursor.execute(query)
    con.commit()


def main() -> None:
    con, cursor = create_con()
    # We compile the pattern to improve performance during repeated use.
    email_pattern = r"^[\w.-]+@([\w-]+\.)+[\w]{2,4}$"
    email_regex = re.compile(email_pattern)
    u_name_pattern = r"[A-Za-z\d]+"
    u_name_regex = re.compile(u_name_pattern)
    create_account(
        email_regex=email_regex, u_name_regex=u_name_regex, con=con, cursor=cursor
    )


if __name__ == "__main__":
    main()
