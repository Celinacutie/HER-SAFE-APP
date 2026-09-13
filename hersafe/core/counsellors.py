import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="her safe",
        password="@amazingselena"
    )

def counsellors(counsellor,userId,status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO counsellors (counsellor,userId,status)
        VALUES (%s, %s, %s)
    """, (counsellor,userId,status))
    conn.commit()
    conn.close()
    print("User signed up successfully!")

counsellors("Jane Amollo",1072,"pending")

