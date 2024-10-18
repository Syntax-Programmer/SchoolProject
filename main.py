import mysql.connector as sqltor

def create_con():
    con = sqltor.connect(user="anand_maurya", passwd="ANAND6308anand", database="SchoolProject", host="localhost")
    if not con.is_connected():
        print("Can't connect to the database")
    cursor = con.cursor()
    return con, cursor


def main():
    con, cursor = create_con()


if __name__ == "__main__":
    main()