import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="her safe",
        password="@amazingselena"


    )
def abuser(abuserId,nationalId,name,age,location):
    conn=get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            INSERT INTO abuser (nationalId,name,age,location)
            Values (%s, %s, %s, %s)
    """, (nationalId,name,age,location)

    )

    conn.commit()
    conn.close()

    print("successful")

abuser(56789, "Joseph Mwangi", 45, "Umoja")