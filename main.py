import re  # To match regex patterns.
import mysql.connector as sqltor
from hashlib import sha512
import os


# ANSI CODES are used to beautify the text being printed on the screen.
# The following is the chart of color codes used.
#
# \033[91m: Red
# \033[92m: Green
# \033[93m: Yellow
# \033[94m: Blue
# \033[90m: Dark Gray
# \033[95m: Magenta (Purple)
# \033[96m: Cyan (Light Blue)
# \033[97m: White
# \033[0m: Reset (reverts to default terminal color)
#
# Background Colors:
# \033[41m: Red Background
# \033[42m: Green Background
# \033[43m: Yellow Background
# \033[44m: Blue Background
# \033[45m: Magenta Background
# \033[46m: Cyan Background
# \033[47m: White Background
# \033[40m: Black Background
#
# Some more codes:
# \033[1m: Bold
# \033[2m: Dim
# \033[3m: Italic
# \033[4m: Underline
# \033[7m: Inverse (swap foreground and background colors)
# \033[9m: Strikethrough


def create_con():
    """
    @brief This creates a connection to the SchoolProject database.
    @return tuple[Connection_OBJ, Cursor_OBJ] A tuple of the connection and cursor object of the database.
    """
    con = sqltor.connect(
        user="anand_maurya",
        passwd="ANAND6308anand",
        database="SchoolProject",
        host="localhost",
        collation="utf8mb4_unicode_520_ci",
    )
    if not con.is_connected():
        raise ConnectionError("\033[91mCan't connect to the database\033[0m")
    cursor = con.cursor()
    return con, cursor


def clear_screen() -> None:
    """
    @brief This clears the terminal screen of any content.
    """
    # For Windows
    if os.name == "nt":
        os.system("cls")
    # For macOS and Linux
    else:
        os.system("clear")


def passwd_hasher(passwd: str) -> str:
    """
    @brief This makes a sha512 hash of the given passwd.
    @param passwd: str The passwd string.
    @return str: The hashed passwd.
    """
    sha512_obj = sha512()
    sha512_obj.update(passwd.encode("utf-8"))
    return sha512_obj.hexdigest()


def make_init_admin(con, cursor) -> None:
    """
    @brief This makes the creator of the program the initial admin, if their account doesn't exist.
    @param con: Connection_OBJ The connection object to the SchoolProject database.
    @param cursor: Cursor_OBJ The cursor object to the SchoolProject database.
    """
    passwd = passwd_hasher("ANAND66308anand")
    fetch_query = "SELECT * FROM LoginData WHERE username = 'ADMIN_ANAND'"
    make_query = f"INSERT INTO LoginData VALUES('ADMIN_ANAND', '{passwd}', 'admin@gmail.com', 911000000000, 2, 1)"
    cursor.execute(fetch_query)
    # If the u_name doesn't exist then we create one
    if not cursor.fetchall():
        cursor.execute(make_query)
        con.commit()


def verify_regex(test: str, regex_pattern: re.Pattern) -> bool:
    """
    @brief This checks if the given test string matches the given pattern.
    @param test: str The string to test for matching.
    @param regex_pattern: re.Pattern The pattern that the test is to be matched against.
    @return bool: True if it matches else False.
    """
    is_matched = regex_pattern.search(test)
    # We check if the email matched and
    # if the string matched is the complete email string and not just the substring.
    if is_matched and is_matched.group() == test:
        return True
    return False


def input_username(username_regex: re.Pattern) -> str:
    username = input("\033[2m\033[1m Enter the user name: \033[0m")
    while (
        len(username) > 50
        or len(username) < 5
        or not verify_regex(username, username_regex)
    ):
        print(
            "\033[41m Username should be 5 - 50 letter long with alphabet nums and _ are permitted, Try again \033[0m"
        )
        username = input("\033[2m\033[1m Enter the user name: \033[0m")
    return username


def input_passwd() -> str:
    pass


def input_email() -> str:
    pass


def input_ph_no() -> int:
    ph_no = input("\033[2m\033[1m enter the ph_no \033[0m")
    while len(ph_no) != 10 or ph_no.isdigit():
        print("\033[41m Enter the valid ph_no\033[0m")
        ph_no = input("\033[2m\033[1m enter the ph_no \033[0m")
    return int(ph_no)


def input_access() -> int:
    access = input(
        "\033[2m\033[1m enter access level 0 for student,1 for teacher,2 for admin \033[0m:"
    )
    while access not in ("0", "1", "2"):
        print("\033[41m Enter from the mentioned above access levels only \033[0m")
        access = input(
            "\033[2m\033[1m enter access level 0 for student,1 for teacher,2 for admin \033[0m"
        )
    return int(access)

def create_account() -> None:
    print(
        "\n\033[92m\033[1m\033[3m\033[4m Your query has been accepted, your account will be verified in a few days. \033[0m\n"
    )
    # Waiting for the user to exit.
    input("\033[2m Enter any key to go back: \033[0m")


def login() -> int:
    # Access Levels:
    # 0: Student
    # 1: Teacher
    # 2: Admin
    access = 0
    return access


def student() -> None:
    pass


def teacher() -> None:
    pass


def admin() -> None:
    pass


def main() -> None:
    """
    @brief The main loop that runs the School ERP system.
    """
    mode = 0
    access = 0
    # We compile the pattern to improve performance during repeated use.
    email_pattern = r"^[\w.-]+@([\w-]+\.)+[\w]{2,4}$"
    email_regex = re.compile(email_pattern)
    username_pattern = r"[a-zA-Z_][\w_]+"
    username_regex = re.compile(username_pattern)
    con, cursor = create_con()
    make_init_admin(con=con, cursor=cursor)
    clear_screen()

    while 1:
        print(
            "\n\033[92m\033[1m\033[3m\033[4m Welcome to the school ERP SYSTEM \033[0m\n"
        )
        print("\033[96m\033[3m Here is what you can do:")
        print(" Mode '1': Create an account")
        print(" Mode '2': Login into an existing account")
        print(" Mode '3': To exit this menu \033[0m")
        mode = input("\n\033[2m\033[1m Enter the mode here: \033[0m")
        if mode not in ["1", "2", "3"]:
            print("\033[41m Enter a valid mode, Try again \033[0m")
            continue
        clear_screen()
        if mode == "1":
            create_account()
        elif mode == "2":
            access = login()
            # To clear the screen for the account stuff.
            clear_screen()
            if access == 0:
                student()
            elif access == 1:
                teacher()
            else:
                admin()
        else:
            print("\n\033[93m\033[3m Exiting the program, BYE \033[0m\n")
            break
        clear_screen()


if __name__ == "__main__":
    main()
