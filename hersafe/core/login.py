from .signup import get_connection

def login(useremail, userpassword):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT UserId, fullname, usergroup, gender, userpassword
        FROM usertbl
        WHERE useremail = %s
    """, (useremail,))
    user = cursor.fetchone()
    conn.close()

    if user is None:
        return {"status": "no_email"}

    if user[4] != userpassword:
        return {"status": "wrong_password"}

    return {
        "status": "success",
        "userId": user[0],
        "fullname": user[1],
        "usergroup": user[2],
        "gender": user[3]
    }