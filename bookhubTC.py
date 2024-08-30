import mysql.connector
from mysql.connector import Error

def create_connection():
    """
    Creates and returns a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='suraj',
            database='library_sys_db'
        )
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def create_tables():
    """
    Creates the tables in the MySQL database.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            
            # Create books table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                bname VARCHAR(100) NOT NULL,
                bcode VARCHAR(100) NOT NULL UNIQUE,
                total INT NOT NULL,
                subject VARCHAR(255) NOT NULL
            );
            """)
            print("Books table created successfully.")
            
            # Create issues table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS issues (
                issue_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                reg_No VARCHAR(100) NOT NULL,
                bcode VARCHAR(100) NOT NULL,
                contact VARCHAR(20),
                email VARCHAR(255),
                issued_date DATE NOT NULL,
                issued_at DATE NOT NULL,
                FOREIGN KEY (bcode) REFERENCES books(bcode)
            );
            """)
            print("Issues table created successfully.")
            
            # Create submit_book table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS submit_book (
                submit_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                reg_No VARCHAR(100) NOT NULL,
                bcode VARCHAR(100) NOT NULL,
                submit_date DATE NOT NULL,
                FOREIGN KEY (bcode) REFERENCES books(bcode)
            );
            """)
            print("Submit Book table created successfully.")
            
            connection.commit()
        except Error as e:
            print(f"Error while creating tables: {e}")
        finally:
            cursor.close()
            connection.close()

def insert_data():
    """
    Inserts sample data into the tables.
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            
            # Insert data into books table
            cursor.execute("""
            INSERT INTO books (bname, bcode, total, subject) VALUES
            ('Introduction to Python', 'B001', 5, 'Programming'),
            ('Advanced MySQL', 'B002', 3, 'Databases'),
            ('Learning React', 'B003', 7, 'Web Development');
            """)
            print("Data inserted into books table.")
            
            # Insert data into issues table
            cursor.execute("""
            INSERT INTO issues (name, reg_No, bcode, contact, email, issued_date, issued_at) VALUES
            ('John Doe', 'R123', 'B001', '123-456-7890', 'john.doe@example.com', '2024-08-20', '2024-08-21'),
            ('Jane Smith', 'R456', 'B002', '987-654-3210', 'jane.smith@example.com', '2024-08-22', '2024-08-23');
            """)
            print("Data inserted into issues table.")
            
            # Insert data into submit_book table
            cursor.execute("""
            INSERT INTO submit_book (name, reg_No, bcode, submit_date) VALUES
            ('John Doe', 'R123', 'B001', '2024-08-25'),
            ('Jane Smith', 'R456', 'B002', '2024-08-26');
            """)
            print("Data inserted into submit_book table.")
            
            connection.commit()
        except Error as e:
            print(f"Error while inserting data: {e}")
        finally:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_tables()
    insert_data()