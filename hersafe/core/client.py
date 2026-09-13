import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="her safe",
        password="@amazingselena"
    )

def client(userId,fullname,nationalId,location,age,gender):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO client (userId,fullname,nationalId,location,age,gender)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (userId,fullname,nationalId,location,age,gender))
    conn.commit()
    conn.close()
    print("User signed up successfully!")

client(1076,"Mary Njogu",3459788, "Umoja",24,"female")