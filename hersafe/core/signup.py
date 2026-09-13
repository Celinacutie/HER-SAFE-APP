import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="her safe",
        password="@amazingselena"
    )

def signup(useremail,fullname,usergroup,userpassword,gender):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usertbl (useremail,fullname,usergroup,userpassword,gender)
        VALUES (%s, %s, %s, %s, %s)
    """, (useremail,fullname,usergroup,userpassword,gender))
    conn.commit()
    conn.close()
    print("User signed up successfully!")
if __name__ == "__main__":
  signup("feit@gmail.com", "Selinh roz", "admin", "test993", "female")