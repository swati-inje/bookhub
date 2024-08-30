import mysql.connector

def create_connection():
    """
    Creates and returns a connection to the MySQL database.
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="bookhub",
        password="password",
        database="libraryM_db"
    )
    return connection