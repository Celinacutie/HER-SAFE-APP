import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="her safe",
        password="@amazingselena"
    )

def cases(userId,casedescription,datereported,abuser,witness,location,victim,abuse,action,reporter,relationship):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cases (userId,casedescription,datereported,abuser,witness,location,victim,abuse,action,reporter,relationship)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)
    """, (userId,casedescription,datereported,abuser,witness,location,victim,abuse,action,reporter,relationship))
    conn.commit()
    conn.close()
    print("User signed up successfully!")
if __name__ == "__main__":
  cases("124", 1072, "he threatened to unalive me", "2026-06-10", "Joseph Mwangi", "Alice","Umoja","Mary Njogu","threats","pending",victim,victim)