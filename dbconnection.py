import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pradeep123#"
    )

    mycur = conn.cursor()

    # Check if connection and cursor are successfully created
    if mycur:
        print("Success")
    else:
        print("Problem in database")

    # Select the database
    mycur.execute("USE customerdata")

    # Create table if it doesn't exist
    query = "CREATE TABLE IF NOT EXISTS studentdb (name VARCHAR(100), rollno VARCHAR(100))"
    mycur.execute(query)

    print("Table created successfully!")

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    # Close cursor and connection
    if conn.is_connected():
        mycur.close()
        conn.close()
        print("Connection closed.")
